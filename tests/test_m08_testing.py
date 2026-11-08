"""Tests of mymath.testing (chapter M08): binomial test, permutation test, intervals, Bonferroni, AIC and BIC.

Oracles: ``scipy.stats.binomtest`` (p-values and Wilson interval), ``scipy.stats.permutation_test`` with every split
(the exact p-value that the Monte Carlo one estimates), ``scipy.stats.ttest_rel`` (Student's interval),
``scipy.stats.norm.ppf`` (Wald), NumPy formulas, and the random procedure of the docstring itself (the seed fixes
the permutations). They describe the expected behaviour without showing more than the docstrings.

    pytest tests/test_m08_testing.py              # your code
    pytest tests/test_m08_testing.py --impl=ref   # the reference
"""

import ast
import inspect
import math

import numpy as np
import pytest
from scipy import stats


@pytest.fixture
def testing(mymath_module):
    return mymath_module("testing")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}"
                    + (f" ({hint})" if hint else ""))


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # a function not written yet stays ⏳
    except ValueError:
        return
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _python_float(got, what):
    assert type(got) is float, (f"expected {what} to be a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__}")


def _float_pair(got, what):
    assert isinstance(got, tuple) and len(got) == 2, (f"expected {what} to be a tuple (low, high), got "
                                                      f"{type(got).__name__} {got!r}")
    for value in got:
        _python_float(value, f"each bound of {what}")


# ---------------------------------------------------------------- no ready-made tool
ALLOWED_STATS = {"t"}          # scipy.stats.t.ppf, Student's quantile, is allowed by the module docstring


def test_testing_uses_no_ready_made_test(testing):
    """testing.py computes its tests itself: no scipy.stats tool other than the quantile t.ppf, no statsmodels."""
    try:
        tree = ast.parse(inspect.getsource(testing))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.startswith("statsmodels"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith("statsmodels"):
                found.add(node.module)
            elif node.module.startswith("scipy.stats"):
                found.update(f"scipy.stats.{alias.name}" for alias in node.names if alias.name not in ALLOWED_STATS)
        elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Attribute) and node.value.attr == "stats":
            if node.attr not in ALLOWED_STATS:
                found.add(f"scipy.stats.{node.attr}")
        elif (isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "stats"
              and node.attr not in ALLOWED_STATS):
            found.add(f"scipy.stats.{node.attr}")
    assert not found, (f"expected testing.py to use no ready-made test (only scipy.stats.t.ppf and "
                       f"statistics.NormalDist are allowed: the tests compare your results with scipy.stats), found "
                       f"{sorted(found)}")


# ---------------------------------------------------------------- binomial_test
BINOMIAL_CASES = [   # (k, n, p): none is an exercise of the chapter
    (3, 17, 0.5), (14, 20, 0.5), (0, 25, 0.5), (25, 25, 0.5), (7, 40, 0.1), (2, 9, 0.35), (120, 300, 0.37),
    (1, 1, 0.5), (11, 30, 0.6), (600, 600, 0.999),
    (1, 2, 1 / 3), (3, 4, 0.6),   # two outcomes equally likely up to rounding: the tolerance 1 + 1e-7 matters
]
ALTERNATIVES = ["two-sided", "greater", "less"]


def test_binomial_test_docstring_examples(testing):
    for kwargs, expected in [({"alternative": "greater"}, 0.0107421875), ({}, 0.021484375)]:
        got = _result(lambda kwargs=kwargs: testing.binomial_test(9, 10, **kwargs), f"{expected}",
                      f"binomial_test(9, 10, {kwargs})")
        assert got == pytest.approx(expected, rel=1e-12), (
            f"expected {expected} for binomial_test(9, 10, {kwargs}), got {got!r}")
    got = _result(lambda: testing.binomial_test(5, 10), "1.0", "binomial_test(5, 10)")
    assert got == pytest.approx(1.0, abs=1e-12), (
        f"expected 1.0 for binomial_test(5, 10) (every outcome is at most as likely as k = 5), got {got!r}")


