"""Load one implementation of the ``mymath`` library under the name ``mymath``.

Three implementations live in the repository:

* ``learner`` -> ``mon_travail/mymath/``  (the learner's own code, default)
* ``ref``     -> ``solutions/mymath_ref/`` (reference implementation)
* ``stubs``   -> ``templates/mymath_stubs/`` (empty skeletons; used by Claude
  to prove that the tests fail before anything is implemented)

Whichever is chosen is registered in ``sys.modules`` as ``mymath``, so
``from mymath.metrics import f1`` works the same way everywhere (notebooks,
tests). Submodules are also imported on first attribute access, so
``mymath.metrics.f1`` works without an explicit import. Inside the packages,
imports between modules must be *relative* (``from .utils import x``).

Fallback (``fallback="ref"``, learner only): a module that is missing from the
learner's package is taken from the reference, so that skipping a chapter does
not break the later ones (e.g. ``eigen.py`` of M12c imports ``matrices.py`` of
M09a). With ``chapter="M12c"`` only the modules of chapters *before* M12c
may come from the reference: the modules you are writing never do, so a check
can never pass with the reference's code instead of yours.
"""

from __future__ import annotations

import importlib
import importlib.abc
import importlib.util
import json
import os
import sys
from pathlib import Path

from wbm.core import repo_root
from wbm.errors import MymathMissingError, MymathNotFoundError

IMPLEMENTATIONS = {
    "learner": Path("mon_travail") / "mymath",
    "ref": Path("solutions") / "mymath_ref",
    "stubs": Path("templates") / "mymath_stubs",
}

# Study order of the math chapters (single source: wbm.chapters).
from wbm.chapters import CHAPTER_ORDER, canonical_id  # noqa: E402

__all__ = ["CHAPTER_ORDER", "IMPLEMENTATIONS", "load_mymath", "modules_before", "mymath_path",
           "MymathNotFoundError"]


class _MissingPackage:
    """Placeholder returned by ``load_mymath(..., missing_ok=True)``.

    Any attribute access raises :class:`MymathMissingError`, which
    ``wbm.attempt`` reports as "⏳ pas encore fait" instead of crashing.
    """

    def __init__(self, message: str):
        self._message = message

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError(name)
        raise MymathMissingError(self._message)

    def __repr__(self) -> str:
        return "<mymath absent : lance tools/start_chapter.py>"


def mymath_path(impl: str = "learner", root: str | Path | None = None) -> Path:
    """Directory of the requested implementation."""
    if impl not in IMPLEMENTATIONS:
        raise ValueError(f"impl must be one of {sorted(IMPLEMENTATIONS)}, not {impl!r}")
    root = Path(root) if root else repo_root()
    return root / IMPLEMENTATIONS[impl]


def _attach_lazy_getattr(module) -> None:
    """Let ``module.sub`` import the submodule ``sub`` on first access (packages only)."""
    if hasattr(module, "__path__") and "__getattr__" not in module.__dict__:
        module.__getattr__ = _make_lazy_getattr(module.__name__)


def _make_lazy_getattr(prefix: str):
    def __getattr__(name: str):
        if name.startswith("__"):
            raise AttributeError(name)
        full = f"{prefix}.{name}"
        try:
            submodule = importlib.import_module(full)
        except ModuleNotFoundError as exc:
            if exc.name and (full == exc.name or full.startswith(exc.name + ".")):
                raise MymathMissingError(
                    f"le module {full} n'existe pas encore dans ta librairie : "
                    "lance tools/start_chapter.py pour ce chapitre"
                ) from None
            raise
        _attach_lazy_getattr(submodule)  # nested packages: mymath.nn.activations
        return submodule

    return __getattr__


