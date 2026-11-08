"""Tests of mymath.convex (chapter M10): convex hull in the plane, linear separability, geometric margin.

Oracles: SciPy (``scipy.spatial.ConvexHull``), scikit-learn (``SVC`` with a linear kernel and C = 10⁴, nearly a hard margin),
NumPy (``np.linalg.pinv`` for the projection on a hyperplane), and constructions whose answer is known (points
labelled by a hyperplane with a gap, a point placed inside the hull of the other class). They describe the expected
behaviour without showing the solution.

    pytest tests/test_m10_convex.py              # your code
    pytest tests/test_m10_convex.py --impl=ref   # the reference
"""

import ast
import inspect

import numpy as np
import pytest
from scipy.spatial import ConvexHull
from sklearn.svm import SVC


@pytest.fixture
def convex(mymath_module):
    return mymath_module("convex")


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


def _show(P):
    return np.array2string(np.asarray(P, dtype=float), precision=4, suppress_small=True).replace("\n", "")


# ---------------------------------------------------------------- no scipy.spatial
def test_convex_uses_no_scipy_spatial(convex):
    """convex.py builds the hull itself: no scipy.spatial (the tests compare with its ConvexHull)."""
    try:
        tree = ast.parse(inspect.getsource(convex))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.startswith("scipy.spatial"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith("scipy.spatial"):
                found.add(node.module)
            elif node.module == "scipy" and any(alias.name == "spatial" for alias in node.names):
                found.add("scipy.spatial")
        elif isinstance(node, ast.Attribute) and node.attr in ("spatial", "ConvexHull"):
            found.add(f".{node.attr}")
        elif isinstance(node, ast.Name) and node.id == "ConvexHull":
            found.add("ConvexHull")
    assert not found, (f"expected convex.py to build the convex hull itself, without scipy.spatial (the tests compare "
                       f"with scipy.spatial.ConvexHull), found {sorted(found)}")


# ---------------------------------------------------------------- convex_hull_2d
def _scipy_hull(P):
    """The hull vertices of ConvexHull, counterclockwise, starting with the smallest point (x, then y)."""
    P = np.asarray(P, dtype=float)
    V = P[ConvexHull(P).vertices]
    start = min(range(len(V)), key=lambda i: (V[i, 0], V[i, 1]))
    return np.roll(V, -start, axis=0)


def _hull(convex, P, what):
    got = _result(lambda: convex.convex_hull_2d(P), "an array of hull vertices", what)
    assert isinstance(got, np.ndarray), (f"expected an (h, 2) numpy.ndarray of floats for {what}, got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert got.ndim == 2 and got.shape[1:] == (2,), f"expected an array of shape (h, 2) for {what}, got {got.shape}"
    assert np.issubdtype(got.dtype, np.floating), f"expected floats for {what}, got the dtype {got.dtype}"
    return got


def _cloud(seed, n, grid=None):
    rng = np.random.default_rng(seed)
    if grid:
        return rng.integers(0, grid, size=(n, 2)).astype(float)
    return rng.normal(size=(n, 2)) * [3.0, 1.5] + [1.0, -2.0]


CLOUDS = {   # none is an example of the fiche or an exercise of the chapter
    "random-6": _cloud(101, 6),
    "random-25": _cloud(102, 25),
    "random-300": _cloud(103, 300),
    "grid-5x5-many-aligned": _cloud(104, 60, grid=5),
    "grid-3x3-many-aligned": _cloud(105, 40, grid=3),
    "grid-10x10": _cloud(106, 200, grid=10),
    "triangle-with-inside": np.array([[4.0, -1.0], [0.0, 3.0], [-2.0, -2.0], [0.5, 0.0], [1.0, 1.0], [-1.0, -1.0]]),
}


def test_convex_hull_2d_docstring_examples(convex):
    got = _hull(convex, [[0, 0], [2, 0], [1, 1], [2, 2], [0, 2], [1, 0]], "the first docstring example")
    assert np.array_equal(got, [[0, 0], [2, 0], [2, 2], [0, 2]]), (
        f"expected [[0, 0], [2, 0], [2, 2], [0, 2]] (counterclockwise from the smallest point; (1, 0) is in the middle "
        f"of an edge, (1, 1) inside), got {_show(got)}")
    got = _hull(convex, [[3, 1], [1, 1], [2, 1]], "three aligned points")
    assert np.array_equal(got, [[1, 1], [3, 1]]), f"expected the two ends [[1, 1], [3, 1]], got {_show(got)}"


@pytest.mark.parametrize("name", list(CLOUDS))
def test_convex_hull_2d_matches_scipy(convex, name):
    P = CLOUDS[name]
    expected = _scipy_hull(P)
    got = _hull(convex, P.tolist(), name)
    assert got.shape == expected.shape and np.allclose(got, expected), (
        f"expected the {len(expected)} vertices {_show(expected)} (counterclockwise, from the smallest point, without "
        f"the points in the middle of an edge) for {name}, got {len(got)}: {_show(got)}")


@pytest.mark.parametrize("n", [3, 8, 31])
def test_convex_hull_2d_points_on_a_circle_are_all_vertices(convex, n):
    rng = np.random.default_rng(n)
    angles = np.sort(rng.uniform(0, 2 * np.pi, size=n))
    P = np.column_stack([np.cos(angles), np.sin(angles)]) * 2.5
    expected = _scipy_hull(P)
    got = _hull(convex, P[rng.permutation(n)], f"{n} points on a circle")
    assert len(got) == n and np.allclose(got, expected), (
        f"expected all {n} points of the circle, counterclockwise from the smallest one, got {len(got)}: {_show(got)}")


def test_convex_hull_2d_starts_with_smallest_x_then_smallest_y(convex):
    P = [[0, 4], [3, 1], [0, 1], [5, 2], [3, 6], [0, 2]]
    got = _hull(convex, P, "points that share their smallest x")
    assert np.array_equal(got[0], [0, 1]), (
        f"expected the first vertex (0, 1): the smallest x, then the smallest y among the points with that x, got "
        f"{_show(got[0])} (sort by x, then by y)")
    assert np.allclose(got, _scipy_hull(P)), f"expected {_show(_scipy_hull(P))}, got {_show(got)}"


def test_convex_hull_2d_is_counterclockwise(convex):
    P = CLOUDS["random-25"]
    got = _hull(convex, P, "random-25")
    x, y = got[:, 0], got[:, 1]
    area = 0.5 * float(np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y))
    assert area > 0, (f"expected the vertices in counterclockwise order (a positive signed area), got the signed area "
                      f"{area:.4f}: check the sign of the cross product")


@pytest.mark.parametrize("name", ["random-300", "grid-5x5-many-aligned"])
def test_convex_hull_2d_contains_every_point_and_turns_left(convex, name):
    P = CLOUDS[name]
    H = _hull(convex, P, name)
    edges = np.roll(H, -1, axis=0) - H
    for i in range(len(H)):
        turn = edges[i, 0] * edges[(i + 1) % len(H), 1] - edges[i, 1] * edges[(i + 1) % len(H), 0]
        assert turn > 0, (f"expected a strict left turn at each vertex for {name}, got {turn:.3g} at {_show(H[(i + 1) % len(H)])} "
                          f"(a point in the middle of an edge, or a clockwise order)")
    for p in P:
        sides = edges[:, 0] * (p[1] - H[:, 1]) - edges[:, 1] * (p[0] - H[:, 0])
        assert np.all(sides >= -1e-9), f"expected every point inside the hull for {name}, {_show(p)} is outside"


@pytest.mark.parametrize("P, ends", [
    ([[2, 5], [-1, 5], [7, 5], [0, 5]], [[-1, 5], [7, 5]]),
    ([[3, 4], [3, -2], [3, 0]], [[3, -2], [3, 4]]),
    ([[1, 1], [4, -5], [2, -1], [0, 3], [3, -3]], [[0, 3], [4, -5]]),
], ids=["horizontal", "vertical", "slanted"])
def test_convex_hull_2d_aligned_points_give_the_two_ends(convex, P, ends):
    got = _hull(convex, P, "aligned points")
    assert np.array_equal(got, ends), (
        f"expected the two ends of the segment {ends}, the smallest point first, for the aligned points {P}, got "
        f"{_show(got)}")


def test_convex_hull_2d_single_and_repeated_points(convex):
    got = _hull(convex, [[2.5, -1.0]], "one point")
    assert np.array_equal(got, [[2.5, -1.0]]), f"expected [[2.5, -1.0]] for one point, got {_show(got)}"
    got = _hull(convex, [[4, 4], [4, 4], [4, 4]], "the same point three times")
    assert np.array_equal(got, [[4, 4]]), f"expected [[4., 4.]] for one distinct point, got {_show(got)}"
    P = [[0, 0], [3, 0], [0, 0], [0, 3], [3, 0], [1, 1], [0, 3]]
    got = _hull(convex, P, "a triangle whose vertices are repeated")
    assert np.array_equal(got, [[0, 0], [3, 0], [0, 3]]), (
        f"expected each vertex once, [[0, 0], [3, 0], [0, 3]], got {_show(got)} (keep the distinct points)")


def test_convex_hull_2d_accepts_tuples_and_keeps_its_input(convex):
    P = np.array([[1.0, 2.0], [-3.0, 0.5], [2.0, -1.0], [0.0, 0.0], [-1.0, 3.0]])
    before = P.copy()
    _hull(convex, P, "an array")
    assert np.array_equal(P, before), "expected convex_hull_2d not to modify the array it receives (it sorted it?)"
    got = _hull(convex, [tuple(p) for p in P.tolist()], "a list of tuples")
    assert np.allclose(got, _scipy_hull(P)), f"expected {_show(_scipy_hull(P))} from a list of tuples, got {_show(got)}"


@pytest.mark.parametrize("bad, why", [
    ([], "no point"),
    ([[1, 2, 3], [4, 5, 6], [0, 1, 1]], "three columns"),
    ([1.0, 2.0], "a single 1-D point instead of a 2-D array"),
], ids=["empty", "three-columns", "one-dimensional"])
def test_convex_hull_2d_rejects_bad_input(convex, bad, why):
    _expect_value_error(lambda: convex.convex_hull_2d(bad), f"convex_hull_2d({bad})", why)


# ---------------------------------------------------------------- is_linearly_separable
def _separable(convex, X, y, what):
    got = _result(lambda: convex.is_linearly_separable(X, y), "True or False", what)
    assert isinstance(got, bool), (f"expected a Python bool for {what}, got {type(got).__module__}.{type(got).__name__}"
                                   f" (wrap the result in bool(...))")
    return got


def _labelled_by_hyperplane(seed, n, d, gap):
    """Points labelled by a random hyperplane, none closer to it than gap: separable by construction."""
    rng = np.random.default_rng(seed)
    w, b = rng.normal(size=d), rng.normal()
    w /= np.linalg.norm(w)
    X = rng.normal(size=(4 * n, d)) * 2
    s = X @ w + b
    keep = np.abs(s) >= gap
    return X[keep][:n], np.where(s[keep][:n] > 0, 1, -1)


def _with_a_point_inside(seed, n, d):
    """A positive point placed at a convex combination of negative points: the hulls meet, not separable."""
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, d))
    y = rng.choice([-1, 1], size=n)
    y[: d + 1] = -1
    weights = rng.dirichlet(np.ones(d + 1))
    inside = weights @ X[: d + 1]
    return np.vstack([X, inside]), np.append(y, 1)


