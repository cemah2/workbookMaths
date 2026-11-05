"""Session setup for every notebook: seeds, device, plot style, environment report."""

from __future__ import annotations

import importlib
import importlib.util
import os
import platform
import random
import sys
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path

from wbm._versions import EXPECTED_VERSIONS, PYTHON_EXPECTED

# Files that identify the root of the workbook repository.
_ROOT_MARKERS = (Path("src") / "wbm" / "__init__.py", Path("docs"))


@dataclass
class Config:
    """What ``wbm.setup()`` decided for this session."""

    seed: int = 42
    fast: bool = True
    device: str = "cpu"
    is_colab: bool = False
    root: Path | None = None
    torch_available: bool = False
    extras: dict = field(default_factory=dict)

    def __repr__(self) -> str:  # compact, readable in a notebook
        return (
            f"Config(seed={self.seed}, fast={self.fast}, device='{self.device}', "
            f"colab={self.is_colab}, torch={self.torch_available})"
        )


# The last configuration created by setup(); used by by_mode() and others.
CONFIG = Config()


# ---------------------------------------------------------------------------
# Environment helpers
# ---------------------------------------------------------------------------
def is_colab() -> bool:
    """Return True when running inside Google Colab."""
    if "google.colab" in sys.modules:
        return True
    if os.environ.get("COLAB_RELEASE_TAG") or os.environ.get("COLAB_GPU"):
        return True
    try:
        return importlib.util.find_spec("google.colab") is not None
    except (ImportError, ValueError):
        return False


def _is_root(path: Path) -> bool:
    return all((path / marker).exists() for marker in _ROOT_MARKERS)


def repo_root(start: str | Path | None = None) -> Path:
    """Locate the workbook repository root.

    Order: the ``WBM_ROOT`` environment variable, then the parents of ``start``
    (default: current directory), then the parents of this file.
    """
    env = os.environ.get("WBM_ROOT")
    if env and _is_root(Path(env)):
        return Path(env).resolve()
    candidates = [Path(start) if start else Path.cwd(), Path(__file__).resolve()]
    for base in candidates:
        base = base.resolve()
        for path in (base, *base.parents):
            if _is_root(path):
                return path
    raise FileNotFoundError(
        "Impossible de trouver la racine du dépôt (dossier contenant src/wbm et docs/). "
        "Lance le notebook depuis le dépôt, ou définis la variable d'environnement WBM_ROOT."
    )


def _import_torch():
    """PyTorch if a notebook already imported it, else None.

    workbookMaths never needs PyTorch: it is not imported here (importing it takes seconds), but if it is already
    loaded, ``seed_everything`` seeds it too.
    """
    return sys.modules.get("torch")


def _torch_installed() -> bool:
    return _import_torch() is not None


def get_device(prefer_mps: bool = False) -> str:
    """Return ``"cuda"`` if a GPU is available, otherwise ``"cpu"``.

    Apple GPUs (``"mps"``) are only used when ``prefer_mps=True``: they are
    fast but some operations are missing or non-deterministic.
    """
    torch = _import_torch()
    if torch is None:
        return "cpu"
    if torch.cuda.is_available():
        return "cuda"
    if prefer_mps and getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def seed_everything(seed: int = 42, deterministic: bool = False) -> None:
    """Fix the random seeds of ``random``, NumPy and (if installed) PyTorch."""
    import numpy as np

    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)  # only affects subprocesses
    torch = _import_torch()
    if torch is not None:
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        if deterministic:
            torch.use_deterministic_algorithms(True, warn_only=True)
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False


def _env_flag(name: str) -> bool | None:
    value = os.environ.get(name)
    if value is None:
        return None
    return value.strip().lower() in {"1", "true", "yes", "oui", "fast"}


def _version_of(module_name: str) -> str | None:
    if module_name in sys.modules:
        return getattr(sys.modules[module_name], "__version__", "?")
    try:
        from importlib.metadata import PackageNotFoundError, version

        from wbm._versions import DIST_NAMES

        try:
            return version(DIST_NAMES.get(module_name, module_name))
        except PackageNotFoundError:
            return None
    except ImportError:  # pragma: no cover
        return None


def _same_minor(found: str, expected) -> bool:
    """True if ``found`` has the minor version of ``expected`` (a version, or a tuple of accepted versions)."""
    base = found.split("+")[0].split(".")
    accepted = (expected,) if isinstance(expected, str) else tuple(expected)
    return any(base[:2] == version.split(".")[:2] for version in accepted)


