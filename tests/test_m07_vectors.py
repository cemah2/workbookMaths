"""Tests of mymath.vectors (chapter M07): p-norms, cosine similarity, projection, centroid, hyperplanes.

Oracles: ``numpy.linalg.norm``, ``scipy.spatial.distance`` and NumPy formulas (``np.average``, ``X @ w + b``), plus
properties (a projection is idempotent and leaves an orthogonal residual, the centroid minimises the sum of squared
distances). They describe the expected behaviour without showing the solution.

    pytest tests/test_m07_vectors.py              # your code
    pytest tests/test_m07_vectors.py --impl=ref   # the reference
"""

import ast
import inspect
import math

import numpy as np
import pytest
from scipy.spatial import distance as spd


@pytest.fixture
def vectors(mymath_module):
    return mymath_module("vectors")


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


def _array(got, what, shape):
    assert isinstance(got, np.ndarray), (f"expected {what} to be a numpy.ndarray (np.array(...)), got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert got.shape == shape, f"expected {what} to have the shape {shape}, got {got.shape}"


# ---------------------------------------------------------------- data
VECTORS = {   # no answer of an exercise, no example of the fiche
    "2d": [2.5, -6.0],
    "3d": [1.2, -0.7, 3.1],
    "5d": [-2.0, 0.5, 4.25, -1.5, 0.0],
    "big": [3e5, -1.2e6, 7.5e5],
    "tiny": [2e-9, -5e-10, 1e-9, 0.0],
}
VECTOR_IDS = list(VECTORS)
P_VALUES = [1, 1.5, 2, 3, 7.5, math.inf]


# ---------------------------------------------------------------- no ready-made tool
def test_vectors_uses_no_ready_made_tool(vectors):
    """vectors.py computes its norms and distances itself: neither numpy.linalg.norm nor scipy.spatial."""
    try:
        tree = ast.parse(inspect.getsource(vectors))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.startswith("scipy.spatial"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith("scipy.spatial") or (node.module == "scipy"
                                                           and any(a.name == "spatial" for a in node.names)):
                found.add("scipy.spatial")
            elif node.module.endswith("linalg") and any(alias.name == "norm" for alias in node.names):
                found.add("numpy.linalg.norm")
        elif isinstance(node, ast.Attribute):
            if node.attr == "norm" and isinstance(node.value, ast.Attribute) and node.value.attr == "linalg":
                found.add("numpy.linalg.norm")
            elif node.attr == "spatial":
                found.add("scipy.spatial")
    assert not found, (f"expected vectors.py to use neither numpy.linalg.norm nor scipy.spatial (the tests compare "
                       f"your results with them), found {sorted(found)}: write the sums with NumPy")


# ---------------------------------------------------------------- norm_p
def test_norm_p_docstring_examples(vectors):
    for p, expected in [(2, 5.0), (1, 7.0), (math.inf, 4.0)]:
        got = _result(lambda p=p: vectors.norm_p([3, -4], p=p), f"{expected}", f"[3, -4] with p = {p}")
        assert got == pytest.approx(expected, abs=1e-12), f"expected {expected} for norm_p([3, -4], p={p}), got {got!r}"


@pytest.mark.parametrize("name", VECTOR_IDS)
@pytest.mark.parametrize("p", P_VALUES, ids=[f"p{p}" for p in P_VALUES])
def test_norm_p_matches_numpy(vectors, name, p):
    x = VECTORS[name]
    expected = float(np.linalg.norm(np.array(x), ord=p))
    got = _result(lambda: vectors.norm_p(x, p=p), f"{expected:.10g}", f"{name} with p = {p}")
    hint = ("p = inf: the largest absolute value" if math.isinf(p) else
            "absolute values first, then the power p, the sum, and the power 1/p")
    assert got == pytest.approx(expected, rel=1e-12, abs=1e-300), (
        f"expected {expected:.12g} for the {p}-norm of {x} (numpy.linalg.norm), got {got!r}: {hint}")


def test_norm_p_default_is_euclidean(vectors):
    x = VECTORS["3d"]
    expected = float(np.linalg.norm(x))
    got = _result(lambda: vectors.norm_p(x), f"{expected:.10g}")
    assert got == pytest.approx(expected, rel=1e-12), f"expected the Euclidean norm {expected:.12g} by default, got {got!r}"


def test_norm_p_returns_a_python_float(vectors):
    got = _result(lambda: vectors.norm_p(np.array([1.5, 2.0]), p=3), "a float")
    _python_float(got, "norm_p(np.array([1.5, 2.0]), p=3)")
    got = _result(lambda: vectors.norm_p(np.array([1.5, 2.0]), p=math.inf), "a float")
    _python_float(got, "norm_p(np.array([1.5, 2.0]), p=inf)")


def test_norm_p_of_the_zero_vector_is_zero(vectors):
    for p in (1, 2, 4, math.inf):
        got = _result(lambda p=p: vectors.norm_p([0.0, 0.0, 0.0], p=p), "0.0", f"p = {p}")
        assert got == 0.0, f"expected 0.0 for the zero vector with p = {p}, got {got!r}"


def test_norm_p_decreases_with_p(vectors):
    x = VECTORS["5d"]
    values = [_result(lambda p=p: vectors.norm_p(x, p=p), "a number", f"p = {p}") for p in P_VALUES]
    assert all(a >= b - 1e-12 for a, b in zip(values, values[1:])), (
        f"expected ‖x‖_p to decrease when p grows (p = {P_VALUES}), got {values}")


@pytest.mark.parametrize("x, p, why", [([], 2, "an empty vector"), ([1.0, 2.0], 0.5, "p < 1 is not a norm"),
                                       ([1.0, 2.0], 0, "p = 0"), ([1.0, 2.0], float("nan"), "p = nan"),
                                       ([[1.0, 2.0], [3.0, 4.0]], 2, "a 2-D table is not a vector")],
                         ids=["empty", "p-half", "p-zero", "p-nan", "2-D"])
def test_norm_p_refuses_bad_input(vectors, x, p, why):
    _expect_value_error(lambda: vectors.norm_p(x, p=p), f"norm_p({x!r}, p={p!r})", why)


# ---------------------------------------------------------------- cosine_similarity
PAIRS = [([1.5, -2.0, 0.5], [0.4, 1.1, -3.0]), ([2.0, 7.0], [-1.0, 3.5]), ([0.3, 0.1, 0.0, 2.2], [1.0, 1.0, 1.0, 1.0]),
         ([4e-7, 1e-7], [3e5, 2e5])]


def test_cosine_similarity_docstring_examples(vectors):
    for u, v, expected in [([1, 0], [1, 1], 1 / math.sqrt(2)), ([1, 2, 2], [-2, -4, -4], -1.0),
                           ([1, 0, 0], [0, 5, 0], 0.0)]:
        got = _result(lambda u=u, v=v: vectors.cosine_similarity(u, v), f"{expected:.6g}", f"{u}, {v}")
        assert got == pytest.approx(expected, abs=1e-12), f"expected {expected:.12g} for {u} and {v}, got {got!r}"


@pytest.mark.parametrize("u, v", PAIRS, ids=["3d", "2d", "4d", "scales"])
def test_cosine_similarity_matches_scipy(vectors, u, v):
    expected = 1.0 - float(spd.cosine(u, v))
    got = _result(lambda: vectors.cosine_similarity(u, v), f"{expected:.10g}", f"{u}, {v}")
    assert got == pytest.approx(expected, abs=1e-12), (
        f"expected {expected:.12g} for {u} and {v} (1 − scipy.spatial.distance.cosine), got {got!r}: the dot product "
        f"divided by the product of the two Euclidean norms")


def test_cosine_similarity_ignores_positive_scaling(vectors):
    u, v = [1.5, -2.0, 0.5], [0.4, 1.1, -3.0]
    a = _result(lambda: vectors.cosine_similarity(u, v), "a number")
    b = _result(lambda: vectors.cosine_similarity([7 * t for t in u], [0.25 * t for t in v]), "a number")
    assert b == pytest.approx(a, abs=1e-12), f"expected the same cosine after multiplying u by 7 and v by 0.25, got {a} and {b}"


def test_cosine_similarity_stays_in_minus_one_one(vectors):
    for u in ([0.1, 0.2, 0.3], [1e8, 3.0, 1e-8], [0.7] * 9):
        got = _result(lambda u=u: vectors.cosine_similarity(u, u), "1.0", f"a vector with itself, {u}")
        assert -1.0 <= got <= 1.0, (f"expected a value between -1 and 1 for {u} with itself, got {got!r}: rounding can "
                                    f"give 1.0000000000000002, np.clip brings it back")
        assert got == pytest.approx(1.0, abs=1e-12), f"expected 1.0 for a vector with itself, got {got!r}"


def test_cosine_similarity_returns_a_python_float(vectors):
    got = _result(lambda: vectors.cosine_similarity(np.array([1.0, 2.0]), np.array([3.0, -1.0])), "a float")
    _python_float(got, "cosine_similarity(np.array([1.0, 2.0]), np.array([3.0, -1.0]))")


@pytest.mark.parametrize("u, v, why", [([0.0, 0.0], [1.0, 2.0], "the first vector is zero"),
                                       ([1.0, 2.0], [0.0, 0.0], "the second vector is zero"),
                                       ([1.0, 2.0], [1.0, 2.0, 3.0], "different lengths"),
                                       ([], [], "empty vectors")],
                         ids=["zero-u", "zero-v", "lengths", "empty"])
def test_cosine_similarity_refuses_bad_input(vectors, u, v, why):
    _expect_value_error(lambda: vectors.cosine_similarity(u, v), f"cosine_similarity({u!r}, {v!r})", why)


# ---------------------------------------------------------------- project_onto_line
PROJECTIONS = [([2.0, -1.0, 4.0], [1.0, 3.0, -2.0]), ([5.5, 0.5], [0.0, 2.0]), ([1.0, 1.0, 1.0, 1.0], [2.0, 0.0, -1.0, 3.0])]


@pytest.mark.parametrize("x, u", PROJECTIONS, ids=["3d", "axis", "4d"])
def test_project_onto_line_matches_the_formula(vectors, x, u):
    xa, ua = np.array(x), np.array(u)
    expected = (xa @ ua) / (ua @ ua) * ua
    got = _result(lambda: vectors.project_onto_line(x, u), f"{expected.tolist()}", f"x = {x}, u = {u}")
    _array(got, f"project_onto_line({x}, {u})", expected.shape)
    np.testing.assert_allclose(got, expected, rtol=1e-12, atol=1e-12, err_msg=(
        f"expected {expected.tolist()} for the projection of {x} on the line directed by {u}: (x · u / u · u) u"))


def test_project_onto_line_leaves_an_orthogonal_residual(vectors):
    x, u = [2.0, -1.0, 4.0], [1.0, 3.0, -2.0]
    got = _result(lambda: vectors.project_onto_line(x, u), "a vector")
    residual = np.array(x) - np.asarray(got, dtype=float)
    assert abs(residual @ np.array(u)) < 1e-12, (
        f"expected x − proj(x) to be orthogonal to u (dot product 0), got {residual @ np.array(u)!r}")


def test_project_onto_line_is_idempotent_and_ignores_the_length_of_u(vectors):
    x, u = [2.0, -1.0, 4.0], [1.0, 3.0, -2.0]
    once = np.asarray(_result(lambda: vectors.project_onto_line(x, u), "a vector"), dtype=float)
    twice = np.asarray(_result(lambda: vectors.project_onto_line(once, u), "a vector"), dtype=float)
    longer = np.asarray(_result(lambda: vectors.project_onto_line(x, [-5.0, -15.0, 10.0]), "a vector"), dtype=float)
    np.testing.assert_allclose(twice, once, atol=1e-12, err_msg="expected projecting a projection to change nothing")
    np.testing.assert_allclose(longer, once, atol=1e-12, err_msg=(
        "expected the same projection with u multiplied by -5: the line depends on the direction of u only"))


def test_project_onto_line_does_not_modify_its_arguments(vectors):
    x, u = np.array([2.0, -1.0, 4.0]), np.array([1.0, 3.0, -2.0])
    _result(lambda: vectors.project_onto_line(x, u), "a vector")
    assert x.tolist() == [2.0, -1.0, 4.0] and u.tolist() == [1.0, 3.0, -2.0], (
        f"expected x and u to stay unchanged, got x = {x.tolist()}, u = {u.tolist()}")


@pytest.mark.parametrize("x, u, why", [([1.0, 2.0], [0.0, 0.0], "u is zero"),
                                       ([1.0, 2.0, 3.0], [1.0, 2.0], "different lengths")],
                         ids=["zero-u", "lengths"])
def test_project_onto_line_refuses_bad_input(vectors, x, u, why):
    _expect_value_error(lambda: vectors.project_onto_line(x, u), f"project_onto_line({x!r}, {u!r})", why)


# ---------------------------------------------------------------- centroid
POINTS = [[1.5, -2.0, 0.5], [3.0, 1.0, -1.0], [-0.5, 4.0, 2.5], [2.0, 0.0, 0.0]]
WEIGHTS = [0.5, 2.0, 1.5, 0.0]


def test_centroid_docstring_examples(vectors):
    got = _result(lambda: vectors.centroid([[0, 0], [2, 0], [1, 3]]), "[1.0, 1.0]")
    np.testing.assert_allclose(got, [1.0, 1.0], atol=1e-12, err_msg="expected [1.0, 1.0] (docstring)")
    got = _result(lambda: vectors.centroid([[0, 0], [4, 0]], weights=[3, 1]), "[1.0, 0.0]")
    np.testing.assert_allclose(got, [1.0, 0.0], atol=1e-12, err_msg="expected [1.0, 0.0] (docstring)")


def test_centroid_matches_numpy(vectors):
    expected = np.mean(POINTS, axis=0)
    got = _result(lambda: vectors.centroid(POINTS), f"{expected.tolist()}")
    _array(got, "centroid(points)", (3,))
    np.testing.assert_allclose(got, expected, rtol=1e-12, err_msg=(
        f"expected the mean of the rows, {expected.tolist()} (np.mean(points, axis=0))"))


def test_centroid_with_weights_matches_numpy(vectors):
    expected = np.average(POINTS, axis=0, weights=WEIGHTS)
    got = _result(lambda: vectors.centroid(POINTS, weights=WEIGHTS), f"{expected.tolist()}")
    _array(got, "centroid(points, weights)", (3,))
    np.testing.assert_allclose(got, expected, rtol=1e-12, err_msg=(
        f"expected {expected.tolist()} (np.average(points, axis=0, weights=weights)): Σ w_i x_i / Σ w_i"))


def test_centroid_of_one_point_is_that_point(vectors):
    got = _result(lambda: vectors.centroid([[2.5, -1.0]]), "[2.5, -1.0]")
    np.testing.assert_allclose(got, [2.5, -1.0], err_msg="expected the point itself for a single point")


@pytest.mark.parametrize("points, weights, why", [
    ([], None, "no point"), ([1.0, 2.0], None, "a 1-D list is one vector, not a set of points"),
    (POINTS, [1.0, 2.0], "one weight per point"), (POINTS, [1.0, -1.0, 1.0, 1.0], "a negative weight"),
    (POINTS, [0.0, 0.0, 0.0, 0.0], "weights of sum 0")],
    ids=["empty", "1-D", "length", "negative", "sum-0"])
def test_centroid_refuses_bad_input(vectors, points, weights, why):
    _expect_value_error(lambda: vectors.centroid(points, weights=weights), f"centroid({points!r}, weights={weights!r})",
                        why)


# ---------------------------------------------------------------- sum_sq_distances_to
def test_sum_sq_distances_to_docstring_examples(vectors):
    for c, expected in [([1, 1], 8.0), ([0, 0], 14.0)]:
        got = _result(lambda c=c: vectors.sum_sq_distances_to([[0, 0], [2, 0], [1, 3]], c), f"{expected}", f"c = {c}")
        assert got == pytest.approx(expected, abs=1e-12), f"expected {expected} for c = {c} (docstring), got {got!r}"


@pytest.mark.parametrize("c", [[0.0, 0.0, 0.0], [1.25, 0.75, 0.5], [-3.0, 2.0, 1.0]], ids=["origin", "centroid", "far"])
def test_sum_sq_distances_to_matches_scipy(vectors, c):
    expected = float(spd.cdist(POINTS, [c], "sqeuclidean").sum())
    got = _result(lambda: vectors.sum_sq_distances_to(POINTS, c), f"{expected:.10g}", f"c = {c}")
    assert got == pytest.approx(expected, rel=1e-12), (
        f"expected {expected:.12g} for c = {c} (scipy.spatial.distance.cdist, squared Euclidean), got {got!r}: square "
        f"every coordinate of x_i − c, without square root")
    _python_float(got, "sum_sq_distances_to(points, c)")


def test_sum_sq_distances_to_is_smallest_at_the_centroid(vectors):
    center = np.mean(POINTS, axis=0)
    at_center = _result(lambda: vectors.sum_sq_distances_to(POINTS, center), "a number")
    rng = np.random.default_rng(7)
    for shift in rng.normal(size=(5, 3)):
        other = _result(lambda s=shift: vectors.sum_sq_distances_to(POINTS, center + 0.3 * s), "a number")
        assert other > at_center, f"expected the sum to be smallest at the centroid, got {other} < {at_center}"


@pytest.mark.parametrize("points, c, why", [(POINTS, [1.0, 2.0], "c has 2 coordinates, the points 3"),
                                            ([], [1.0], "no point")], ids=["shape", "empty"])
def test_sum_sq_distances_to_refuses_bad_input(vectors, points, c, why):
    _expect_value_error(lambda: vectors.sum_sq_distances_to(points, c), f"sum_sq_distances_to({points!r}, {c!r})", why)


# ---------------------------------------------------------------- side_of_hyperplane
W, B = [1.5, -2.0, 0.5], -0.25
GRID = [[1.0, 0.5, 0.5], [0.0, 0.0, 0.0], [2.0, 1.0, -1.0], [0.5, 0.25, 0.5], [-1.0, 3.0, 2.0]]


def test_side_of_hyperplane_docstring_examples(vectors):
    got = _result(lambda: vectors.side_of_hyperplane([3, 0], [1, 1], -2), "1")
    assert got == 1, f"expected 1 for the point (3, 0) and the line x + y − 2 = 0, got {got!r}"
    got = _result(lambda: vectors.side_of_hyperplane([[1, 1], [0, 0], [3, 0]], [1, 1], -2), "[0, -1, 1]")
    np.testing.assert_array_equal(got, [0, -1, 1], err_msg="expected [0, -1, 1] (docstring)")


def test_side_of_hyperplane_matches_numpy_on_several_points(vectors):
    expected = np.sign(np.array(GRID) @ np.array(W) + B).astype(int)
    got = _result(lambda: vectors.side_of_hyperplane(GRID, W, B), f"{expected.tolist()}")
    _array(got, "side_of_hyperplane(points, w, b)", (len(GRID),))
    assert np.issubdtype(got.dtype, np.integer), f"expected an array of ints (astype(int)), got dtype {got.dtype}"
    np.testing.assert_array_equal(got, expected, err_msg=(
        f"expected {expected.tolist()}: the sign of w · x + b for each row (0 exactly on the hyperplane)"))


def test_side_of_hyperplane_returns_a_python_int_for_one_point(vectors):
    for point in GRID:
        expected = int(np.sign(np.array(point) @ np.array(W) + B))
        got = _result(lambda point=point: vectors.side_of_hyperplane(point, W, B), f"{expected}", f"the point {point}")
        assert type(got) is int, (f"expected a Python int for one point (int(...)), got "
                                  f"{type(got).__module__}.{type(got).__name__}")
        assert got == expected, f"expected {expected} for the point {point}, got {got!r}"


@pytest.mark.parametrize("x, w, why", [([1.0, 2.0], [0.0, 0.0], "w is zero"),
                                       ([1.0, 2.0, 3.0], [1.0, 1.0], "3 coordinates, w has 2"),
                                       ([[1.0, 2.0, 3.0]], [1.0, 1.0], "rows of 3 coordinates, w has 2")],
                         ids=["zero-w", "point-length", "rows-length"])
def test_side_of_hyperplane_refuses_bad_input(vectors, x, w, why):
    _expect_value_error(lambda: vectors.side_of_hyperplane(x, w, 1.0), f"side_of_hyperplane({x!r}, {w!r}, 1.0)", why)


# ---------------------------------------------------------------- distance_to_hyperplane
def test_distance_to_hyperplane_docstring_examples(vectors):
    got = _result(lambda: vectors.distance_to_hyperplane([3, 4], [3, 4], 0), "5.0")
    assert got == pytest.approx(5.0, abs=1e-12), f"expected 5.0 (docstring), got {got!r}"
    got = _result(lambda: vectors.distance_to_hyperplane([0, 0], [1, 1], -2, signed=True), "-1.4142…")
    assert got == pytest.approx(-math.sqrt(2), abs=1e-12), f"expected -√2 ≈ -1.4142 (docstring), got {got!r}"


def test_distance_to_hyperplane_matches_numpy(vectors):
    scores = np.array(GRID) @ np.array(W) + B
    expected = np.abs(scores) / np.linalg.norm(W)
    got = _result(lambda: vectors.distance_to_hyperplane(GRID, W, B), f"{expected.round(6).tolist()}")
    _array(got, "distance_to_hyperplane(points, w, b)", (len(GRID),))
    np.testing.assert_allclose(got, expected, rtol=1e-12, atol=1e-15, err_msg=(
        f"expected {expected.tolist()}: |w · x + b| / ‖w‖ for each row (divide by the norm of w)"))


def test_distance_to_hyperplane_signed(vectors):
    scores = np.array(GRID) @ np.array(W) + B
    expected = scores / np.linalg.norm(W)
    got = _result(lambda: vectors.distance_to_hyperplane(GRID, W, B, signed=True), f"{expected.round(6).tolist()}")
    np.testing.assert_allclose(got, expected, rtol=1e-12, atol=1e-15, err_msg=(
        f"expected {expected.tolist()}: with signed=True, keep the sign of w · x + b"))


def test_distance_to_hyperplane_ignores_the_scale_of_w_and_b(vectors):
    point = [2.0, 1.0, -1.0]
    a = _result(lambda: vectors.distance_to_hyperplane(point, W, B), "a number")
    b = _result(lambda: vectors.distance_to_hyperplane(point, [4 * t for t in W], 4 * B), "a number")
    assert b == pytest.approx(a, rel=1e-12), (
        f"expected the same distance after multiplying w and b by 4 (the same hyperplane), got {a} and {b}")


def test_distance_to_hyperplane_returns_a_python_float_for_one_point(vectors):
    got = _result(lambda: vectors.distance_to_hyperplane(np.array([2.0, 1.0, -1.0]), np.array(W), B), "a float")
    _python_float(got, "distance_to_hyperplane of one point")
    got = _result(lambda: vectors.distance_to_hyperplane([2.0, 1.0, -1.0], W, B, signed=True), "a float")
    _python_float(got, "distance_to_hyperplane of one point, signed")


@pytest.mark.parametrize("x, w, why", [([1.0, 2.0], [0.0, 0.0], "w is zero"),
                                       ([1.0, 2.0, 3.0], [1.0, 1.0], "3 coordinates, w has 2")],
                         ids=["zero-w", "length"])
def test_distance_to_hyperplane_refuses_bad_input(vectors, x, w, why):
    _expect_value_error(lambda: vectors.distance_to_hyperplane(x, w, 1.0), f"distance_to_hyperplane({x!r}, {w!r}, 1.0)",
                        why)