def test_is_linearly_separable_docstring_examples(convex):
    assert _separable(convex, [[0, 0], [1, 1]], [-1, 1], "two points") is True, (
        "expected True for two points of different labels (the docstring example)")
    assert _separable(convex, [[0], [1], [2]], [1, -1, 1], "+1, -1, +1 on a line") is False, (
        "expected False for the labels +1, -1, +1 at 0, 1, 2: the -1 point is between the two +1 points")


@pytest.mark.parametrize("seed, n, d", [(201, 10, 1), (202, 30, 2), (203, 40, 3), (204, 60, 5)])
def test_is_linearly_separable_true_for_points_labelled_by_a_hyperplane(convex, seed, n, d):
    X, y = _labelled_by_hyperplane(seed, n, d, gap=0.05)
    assert _separable(convex, X.tolist(), y.tolist(), f"{n} points in dimension {d}") is True, (
        f"expected True for {n} points in dimension {d} labelled by the side of a hyperplane (separable by "
        f"construction)")


@pytest.mark.parametrize("seed, n, d", [(211, 10, 1), (212, 30, 2), (213, 40, 3), (214, 60, 5)])
def test_is_linearly_separable_false_when_a_point_is_inside_the_other_hull(convex, seed, n, d):
    X, y = _with_a_point_inside(seed, n, d)
    assert _separable(convex, X, y, f"{n + 1} points in dimension {d}") is False, (
        f"expected False in dimension {d}: one +1 point is a convex combination of -1 points, so the two convex hulls "
        f"meet and no hyperplane separates them")