def environment_report(config: Config | None = None) -> str:
    """Build a short, human-readable description of the environment."""
    config = config or CONFIG
    lines = ["🧪 workbookMaths : environnement"]
    if config.is_colab:
        where = "Google Colab"
    else:
        where = f"Local ({platform.system()} {platform.machine()}, {os.cpu_count()} CPU)"
    gpu = ""
    if config.device == "cuda":
        gpu = f" · GPU : {_import_torch().cuda.get_device_name(0)}"
    lines.append(f"   Plateforme : {where}{gpu}")

    py = platform.python_version()
    versions = [f"Python {py}"]
    drift = []
    if not py.startswith(PYTHON_EXPECTED):
        drift.append(f"Python {py} (workbook testé avec {PYTHON_EXPECTED})")
    for module_name, expected in EXPECTED_VERSIONS.items():
        found = _version_of(module_name)
        label = "scikit-learn" if module_name == "sklearn" else module_name
        if found is None:
            versions.append(f"{label} ✗")
            continue
        versions.append(f"{label} {found}")
        if not _same_minor(found, expected):
            wanted = expected if isinstance(expected, str) else " ou ".join(expected)
            drift.append(f"{label} {found} (attendu {wanted})")
    lines.append("   " + " | ".join(versions))
    lines.append(f"   Graine : {config.seed} | FAST_MODE : {config.fast}")
    if drift:
        lines.append("   ⚠️ Versions différentes de celles du workbook : " + " ; ".join(drift))
        lines.append("      Ça marche en général, mais des résultats peuvent varier légèrement.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
def setup(
    seed: int = 42,
    fast: bool = True,
    *,
    verbose: bool = True,
    style: bool = True,
    deterministic: bool = False,
    prefer_mps: bool = False,
) -> Config:
    """Prepare a notebook session and return a :class:`Config`.

    - fixes the seeds (random, NumPy, PyTorch if installed);
    - picks the device (``cuda`` if available, else ``cpu``);
    - applies the workbook plot style;
    - prints a short report of the environment.

    The environment variable ``WBM_FAST_MODE`` (0/1) overrides ``fast``; it is
    used by ``tools/run_all_notebooks.py --full``.
    """
    global CONFIG

    override = _env_flag("WBM_FAST_MODE")
    if override is not None:
        fast = override

    seed_everything(seed, deterministic=deterministic)
    torch_ok = _torch_installed()
    try:
        root = repo_root()
    except FileNotFoundError:
        root = None

    CONFIG = Config(
        seed=seed,
        fast=bool(fast),
        device=get_device(prefer_mps=prefer_mps),
        is_colab=is_colab(),
        root=root,
        torch_available=torch_ok,
    )
    if style:
        from wbm import plot

        plot.set_style()
    if verbose:
        print(environment_report(CONFIG))
    return CONFIG


def by_mode(fast, full):
    """Return ``fast`` in FAST_MODE, ``full`` otherwise.

    Example: ``n_epochs = wbm.by_mode(fast=2, full=20)``.
    """
    return fast if CONFIG.fast else full


# distribution name -> import name, when they differ
_IMPORT_NAMES = {
    "scikit-learn": "sklearn",
    "umap-learn": "umap",
    "pillow": "PIL",
    "huggingface_hub": "huggingface_hub",
    "huggingface-hub": "huggingface_hub",
}


def _pinned_versions() -> dict[str, str]:
    """``{distribution: version}`` read from requirements.txt (empty if not found)."""
    try:
        path = repo_root() / "requirements.txt"
    except FileNotFoundError:
        return {}
    pins = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#")[0].strip()
        if "==" in line:
            name, version = line.split("==", 1)
            pins[name.strip().lower()] = version.strip()
    return pins


def ensure(*packages: str, quiet: bool = True) -> list[str]:
    """Install the listed packages only if they cannot be imported.

    Versions come from ``requirements.txt``. Example (Colab or local):
    ``wbm.ensure("gymnasium", "umap-learn")``. Returns what was installed.
    """
    import subprocess

    pins = _pinned_versions()
    to_install = []
    for dist in packages:
        module = _IMPORT_NAMES.get(dist.lower(), dist.replace("-", "_"))
        try:
            found = importlib.util.find_spec(module) is not None
        except (ImportError, ValueError):
            found = False
        if not found:
            version = pins.get(dist.lower())
            to_install.append(f"{dist}=={version}" if version else dist)
    if to_install:
        print("📦 Installation : " + ", ".join(to_install))
        cmd = [sys.executable, "-m", "pip", "install", *to_install]
        if quiet:
            cmd.insert(4, "-q")
        subprocess.run(cmd, check=True)
        importlib.invalidate_caches()
    return to_install


@contextmanager
def timer(label: str = "durée", verbose: bool = True):
    """Measure the wall-clock time of a block: ``with wbm.timer("entraînement"): ...``."""
    result = {"seconds": None}
    start = time.perf_counter()
    try:
        yield result
    finally:
        result["seconds"] = time.perf_counter() - start
        if verbose:
            print(f"⏱️ {label} : {result['seconds']:.2f} s")
