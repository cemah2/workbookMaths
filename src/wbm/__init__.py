"""wbm: utilities of workbookMaths (the maths companion of workbookIA).

>>> import wbm
>>> cfg = wbm.setup(seed=42)               # seeds, plot style, environment report
>>> wbm.check("R1.3", my_answer)            # checks an answer without revealing it
>>> wbm.check("R7.5", "2*x*exp(x**2)", kind="expr")   # an expression, compared by its values (SymPy)
>>> X, y = wbm.synth.make_blobs(200)        # synthetic data
>>> A = wbm.datasets.load_image("tasse")    # a public-domain photograph in grey levels (data/cards/)
>>> mymath = wbm.load_mymath("learner")     # your own library (or "ref" in solutions)
>>> from wbm.nbtools import checked, same, run_pytest_group   # tools of the check cells

The package is called ``wbm`` (not ``wb``) and the library ``mymath`` (not ``mylearn``), so that workbookMaths
and workbookIA can be installed in the same environment.
"""

from wbm import chapters, datasets, plot, synth
from wbm._versions import __version__
from wbm.checker import attempt, check, record
from wbm.core import Config, by_mode, ensure, environment_report, get_device, is_colab, repo_root, seed_everything, setup, timer
from wbm.impl import load_mymath
from wbm import nbtools  # noqa: E402  (after wbm.checker, which it uses)
from wbm.testing import run_pytest

__all__ = [
    "__version__",
    "setup",
    "Config",
    "by_mode",
    "ensure",
    "timer",
    "get_device",
    "is_colab",
    "repo_root",
    "seed_everything",
    "environment_report",
    "check",
    "attempt",
    "record",
    "load_mymath",
    "run_pytest",
    "chapters",
    "synth",
    "datasets",
    "plot",
    "nbtools",
]