def test_is_linearly_separable_needs_the_offset_b(convex):
    X = [[3, 1], [4, 1], [6, 1], [7, 1]]   # every point far from the origin: a separator must not go through it
    assert _separable(convex, X, [-1, -1, 1, 1], "points that need an offset") is True, (
        "expected True for x = 3, 4 (label -1) and x = 6, 7 (label +1) at height 1: the line x = 5 separates them; "
        "keep the offset b among the unknowns (a column of ones)")
    assert _separable(convex, [[-2.0], [1.0], [2.0]], [1, -1, -1], "a point on each side of x = -0.5") is True, (
        "expected True: x = -0.5 separates -2 from 1 and 2")


@pytest.mark.parametrize("seed", range(221, 233))
def test_is_linearly_separable_matches_a_hard_margin_svm(convex, seed):
    rng = np.random.default_rng(seed)
    d, n = int(rng.integers(2, 4)), int(rng.integers(6, 10))
    X = rng.normal(size=(n, d))
    y = rng.choice([-1, 1], size=n)
    y[0], y[1] = -1, 1
    svm = SVC(kernel="linear", C=1e4).fit(X, y)   # a large C: nearly a hard margin
    expected = bool(np.all(svm.predict(X) == y))
    got = _separable(convex, X, y, f"{n} random labels in dimension {d}")
    assert got is expected, (f"expected {expected} for {n} points in dimension {d} with random labels (a hard-margin "
                             f"linear SVM {'separates' if expected else 'cannot separate'} them), got {got}")