@pytest.mark.parametrize("case", BINOMIAL_CASES, ids=[f"k{k}-n{n}-p{p}" for k, n, p in BINOMIAL_CASES])
@pytest.mark.parametrize("alternative", ALTERNATIVES)
def test_binomial_test_matches_scipy(testing, case, alternative):
    k, n, p = case
    expected = float(stats.binomtest(k, n, p, alternative=alternative).pvalue)
    got = _result(lambda: testing.binomial_test(k, n, p, alternative=alternative), f"{expected:.10g}",
                  f"k = {k}, n = {n}, p = {p}, alternative = {alternative!r}")
    hints = {"greater": "P(K ≥ k): add the probabilities of j = k, k + 1, …, n",
             "less": "P(K ≤ k): add the probabilities of j = 0, 1, …, k",
             "two-sided": "add P(K = j) over every j with P(K = j) ≤ P(K = k) × (1 + 1e-7), then cap at 1"}
    assert got == pytest.approx(expected, rel=1e-9, abs=1e-300), (
        f"expected {expected:.10g} for k = {k}, n = {n}, p = {p}, alternative = {alternative!r}, got {got!r} "
        f"({hints[alternative]})")


def test_binomial_test_returns_a_python_float_in_0_1(testing):
    got = _result(lambda: testing.binomial_test(4, 12, 0.25), "a float", "binomial_test(4, 12, 0.25)")
    _python_float(got, "binomial_test(4, 12, 0.25)")
    assert 0 < got <= 1, f"expected a p-value in ]0, 1], got {got!r}"


@pytest.mark.parametrize("case", [(10, 20, 0.5), (0, 2, 0.2)], ids=["k10-n20-p0.5", "k0-n2-p0.2"])
def test_binomial_test_two_sided_is_capped_at_one(testing, case):
    k, n, p = case
    got = _result(lambda: testing.binomial_test(k, n, p), "1.0", f"binomial_test({k}, {n}, {p})")
    assert got <= 1.0, (f"expected a p-value at most 1 for binomial_test({k}, {n}, {p}) (cap the sum at 1: rounding "
                        f"can push it just above), got {got!r}")


BINOMIAL_INVALID = {
    "k-above-n": ((8, 7, 0.5, "two-sided"), "k cannot exceed n"),
    "k-negative": ((-1, 7, 0.5, "two-sided"), "k is a number of successes"),
    "n-zero": ((0, 0, 0.5, "two-sided"), "at least one trial"),
    "p-zero": ((2, 7, 0.0, "two-sided"), "p must be strictly between 0 and 1"),
    "p-one": ((2, 7, 1.0, "two-sided"), "p must be strictly between 0 and 1"),
    "unknown-alternative": ((2, 7, 0.5, "bigger"), "alternative must be two-sided, greater or less"),
}


@pytest.mark.parametrize("name", list(BINOMIAL_INVALID))
def test_binomial_test_rejects_invalid_input(testing, name):
    (k, n, p, alternative), why = BINOMIAL_INVALID[name]
    _expect_value_error(lambda: testing.binomial_test(k, n, p, alternative=alternative),
                        f"binomial_test({k}, {n}, {p}, alternative={alternative!r})", why)


