#!/usr/bin/env python
"""Check that your environment is ready for workbookMaths.

    python 00_setup/check_env.py          # from the repository root
    python 00_setup/check_env.py --quick  # skip the slower checks (SymPy computation, pytest)

Works with a bare Python: missing packages are reported, not fatal.
Exit code 0 = ready (warnings allowed), 1 = something important is missing.
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# import name -> distribution name in requirements.txt
PACKAGES = {
    "numpy": "numpy", "scipy": "scipy", "sympy": "sympy", "matplotlib": "matplotlib", "pandas": "pandas",
    "sklearn": "scikit-learn", "pytest": "pytest", "nbformat": "nbformat", "nbclient": "nbclient",
}
CRITICAL = {"numpy", "scipy", "sympy", "matplotlib", "pytest"}
NEEDED_FROM = {"sklearn": "M09b (oracles des moindres carrés)", "pandas": "M02c", "nbformat": "outils",
               "nbclient": "outils"}
DATA_FILES: list[str] = []   # light datasets are added with the chapters that use them (BIBLE §10)

results = {"ok": 0, "warn": 0, "fail": 0}


def report(status: str, message: str) -> None:
    icon = {"ok": "✅", "warn": "⚠️ ", "fail": "❌"}[status]
    results[status] += 1
    print(f"  {icon} {message}")


def pinned_versions() -> dict[str, str]:
    pins = {}
    req = ROOT / "requirements.txt"
    if req.exists():
        for line in req.read_text(encoding="utf-8").splitlines():
            line = line.split("#")[0].strip()
            if "==" in line:
                name, version = line.split("==", 1)
                pins[name.strip().lower()] = version.strip()
    return pins


def check_python() -> None:
    print("\n1. Python")
    version = platform.python_version()
    if sys.version_info >= (3, 12):
        report("ok", f"Python {version} ({sys.executable})")
    elif sys.version_info >= (3, 11):
        report("warn", f"Python {version} : ça fonctionne, mais le workbook vise Python 3.13 (comme Colab)")
    else:
        report("fail", f"Python {version} : trop ancien, installe Python 3.13 (voir 00_setup/INSTALL_LOCAL.md)")
    if sys.prefix == sys.base_prefix and "COLAB_RELEASE_TAG" not in os.environ:
        report("warn", "pas d'environnement virtuel actif : recommandé (voir INSTALL_LOCAL.md, étape 4)")


def check_packages() -> dict:
    print("\n2. Bibliothèques")
    pins = pinned_versions()
    found = {}
    for module, dist in PACKAGES.items():
        try:
            mod = importlib.import_module(module)
        except Exception:
            status = "fail" if module in CRITICAL else "warn"
            when = f" (nécessaire à partir du {NEEDED_FROM[module]})" if module in NEEDED_FROM else ""
            report(status, f"{dist} manquant{when}")
            continue
        version = getattr(mod, "__version__", "?")
        found[module] = version
        expected = pins.get(dist)
        if expected and version.split("+")[0].split(".")[:2] != expected.split(".")[:2]:
            report("warn", f"{dist} {version} (le workbook est testé avec {expected})")
        else:
            report("ok", f"{dist} {version}")
    return found


def check_sympy(found: dict, quick: bool) -> None:
    print("\n3. Calcul symbolique")
    if "sympy" not in found:
        report("fail", "SymPy absent : pip install -r requirements.txt")
        return
    if quick:
        report("warn", "calcul SymPy ignoré (--quick)")
        return
    import sympy

    x = sympy.Symbol("x")
    ok = sympy.simplify(sympy.diff(sympy.exp(x**2), x) - 2 * x * sympy.exp(x**2)) == 0
    report("ok" if ok else "fail", "SymPy dérive exp(x²) correctement")


def check_repo() -> None:
    print("\n4. Dépôt workbookMaths")
    sys.path.insert(0, str(ROOT / "src"))
    try:
        import wbm

        report("ok", f"package wbm {wbm.__version__} importable")
    except Exception as exc:
        report("fail", f"import wbm impossible : {exc}")
        return
    for rel in DATA_FILES:
        path = ROOT / rel
        if path.exists():
            report("ok", f"{rel} ({path.stat().st_size / 1e6:.2f} Mo)")
        else:
            report("fail", f"{rel} manquant : fais `git pull`")
    try:
        answers = json.loads((ROOT / "src" / "wbm" / "answers.json").read_text(encoding="utf-8"))
        report("ok", f"answers.json lisible ({len(answers.get('answers', {}))} réponses)")
    except Exception as exc:
        report("fail", f"answers.json illisible : {exc}")
    learner = ROOT / "mon_travail" / "mymath" / "__init__.py"
    if learner.exists():
        report("ok", "ta librairie mon_travail/mymath existe")
    else:
        report("warn", "mon_travail/mymath pas encore créé : python tools/start_chapter.py --init")


def check_tests(quick: bool) -> None:
    print("\n5. Tests")
    if quick:
        report("warn", "tests ignorés (--quick)")
        return
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_example_mymath.py", "--impl=ref", "-q",
         "-p", "no:cacheprovider", "--color=no"],
        cwd=ROOT, capture_output=True, text=True,
    )
    last = (proc.stdout.strip().splitlines() or ["(pas de sortie)"])[-1]
    report("ok" if proc.returncode == 0 else "fail", f"pytest --impl=ref : {last}")


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):  # emoji on Windows consoles and pipes
        sys.stdout.reconfigure(errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--quick", action="store_true", help="skip the slower checks")
    args = parser.parse_args(argv)
    print(f"🔎 Vérification de l'environnement ({platform.system()} {platform.machine()})")
    check_python()
    found = check_packages()
    check_sympy(found, args.quick)
    check_repo()
    check_tests(args.quick)
    print(f"\nBilan : {results['ok']} OK, {results['warn']} avertissement(s), {results['fail']} problème(s).")
    if results["fail"]:
        print("❌ Corrige les problèmes ci-dessus (voir 00_setup/INSTALL_LOCAL.md).")
        return 1
    print("✅ Environnement prêt. Ouvre 00_setup/demo.ipynb pour la démonstration.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