def test_is_linearly_separable_one_label_and_one_point(convex):
    assert _separable(convex, [[1, 2], [3, -1], [0, 0]], [1, 1, 1], "a single label") is True, (
        "expected True when every point has the same label (the docstring says so)")
    assert _separable(convex, [[5.0, -2.0, 1.0]], [-1], "one point") is True, "expected True for a single point"


def test_is_linearly_separable_same_point_with_two_labels(convex):
    X = [[1, 1], [2, 0], [1, 1], [-3, 2]]
    assert _separable(convex, X, [1, -1, -1, 1], "a point repeated with both labels") is False, (
        "expected False: the point (1, 1) carries both labels, it cannot be on both sides")


@pytest.mark.parametrize("X, y, why", [
    ([[0, 0], [1, 1], [2, 2]], [1, -1], "two labels for three points"),
    ([[0, 0], [1, 1]], [0, 1], "the labels 0 and 1 instead of -1 and +1"),
    ([[0, 0], [1, 1]], [-1, 2], "the label 2"),
], ids=["lengths", "zero-one", "two"])
def test_is_linearly_separable_rejects_bad_labels(convex, X, y, why):
    _expect_value_error(lambda: convex.is_linearly_separable(X, y), f"is_linearly_separable({X}, {y})", why)


# ---------------------------------------------------------------- margin_of_separator
def _margin(convex, X, y, w, b, what):
    got = _result(lambda: convex.margin_of_separator(X, y, w, b), "a float", what)
    assert type(got) is float, (f"expected a Python float for {what}, got {type(got).__module__}."
                                f"{type(got).__name__} (wrap the result in float(...))")
    return got


def _projection_margin(X, y, w, b):
    """Oracle: the signed distances from the projections on the hyperplane, found with np.linalg.pinv."""
    X, y, w = np.asarray(X, float), np.asarray(y, float), np.asarray(w, float)
    row = w[None, :]
    distances = []
    for x, label in zip(X, y):
        score = float((row @ x)[0]) + b
        delta = np.linalg.pinv(row) @ np.array([-score])               # the smallest move onto w·p + b = 0
        side = 1.0 if score > 0 else -1.0 if score < 0 else 0.0
        distances.append(label * side * np.linalg.norm(delta))
    return min(distances)


def test_margin_of_separator_docstring_examples(convex):
    got = _margin(convex, [[0, 0], [2, 2]], [-1, 1], [1, 1], -2, "the first docstring example")
    assert got == pytest.approx(2 ** 0.5), f"expected √2 ≈ 1.4142 (2 / ‖(1, 1)‖), got {got}"
    got = _margin(convex, [[0, 0], [2, 2]], [1, 1], [0, 1], -1, "the second docstring example")
    assert got == pytest.approx(-1.0), f"expected -1.0 ((0, 0), labelled +1, is at distance 1 on the wrong side), got {got}"