def _manifest(root: str | Path | None = None) -> dict:
    root = Path(root) if root else repo_root()
    path = root / IMPLEMENTATIONS["stubs"] / "MANIFEST.json"
    if not path.exists():
        return {"base": [], "chapters": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_chapter(chapter: str) -> str:
    """'m12C' -> 'M12c', 'r3' -> 'R3' (ValueError for an unknown id)."""
    return canonical_id(chapter)


def modules_before(chapter: str | None, root: str | Path | None = None) -> set[str] | None:
    """Stub files (e.g. ``"matrices.py"``) published before ``chapter``.

    ``None`` for ``chapter=None`` (no restriction). The base files (``_example.py``...)
    are never included: every learner has them (``start_chapter.py --init``) and
    ``_example.mean`` is itself an exercise of chapter R0.
    """
    if chapter is None:
        return None
    rank = CHAPTER_ORDER.index(_canonical_chapter(chapter))
    manifest = _manifest(root)
    allowed: set[str] = set()
    for cid, files in manifest.get("chapters", {}).items():
        if cid in CHAPTER_ORDER and CHAPTER_ORDER.index(cid) < rank:
            allowed.update(files)
    return allowed


# The fallback modules already announced in this session, (learner folder, module name): a notebook reloads the
# library before each exercise, and the ℹ️ line says once that the reference replaces a missing module.
_ANNOUNCED: set[tuple[str, str]] = set()


class _FallbackFinder(importlib.abc.MetaPathFinder):
    """Import ``alias.x`` from ``fallback`` when the learner's package has no module ``x``."""

    def __init__(self, alias: str, primary: Path, fallback: Path, allowed: set[str] | None,
                 notify: bool, owners: dict[str, str]):
        self.alias, self.primary, self.fallback = alias, primary, fallback
        self.allowed, self.notify, self.owners = allowed, notify, owners
        self.used: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if not fullname.startswith(self.alias + "."):
            return None
        rel = "/".join(fullname.split(".")[1:])
        if (self.primary / f"{rel}.py").exists() or (self.primary / rel / "__init__.py").exists():
            return None  # the learner's own module wins
        package = self.fallback / rel / "__init__.py"
        module = self.fallback / f"{rel}.py"
        if package.exists():
            # its sub-modules are searched in the learner's folder only: each one comes
            # back through this finder, which applies the same rule to it
            candidate, rel_file = package, f"{rel}/__init__.py"
            locations = [str(self.primary / rel)]
        elif module.exists():
            candidate, rel_file, locations = module, f"{rel}.py", None
        else:
            return None
        if self.allowed is not None and rel_file not in self.allowed:
            return None  # a module of this chapter or a later one: never replaced
        self.used.append(fullname)
        if self.notify and locations is None and (str(self.primary), fullname) not in _ANNOUNCED:
            _ANNOUNCED.add((str(self.primary), fullname))
            owner = self.owners.get(rel_file)
            where = f" (ch. {owner})" if owner else ""
            print(f"ℹ️ {fullname} : tu n'as pas ce module{where}, "
                  "la référence est utilisée.")
        return importlib.util.spec_from_file_location(
            fullname, candidate, submodule_search_locations=locations)


def _remove_finders(alias: str) -> None:
    sys.meta_path[:] = [f for f in sys.meta_path
                        if not (isinstance(f, _FallbackFinder) and f.alias == alias)]


def _forget(alias: str) -> None:
    for name in list(sys.modules):
        if name == alias or name.startswith(alias + "."):
            del sys.modules[name]
    _remove_finders(alias)
    importlib.invalidate_caches()


def load_mymath(
    impl: str | None = None,
    *,
    path: str | Path | None = None,
    root: str | Path | None = None,
    alias: str = "mymath",
    missing_ok: bool = False,
    verbose: bool = False,
    fallback: str | None = None,
    chapter: str | None = None,
    notify: bool = True,
):
    """Import an implementation of mymath and register it as ``alias``.

    ``impl`` defaults to the ``WBM_IMPL`` environment variable, else ``"learner"``.
    ``path`` points to another directory (used by the tests of the mechanism).
    With ``missing_ok=True`` a missing package returns a placeholder whose use
    prints "⏳ pas encore fait" inside ``wbm.attempt`` (exercise notebooks).
    ``fallback="ref"`` (learner only): modules missing from the learner's package
    come from the reference; with ``chapter`` given, only the modules of earlier
    chapters (see ``modules_before``). ``notify`` prints a line for each of them, once
    per session (a notebook reloads the library before each exercise).
    """
    impl = impl or os.environ.get("WBM_IMPL", "learner")
    pkg_dir = Path(path) if path else mymath_path(impl, root)
    init = pkg_dir / "__init__.py"
    if not init.exists():
        if impl == "learner" and not path:
            message = (
                "ta librairie mymath n'existe pas encore dans mon_travail/mymath/ ; "
                f"lance d'abord : python tools/start_chapter.py {chapter or '--init'}"
            )
        else:
            message = f"aucun package mymath trouvé dans {pkg_dir}"
        _forget(alias)  # never leave a previously loaded implementation (e.g. ref) in place
        if missing_ok:
            print("ℹ️ " + message[0].upper() + message[1:] + ".")
            return _MissingPackage(message)
        raise MymathNotFoundError(message)

    _forget(alias)  # forget any previously loaded implementation (and its submodules)

    spec = importlib.util.spec_from_file_location(
        alias, init, submodule_search_locations=[str(pkg_dir)]
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[alias] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        del sys.modules[alias]
        raise
    _attach_lazy_getattr(module)
    module.__wb_impl__ = impl if not path else f"{impl}:{pkg_dir}"
    module.__wb_fallback__ = None
    if fallback is not None and impl == "learner":
        fb_dir = mymath_path(fallback, root)
        manifest = _manifest(root)
        owners = {}
        for cid, files in manifest.get("chapters", {}).items():
            for rel in files:
                owners.setdefault(rel, cid)
        finder = _FallbackFinder(alias, pkg_dir, fb_dir, modules_before(chapter, root), notify,
                                 owners)
        sys.meta_path.insert(0, finder)
        module.__wb_fallback__ = finder
    # Import the subpackages of the learner's package now (their __init__.py import nothing) and give them the
    # lazy getattr: otherwise a first `from mymath.nn.activations import relu` creates mymath.nn through the
    # import system, without it, and `mymath.nn.backward` then raises AttributeError until imported explicitly.
    for init_file in sorted(pkg_dir.glob("*/__init__.py")):
        try:
            _attach_lazy_getattr(importlib.import_module(f"{alias}.{init_file.parent.name}"))
        except Exception:  # a broken subpackage: its own import will say why, later, inside wbm.attempt
            pass
    if verbose:
        print(f"📦 mymath chargé depuis {pkg_dir} (implémentation : {impl})")
    return module