# ---------------------------------------------------------------- permutation_test
def _docstring_procedure(x, y, n_permutations, alternative, seed):
    """The p-value that the docstring describes, step by step (the same generator, used in the same order)."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    observed = x.mean() - y.mean()
    pooled = np.concatenate([x, y])
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n_permutations):
        perm = rng.permutation(pooled)
        t_perm = perm[: x.size].mean() - perm[x.size:].mean()
        if alternative == "greater":
            count += t_perm >= observed - 1e-9
        elif alternative == "less":
            count += t_perm <= observed + 1e-9
        else:
            count += abs(t_perm) >= abs(observed) - 1e-9
    return (count + 1) / (n_permutations + 1)


SAMPLES = {   # (x, y): none is an exercise of the chapter
    "shifted": ([4.1, 5.3, 6.0, 5.7, 4.9], [3.2, 4.0, 3.7, 4.4]),
    "equal-means": ([1.0, 3.0, 5.0], [2.0, 3.0, 4.0]),
    "ties": ([2.0, 2.0, 3.0, 3.0], [2.0, 3.0, 3.0, 4.0, 4.0]),
    "one-value": ([7.5], [1.0, 2.0, 3.5, 2.5]),
    "negative": ([-0.4, -1.2, 0.3, -0.8, -0.1, -0.6], [0.5, 0.2, -0.3, 0.9, 0.4]),
}


def test_permutation_test_docstring_examples(testing):
    got = _result(lambda: testing.permutation_test([1, 2, 3], [3, 2, 1]), "1.0", "permutation_test([1, 2, 3], [3, 2, 1])")
    assert got == pytest.approx(1.0, abs=1e-12), (
        f"expected 1.0 for permutation_test([1, 2, 3], [3, 2, 1]) (t = 0: every permutation is at least as extreme), "
        f"got {got!r}")
    got = _result(lambda: testing.permutation_test([10, 11, 12, 13], [1, 2, 3, 4], alternative="greater"), "0.0146",
                  "the second example of the docstring")
    assert got == pytest.approx(0.0146, abs=1e-12), (
        f"expected 0.0146 for permutation_test([10, 11, 12, 13], [1, 2, 3, 4], alternative='greater'), got {got!r} "
        f"(rng = np.random.default_rng(0), one rng.permutation(pooled) per draw, then (C + 1) / (n_permutations + 1))")


@pytest.mark.parametrize("name", list(SAMPLES))
@pytest.mark.parametrize("alternative", ALTERNATIVES)
def test_permutation_test_follows_the_docstring_procedure(testing, name, alternative):
    x, y = SAMPLES[name]
    expected = float(_docstring_procedure(x, y, 999, alternative, 21))
    got = _result(lambda: testing.permutation_test(x, y, n_permutations=999, alternative=alternative, seed=21),
                  f"{expected:.10g}", f"{name}, n_permutations = 999, alternative = {alternative!r}, seed = 21")
    assert got == pytest.approx(expected, abs=1e-12), (
        f"expected {expected:.10g} for {name}, n_permutations = 999, alternative = {alternative!r}, seed = 21, got "
        f"{got!r} (one generator default_rng(seed), pooled = x then y, rng.permutation(pooled) at each draw, the "
        f"tolerance 1e-9 of the docstring, then (C + 1) / (n_permutations + 1))")


@pytest.mark.parametrize("name", ["shifted", "ties", "negative"])
@pytest.mark.parametrize("alternative", ["greater", "less"])
def test_permutation_test_estimates_the_exact_p_value(testing, name, alternative):
    """With many permutations, the p-value is close to the exact one of scipy (every split, each counted once)."""
    x, y = SAMPLES[name]
    exact = float(stats.permutation_test((x, y), lambda a, b: np.mean(a) - np.mean(b), permutation_type="independent",
                                         n_resamples=np.inf, alternative=alternative).pvalue)
    got = _result(lambda: testing.permutation_test(x, y, n_permutations=4000, alternative=alternative, seed=5),
                  f"about {exact:.4f}", f"{name}, alternative = {alternative!r}")
    tolerance = 5 * math.sqrt(exact * (1 - exact) / 4000) + 2 / 4000
    assert abs(got - exact) <= tolerance, (
        f"expected about {exact:.4f} (the exact p-value, ± {tolerance:.4f}) for {name}, alternative = "
        f"{alternative!r}, got {got!r}")


def test_permutation_test_never_returns_zero(testing):
    got = _result(lambda: testing.permutation_test([20, 21, 22, 23, 24], [1, 2, 3, 4, 5], n_permutations=49,
                                                   alternative="greater"), "at least 1/50",
                  "two separated groups and 49 permutations")
    _python_float(got, "permutation_test(...)")
    assert got >= 1 / 50 - 1e-12, (
        f"expected a p-value at least 1/50 = 0.02 with 49 permutations (the observed split counts as one), got {got!r}")


def test_permutation_test_depends_only_on_the_seed(testing):
    x, y = SAMPLES["shifted"]
    first = _result(lambda: testing.permutation_test(x, y, n_permutations=300, seed=9), "a float", "seed = 9")
    second = _result(lambda: testing.permutation_test(x, y, n_permutations=300, seed=9), "a float", "seed = 9")
    assert first == second, (f"expected the same p-value for two calls with seed = 9, got {first!r} and {second!r} "
                             f"(create the generator inside the function: rng = np.random.default_rng(seed))")


PERMUTATION_INVALID = {
    "x-empty": (([], [1.0, 2.0], 99, "two-sided"), "a sample needs at least one value"),
    "y-empty": (([1.0, 2.0], [], 99, "two-sided"), "a sample needs at least one value"),
    "no-permutation": (([1.0, 2.0], [3.0], 0, "two-sided"), "n_permutations must be at least 1"),
    "unknown-alternative": (([1.0, 2.0], [3.0], 99, "larger"), "alternative must be two-sided, greater or less"),
}


@pytest.mark.parametrize("name", list(PERMUTATION_INVALID))
def test_permutation_test_rejects_invalid_input(testing, name):
    (x, y, n_perm, alternative), why = PERMUTATION_INVALID[name]
    _expect_value_error(lambda: testing.permutation_test(x, y, n_permutations=n_perm, alternative=alternative),
                        f"permutation_test({x}, {y}, n_permutations={n_perm}, alternative={alternative!r})", why)


# ---------------------------------------------------------------- proportion_ci
PROPORTION_CASES = [(0, 12), (1, 12), (6, 13), (37, 50), (50, 50), (149, 400), (3, 1000)]
LEVELS = [0.9, 0.95, 0.99]


def test_proportion_ci_docstring_examples(testing):
    got = _result(lambda: testing.proportion_ci(0, 10, method="wald"), "(0.0, 0.0)", "proportion_ci(0, 10, 'wald')")
    assert got == pytest.approx((0.0, 0.0), abs=1e-12), (
        f"expected (0.0, 0.0) for proportion_ci(0, 10, method='wald') (p̂ = 0 gives a zero half-width), got {got!r}")
    for (k, n), expected in [((0, 10), (0.0, 0.2775)), ((8, 40), (0.105, 0.3476))]:
        got = _result(lambda k=k, n=n: testing.proportion_ci(k, n), f"{expected}", f"proportion_ci({k}, {n})")
        assert [round(v, 4) for v in got] == list(expected), (
            f"expected {list(expected)} for proportion_ci({k}, {n}) rounded to 4 decimals, got {got!r}")


@pytest.mark.parametrize("case", PROPORTION_CASES, ids=[f"k{k}-n{n}" for k, n in PROPORTION_CASES])
@pytest.mark.parametrize("level", LEVELS)
def test_proportion_ci_wilson_matches_scipy(testing, case, level):
    k, n = case
    ci = stats.binomtest(k, n).proportion_ci(confidence_level=level, method="wilson")
    expected = (float(ci.low), float(ci.high))
    got = _result(lambda: testing.proportion_ci(k, n, level=level), f"({expected[0]:.6f}, {expected[1]:.6f})",
                  f"k = {k}, n = {n}, level = {level}")
    _float_pair(got, f"proportion_ci({k}, {n}, level={level})")
    assert got == pytest.approx(expected, abs=1e-9), (
        f"expected ({expected[0]:.6f}, {expected[1]:.6f}) for the Wilson interval with k = {k}, n = {n}, level = "
        f"{level}, got {got!r} (z is the quantile of order (1 + level) / 2, and the whole interval is divided by "
        f"1 + z²/n)")


@pytest.mark.parametrize("case", PROPORTION_CASES, ids=[f"k{k}-n{n}" for k, n in PROPORTION_CASES])
@pytest.mark.parametrize("level", LEVELS)
def test_proportion_ci_wald_matches_the_formula(testing, case, level):
    k, n = case
    z = float(stats.norm.ppf((1 + level) / 2))
    p_hat = k / n
    half = z * math.sqrt(p_hat * (1 - p_hat) / n)
    expected = (max(0.0, p_hat - half), min(1.0, p_hat + half))
    got = _result(lambda: testing.proportion_ci(k, n, level=level, method="wald"),
                  f"({expected[0]:.6f}, {expected[1]:.6f})", f"k = {k}, n = {n}, level = {level}, method = 'wald'")
    _float_pair(got, f"proportion_ci({k}, {n}, level={level}, method='wald')")
    assert got == pytest.approx(expected, abs=1e-9), (
        f"expected ({expected[0]:.6f}, {expected[1]:.6f}) for the Wald interval with k = {k}, n = {n}, level = "
        f"{level}, got {got!r} (p̂ ± z √(p̂(1 − p̂)/n), clipped to [0, 1])")


@pytest.mark.parametrize("case", PROPORTION_CASES, ids=[f"k{k}-n{n}" for k, n in PROPORTION_CASES])
def test_proportion_ci_wilson_contains_p_hat_inside_0_1(testing, case):
    k, n = case
    got = _result(lambda: testing.proportion_ci(k, n), "an interval", f"k = {k}, n = {n}")
    low, high = got
    assert 0 <= low <= k / n <= high <= 1, (
        f"expected 0 ≤ low ≤ p̂ = {k / n:.4f} ≤ high ≤ 1 for the Wilson interval with k = {k}, n = {n}, got {got!r} "
        f"(clip each bound to [0, 1] with min and max: rounding can push a bound just outside, such as "
        f"1.0000000000000002 for k = n)")


PROPORTION_INVALID = {
    "k-above-n": ((11, 10, 0.95, "wilson"), "k cannot exceed n"),
    "n-zero": ((0, 0, 0.95, "wilson"), "at least one trial"),
    "level-one": ((3, 10, 1.0, "wilson"), "the level must be strictly between 0 and 1"),
    "level-zero": ((3, 10, 0.0, "wilson"), "the level must be strictly between 0 and 1"),
    "unknown-method": ((3, 10, 0.95, "agresti"), "method must be wilson or wald"),
}


@pytest.mark.parametrize("name", list(PROPORTION_INVALID))
def test_proportion_ci_rejects_invalid_input(testing, name):
    (k, n, level, method), why = PROPORTION_INVALID[name]
    _expect_value_error(lambda: testing.proportion_ci(k, n, level=level, method=method),
                        f"proportion_ci({k}, {n}, level={level}, method={method!r})", why)


# ---------------------------------------------------------------- paired_difference_ci
PAIRS = {   # (a, b): none is an exercise of the chapter
    "small": ([3.1, 2.4, 4.0], [2.2, 2.5, 3.1]),
    "eight": ([10.2, 9.8, 11.5, 10.9, 12.1, 9.4, 10.7, 11.0], [9.6, 9.9, 10.8, 10.1, 11.2, 9.0, 10.5, 10.1]),
    "negative": ([-1.0, 0.5, -0.2, 0.8, -0.6], [0.4, 0.9, 0.3, 1.2, 0.1]),
    "two-pairs": ([5.0, 7.0], [4.0, 4.5]),
}


def test_paired_difference_ci_docstring_example(testing):
    got = _result(lambda: testing.paired_difference_ci([5, 7, 6, 8], [4, 5, 5, 6]), "[0.5813, 2.4187]",
                  "the docstring example")
    assert [round(v, 4) for v in got] == [0.5813, 2.4187], (
        f"expected [0.5813, 2.4187] (rounded) for paired_difference_ci([5, 7, 6, 8], [4, 5, 5, 6]), got {got!r}")


@pytest.mark.parametrize("name", list(PAIRS))
@pytest.mark.parametrize("level", LEVELS)
def test_paired_difference_ci_matches_scipy(testing, name, level):
    a, b = PAIRS[name]
    ci = stats.ttest_rel(a, b).confidence_interval(confidence_level=level)
    expected = (float(ci.low), float(ci.high))
    got = _result(lambda: testing.paired_difference_ci(a, b, level=level), f"({expected[0]:.6f}, {expected[1]:.6f})",
                  f"{name}, level = {level}")
    _float_pair(got, f"paired_difference_ci({name}, level={level})")
    assert got == pytest.approx(expected, abs=1e-9), (
        f"expected ({expected[0]:.6f}, {expected[1]:.6f}) for {name} at level {level}, got {got!r} (the mean of the "
        f"differences ± t s_d / √n, with s_d computed with ddof=1 and t = scipy.stats.t.ppf((1 + level) / 2, n − 1))")


PAIRED_INVALID = {
    "lengths-differ": (([1.0, 2.0, 3.0], [1.0, 2.0], 0.95), "paired measurements have the same length"),
    "one-pair": (([1.0], [2.0], 0.95), "ddof=1 needs at least two pairs"),
    "level-out": (([1.0, 2.0, 3.0], [1.5, 2.0, 2.0], 1.5), "the level must be strictly between 0 and 1"),
}


@pytest.mark.parametrize("name", list(PAIRED_INVALID))
def test_paired_difference_ci_rejects_invalid_input(testing, name):
    (a, b, level), why = PAIRED_INVALID[name]
    _expect_value_error(lambda: testing.paired_difference_ci(a, b, level=level),
                        f"paired_difference_ci({a}, {b}, level={level})", why)


# ---------------------------------------------------------------- bonferroni
def test_bonferroni_docstring_example(testing):
    got = _result(lambda: testing.bonferroni([0.01, 0.04, 0.3]), "array([0.03, 0.12, 0.9])", "the docstring example")
    assert isinstance(got, np.ndarray), (f"expected a numpy.ndarray (np.array(...)), got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert np.allclose(got, [0.03, 0.12, 0.9], atol=1e-12), f"expected [0.03, 0.12, 0.9], got {got!r}"


@pytest.mark.parametrize("p_values", [[0.2], [0.001, 0.02, 0.5, 0.0], [0.07, 0.3, 0.45, 0.012, 1.0, 0.026],
                                      list(np.linspace(0.001, 0.2, 40))], ids=["one", "four", "six", "forty"])
def test_bonferroni_matches_the_formula(testing, p_values):
    expected = np.minimum(1.0, np.array(p_values) * len(p_values))
    got = _result(lambda: testing.bonferroni(p_values), f"{np.round(expected, 6).tolist()}",
                  f"{len(p_values)} p-values")
    got = np.asarray(got, dtype=float)
    assert got.shape == expected.shape, f"expected {expected.size} adjusted p-values, got shape {got.shape}"
    assert np.allclose(got, expected, atol=1e-12), (
        f"expected {np.round(expected, 6).tolist()} for {len(p_values)} p-values, got {np.round(got, 6).tolist()} "
        f"(multiply by the number of tests m, then cap at 1, in the same order)")


BONFERRONI_INVALID = {
    "empty": ([], "at least one p-value"),
    "above-one": ([0.2, 1.3], "a p-value is at most 1"),
    "negative": ([-0.1, 0.4], "a p-value is at least 0"),
}


@pytest.mark.parametrize("name", list(BONFERRONI_INVALID))
def test_bonferroni_rejects_invalid_input(testing, name):
    p_values, why = BONFERRONI_INVALID[name]
    _expect_value_error(lambda: testing.bonferroni(p_values), f"bonferroni({p_values})", why)


# ---------------------------------------------------------------- aic_bic
def test_aic_bic_docstring_example(testing):
    got = _result(lambda: testing.aic_bic(-100.0, 3, 50), "(206.0, 211.736…)", "aic_bic(-100.0, 3, 50)")
    _float_pair(got, "aic_bic(-100.0, 3, 50)")
    assert got[0] == pytest.approx(206.0, abs=1e-9) and round(got[1], 3) == 211.736, (
        f"expected (206.0, 211.736…) for aic_bic(-100.0, 3, 50), got {got!r}")


@pytest.mark.parametrize("args", [(-12.5, 1, 30), (-842.31, 6, 1200), (3.2, 2, 8), (-0.01, 15, 1)],
                         ids=["one-parameter", "large-n", "positive-log-likelihood", "n-one"])
def test_aic_bic_matches_the_formulas(testing, args):
    log_l, k, n = args
    expected = (2 * k - 2 * log_l, k * math.log(n) - 2 * log_l)
    got = _result(lambda: testing.aic_bic(log_l, k, n), f"({expected[0]:.6f}, {expected[1]:.6f})",
                  f"ln L = {log_l}, k = {k}, n = {n}")
    _float_pair(got, f"aic_bic({log_l}, {k}, {n})")
    assert got == pytest.approx(expected, rel=1e-12, abs=1e-12), (
        f"expected ({expected[0]:.6f}, {expected[1]:.6f}) for ln L = {log_l}, k = {k}, n = {n}, got {got!r} "
        f"(AIC = 2k − 2 ln L, BIC = k ln n − 2 ln L, with the natural logarithm)")


@pytest.mark.parametrize("args", [(-10.0, 0, 20), (-10.0, 2, 0)], ids=["k-zero", "n-zero"])
def test_aic_bic_rejects_invalid_input(testing, args):
    log_l, k, n = args
    _expect_value_error(lambda: testing.aic_bic(log_l, k, n), f"aic_bic({log_l}, {k}, {n})",
                        "k and n must be at least 1")