@pytest.mark.parametrize("seed, n, d", [(301, 5, 2), (302, 12, 3), (303, 30, 6)])
def test_margin_of_separator_matches_projections(convex, seed, n, d):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, d)) * 3
    w, b = rng.normal(size=d) * 2, float(rng.normal())
    y = np.where(X @ w + b > 0, 1, -1)
    y[0] = -y[0]                                 # one point on the wrong side: a negative margin
    for labels, what in ((np.where(X @ w + b > 0, 1, -1), "every point on its side"), (y, "one point misplaced")):
        expected = _projection_margin(X, labels, w, b)
        got = _margin(convex, X.tolist(), labels.tolist(), w.tolist(), b, f"{n} points in dimension {d}, {what}")
        assert got == pytest.approx(expected, abs=1e-9), (
            f"expected the margin {expected:.6f} (the smallest y_i (w · x_i + b) / ‖w‖) for {n} points in dimension "
            f"{d}, {what}, got {got:.6f}")


def test_margin_of_separator_by_cross_products_in_the_plane(convex):
    X = np.array([[1.0, 4.0], [3.0, 3.5], [-2.0, 1.0], [0.0, -1.5], [4.0, 0.5]])
    y = [1, 1, -1, -1, 1]
    a, q = np.array([-1.0, 3.0]), np.array([2.0, -1.0])    # two points of the line
    w = np.array([q[1] - a[1], a[0] - q[0]])                # a normal: (q - a) turned by a quarter turn
    b = -float(w @ a)
    direction = (q - a) / np.linalg.norm(q - a)
    side = np.sign(X @ w + b)
    dist = np.abs((X[:, 0] - a[0]) * direction[1] - (X[:, 1] - a[1]) * direction[0])
    expected = float(np.min(np.array(y) * side * dist))
    got = _margin(convex, X, y, w, b, "five points of the plane")
    assert got == pytest.approx(expected, abs=1e-9), (
        f"expected {expected:.6f} (signed distances to the line through (-1, 3) and (2, -1)), got {got:.6f}")
    got_scaled = _margin(convex, X, y, -3 * w, -3 * b, "the same line, (w, b) multiplied by -3")
    assert got_scaled == pytest.approx(float(np.min(-np.array(y) * side * dist)), abs=1e-9), (
        f"expected {float(np.min(-np.array(y) * side * dist)):.6f}: multiplying (w, b) by -3 exchanges the two sides, "
        f"got {got_scaled:.6f}")


@pytest.mark.parametrize("c", [0.001, 0.5, 7.0, 1e6])
def test_margin_of_separator_ignores_a_positive_factor(convex, c):
    X, y, w, b = [[2, 1], [0, 3], [-1, -1], [1, -2]], [1, 1, -1, -1], [1.0, 2.0], -0.5
    reference = _projection_margin(X, y, w, b)
    got = _margin(convex, X, y, [c * v for v in w], c * b, f"(w, b) multiplied by {c}")
    assert got == pytest.approx(reference, rel=1e-9), (
        f"expected the same margin {reference:.6f} with (w, b) multiplied by {c} > 0 (divide by ‖w‖), got {got:.6f}")


def test_margin_of_separator_zero_on_the_hyperplane(convex):
    got = _margin(convex, [[1, 1], [3, 0], [-1, 2]], [1, 1, -1], [1, -1], 0.0, "a point on the line x₁ = x₂")
    assert got == pytest.approx(0.0, abs=1e-12), f"expected 0.0: (1, 1) is on the hyperplane x₁ - x₂ = 0, got {got}"


def test_margin_of_separator_keeps_its_inputs(convex):
    X, y, w = np.array([[1.0, 2.0], [-1.0, 0.5]]), np.array([1, -1]), np.array([2.0, 1.0])
    before = (X.copy(), y.copy(), w.copy())
    _margin(convex, X, y, w, 0.25, "two points")
    assert all(np.array_equal(a, b) for a, b in zip((X, y, w), before)), (
        "expected margin_of_separator not to modify X, y or w")


@pytest.mark.parametrize("args, why", [
    (([[0, 0], [1, 1]], [1, -1], [0, 0], 1.0), "w is zero"),
    (([[0, 0], [1, 1]], [1, -1], [1, 1, 1], 0.0), "w has three entries for points of the plane"),
    (([[0, 0], [1, 1]], [1, -1, 1], [1, 1], 0.0), "three labels for two points"),
    (([[0, 0], [1, 1]], [1, 0], [1, 1], 0.0), "the label 0"),
], ids=["zero-w", "w-length", "y-length", "label-zero"])
def test_margin_of_separator_rejects_bad_input(convex, args, why):
    _expect_value_error(lambda: convex.margin_of_separator(*args), f"margin_of_separator{args}", why)
