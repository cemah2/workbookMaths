"""Tests of your synthesis project (PS.7): python -m pytest -q test_algo.py

TODO PS.7: each test below is a skeleton, skipped with ⏳ by ``todo(...)``. Replace its body by your test (the
comments after ``todo`` give the plan), and add your own. The rules (README, « Les règles » and PS.7):

* the oracle is independent: NumPy, SciPy, SymPy, scikit-learn or PyTorch; never another function of algo.py or
  of mymath, never a formula of the article copied into the test;
* random cases: several sizes and several seeds (``pytest.mark.parametrize``, with readable ids);
* the derivatives that your code computes, against centred finite differences written here, with the step and the
  tolerance justified (M05a §5 and §7);
* the first line of each failure message says what was expected (``assert_close`` below does it);
* the mutation of mutants.py makes at least one test fail: python -m pytest -q test_algo.py --mutant=<name>.

The fixtures ``algo`` (your module) and ``mymath`` (your library) come from conftest.py: a test takes them as
arguments and calls ``algo.<function>(...)``, never ``from algo import ...`` (the mutation would not reach it).
A test stopped by a function that still raises NotImplementedError is skipped with ⏳: the code of the project is
ready when ``python -m pytest -q -rfs test_algo.py`` passes everything and skips nothing.
"""

from __future__ import annotations

import numpy as np
import pytest

SEEDS = [0, 1, 2]                      # TODO PS.7: your seeds
SIZES = [(4, 2), (30, 3), (200, 5)]    # TODO PS.7: what a size means for your algorithm (here (n, p))


def todo(what: str) -> None:
    """Skip a test skeleton that is not written yet (⏳)."""
    pytest.skip(f"⏳ à écrire (PS.7) : {what}")


def assert_close(got, expected, *, rtol: float, atol: float, what: str) -> None:
    """Compare two arrays; the first line of the failure says what was expected (the oracle's value)."""
    got = np.asarray(got, dtype=float)
    expected = np.asarray(expected, dtype=float)
    assert got.shape == expected.shape, f"{what}: expected shape {expected.shape}, got {got.shape}"
    gap = np.abs(got - expected)
    bad = gap > atol + rtol * np.abs(expected)
    if np.any(bad) or not np.all(np.isfinite(got)):
        index = np.unravel_index(int(np.argmax(np.where(np.isfinite(gap), gap, np.inf))), gap.shape)
        raise AssertionError(f"{what}: expected {float(expected[index])!r} at index {tuple(int(i) for i in index)} "
                             f"(rtol={rtol}, atol={atol}), got {float(got[index])!r}; {int(np.sum(bad))} value(s) out "
                             "of tolerance")


def test_example_function(algo):
    """Delete this test with example_function: it only shows a test skipped while a function raises NotImplementedError."""
    x = np.ones((3, 2))
    assert algo.example_function(x).shape == (3,), "expected a result of shape (n,) = (3,)"


@pytest.mark.parametrize("seed", SEEDS, ids=[f"seed={s}" for s in SEEDS])
@pytest.mark.parametrize("size", SIZES, ids=[f"n={n},p={p}" for n, p in SIZES])
def test_matches_oracle(algo, size, seed):
    """The algorithm gives the oracle's result on a random case (PS.7)."""
    todo("le résultat de l'algorithme contre l'oracle de ton cadrage, sur un cas tiré au hasard")
    rng = np.random.default_rng(seed)
    # 1. draw a case of this size (data, parameters) with rng only;
    # 2. got = algo.<your function>(...);
    # 3. expected = the oracle (a function of NumPy, SciPy, SymPy, scikit-learn or PyTorch), with the settings
    #    that make it comparable (written in the cadrage);
    # 4. assert_close(got, expected, rtol=..., atol=..., what="...")   # why this tolerance?


@pytest.mark.parametrize("seed", SEEDS, ids=[f"seed={s}" for s in SEEDS])
def test_derivative_matches_centred_differences(algo, seed):
    """A derivative computed by the code equals its centred finite differences (PS.7)."""
    todo("une dérivée calculée par ton code contre des différences finies centrées écrites ici")
    rng = np.random.default_rng(seed)
    # h = ...  # the step: why this one (M05a §7: truncation error against rounding error)?
    # for each coordinate i: (f(x + h e_i) - f(x - h e_i)) / (2 h), compared with the derivative of algo.py,
    # with a tolerance of the order of the error of the method (M05a §5).


@pytest.mark.parametrize("seed", SEEDS, ids=[f"seed={s}" for s in SEEDS])
def test_property(algo, seed):
    """A property of §4 (or an invariance, an identity, a bound) holds on a random case (PS.7)."""
    todo("une propriété démontrée en §4, vérifiée sur un cas tiré au hasard")
    rng = np.random.default_rng(seed)


def test_hand_example(algo):
    """The example computed by hand in §5 (exact values, fractions.Fraction when possible)."""
    todo("l'exemple à la main de §5 : ses données et les valeurs exactes que tu as trouvées")


def test_rejects_invalid_input(algo):
    """An invalid input raises the error announced by the docstring (PS.6)."""
    todo("une entrée invalide lève l'erreur annoncée par la docstring")
    # with pytest.raises(ValueError, match="expected"):
    #     algo.<your function>(<an input of the wrong shape, or out of the domain of §2>)
