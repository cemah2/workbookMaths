"""Tests of mymath.affine (chapter M16): affine maps in homogeneous coordinates, sums over the paths of a directed graph
without cycle, and the variance of a product of independent variables.

Oracles: NumPy (``np.linalg.matrix_power``, ``np.linalg.inv`` for ``(I - A)⁻¹``), an enumeration of the paths by a
depth-first search, an exact computation of the law of a product of two independent discrete variables, and
properties (the image of ``[x, 1]`` by ``H1 @ H2`` is ``[f2(f1(x)), 1]``, ``Var(XY) ≥ Var(X) Var(Y)``). They describe
the expected behaviour without showing the solution.

    pytest tests/test_m16_affine.py              # your code
    pytest tests/test_m16_affine.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import warnings

import numpy as np
import pytest


@pytest.fixture
def aff(mymath_module):
    return mymath_module("affine")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        try:
            return call()
        except NotImplementedError:
            raise                 # a function not written yet: ⏳
        except RuntimeWarning as warning:
            pytest.fail(f"expected {expected}{' for ' + what if what else ''} without a RuntimeWarning, got "
                        f"RuntimeWarning: {warning}" + (f" ({hint})" if hint else ""))
        except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
            pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised "
                        f"{type(exc).__name__}: {exc}" + (f" ({hint})" if hint else ""))


def _expect_value_error(call, what, why, hint=""):
    """Fail with what was expected first, whatever the function did instead of raising ValueError itself."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        try:
            result = call()
        except NotImplementedError:
            raise                 # a function not written yet stays ⏳
        except ValueError as exc:
            if type(exc) is ValueError:
                return exc
            pytest.fail(f"expected {what} to raise ValueError itself ({why}), got {type(exc).__name__}: "
                        + (hint or "check the input yourself and raise ValueError, as the docstring asks"))
        except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
            pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _python_float(got, what):
    assert type(got) is float, (f"expected {what} to be a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__}")


def _show(v):
    return np.array2string(np.asarray(v, dtype=float), precision=6, suppress_small=True).replace("\n", "")


def _float_array(got, shape, what):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else ""))


def test_sum_over_paths_uses_no_ready_made_power(aff):
    """sum_over_paths multiplies the matrices itself: the tests compare it with matrix_power and inv."""
    try:
        tree = ast.parse(inspect.getsource(aff.sum_over_paths))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    forbidden = {"matrix_power", "inv", "solve", "pinv", "lstsq"}
    found = {node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute) and node.attr in forbidden}
    found |= {node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and node.id in forbidden}
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] + ([node.module] if isinstance(node, ast.ImportFrom) else [])
            found |= {n for n in names if n and n.split(".")[0] in ("scipy", "networkx", "graphlib")}
    assert not found, (f"expected sum_over_paths to multiply the matrices itself (@ in a loop), found "
                       f"{sorted(found)}: the tests compare your result with them")


# ---------------------------------------------------------------- homogeneous_matrix
def test_homogeneous_docstring_examples(aff):
    got = _result(lambda: aff.homogeneous_matrix([[2, 0], [0, 3]], [1, -1]), "the (3, 3) matrix")
    _float_array(got, (3, 3), "homogeneous_matrix([[2, 0], [0, 3]], [1, -1])")
    expected = np.array([[2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [1.0, -1.0, 1.0]])
    hint = ""
    if np.allclose(got, expected.T):
        hint = (" (that is the matrix for column vectors: here the points are rows [x, 1], so b goes on the LAST "
                "ROW and the last column is (0, …, 0, 1))")
    assert np.allclose(got, expected), f"expected {_show(expected)}, got {_show(got)}{hint}"
    H = _result(lambda: aff.homogeneous_matrix([[1], [1]], [0.5]), "the (3, 2) matrix", "W of shape (2, 1)")
    _float_array(H, (3, 2), "homogeneous_matrix([[1], [1]], [0.5])")
    image = np.array([2.0, 3.0, 1.0]) @ H
    assert np.allclose(image, [5.5, 1.0]), (
        f"expected [2, 3, 1] @ H = [5.5, 1] (2 + 3 + 0.5, then the 1 of homogeneous coordinates), got {_show(image)}")


@pytest.mark.parametrize("n, m, seed", [(1, 1, 4910), (2, 3, 4911), (4, 2, 4912), (5, 5, 4913)])
def test_homogeneous_sends_x_1_to_its_image(aff, n, m, seed):
    rng = np.random.default_rng(seed)
    W, b = rng.normal(size=(n, m)), rng.normal(size=m)
    H = _result(lambda: aff.homogeneous_matrix(W, b), f"the ({n + 1}, {m + 1}) matrix", f"W of shape {(n, m)}")
    _float_array(H, (n + 1, m + 1), f"the matrix of a map of R^{n} into R^{m}")
    X = rng.normal(size=(6, n))
    images = np.hstack([X, np.ones((6, 1))]) @ H
    expected = np.hstack([X @ W + b, np.ones((6, 1))])
    assert np.allclose(images, expected), (
        f"expected [x, 1] @ H = [x W + b, 1] for every point x, got for x = {_show(X[0])} the image "
        f"{_show(images[0])} instead of {_show(expected[0])}")


@pytest.mark.parametrize("dims, seed", [((2, 2, 2), 4914), ((3, 2, 4), 4915), ((1, 3, 2), 4916)])
def test_homogeneous_composition_is_a_product(aff, dims, seed):
    """Applying f1 then f2 is multiplying by H1 @ H2 (checked on images of points)."""
    n, m, k = dims
    rng = np.random.default_rng(seed)
    W1, b1, W2, b2 = rng.normal(size=(n, m)), rng.normal(size=m), rng.normal(size=(m, k)), rng.normal(size=k)
    H1 = _result(lambda: aff.homogeneous_matrix(W1, b1), "the matrix of f1")
    H2 = _result(lambda: aff.homogeneous_matrix(W2, b2), "the matrix of f2")
    x = rng.normal(size=n)
    got = np.append(x, 1.0) @ H1 @ H2
    expected = np.append((x @ W1 + b1) @ W2 + b2, 1.0)
    assert np.allclose(got, expected), (
        f"expected [x, 1] @ H1 @ H2 = [f2(f1(x)), 1] = {_show(expected)}, got {_show(got)}")


def test_homogeneous_leaves_its_inputs(aff):
    W, b = np.array([[1.5, -2.0], [0.0, 4.0]]), np.array([3.0, -1.0])
    copies = (W.copy(), b.copy())
    H = _result(lambda: aff.homogeneous_matrix(W, b), "the matrix")
    H[0, 0] = 99.0
    assert np.array_equal(W, copies[0]) and np.array_equal(b, copies[1]), (
        "expected W and b unchanged after the call, and a new matrix (not a view of W), got them modified")


@pytest.mark.parametrize("W, b, why", [([1, 2], [0.5], "W is 1-D"),
                                       ([[1, 2], [3, 4]], [[0.5, 1]], "b is 2-D"),
                                       ([[1, 2], [3, 4]], [0.5, 1, 2], "3 coordinates of b for 2 columns of W"),
                                       ([[1, 2], [3, 4]], [0.5], "1 coordinate of b for 2 columns of W"),
                                       ([["a", "b"]], [1, 2], "W is not made of numbers")])
def test_homogeneous_refuses_bad_arguments(aff, W, b, why):
    _expect_value_error(lambda: aff.homogeneous_matrix(W, b), f"homogeneous_matrix({W!r}, {b!r})", why)


# ---------------------------------------------------------------- sum_over_paths
def _paths_sum(A, s, t):
    """Sum over the paths of at least one edge from s to t of the products of the weights (depth-first search)."""
    A = np.asarray(A, dtype=float)
    total = 0.0

    def walk(node, product):
        nonlocal total
        for nxt in np.flatnonzero(A[node]):
            weight = product * A[node, nxt]
            if nxt == t:
                total += weight
            walk(nxt, weight)

    walk(s, 1.0)
    return total


def _random_dag(rng, n, weighted):
    """A graph without cycle: a strictly upper triangular pattern, nodes renamed at random."""
    pattern = np.triu(rng.random((n, n)) < 0.55, 1)
    values = rng.choice([-2.0, -1.0, -0.5, 0.5, 1.5, 2.0, 3.0], size=(n, n)) if weighted else np.ones((n, n))
    A = pattern * values
    order = rng.permutation(n)
    return A[np.ix_(order, order)]


def test_paths_docstring_examples(aff):
    A = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    got = _result(lambda: aff.sum_over_paths(A, 0, 3), "3.0", "the 4-node example of the docstring")
    _python_float(got, "sum_over_paths(A, 0, 3)")
    hint = ""
    if got == 2.0:
        hint = " (only the paths of 2 edges were counted: the path 0 → 1 → 2 → 3 has 3 edges)"
    elif got == 1.0:
        hint = " (only the paths of one length were counted: add up A, A², A³…)"
    assert got == 3.0, f"expected 3.0 (0 → 1 → 3, 0 → 2 → 3, 0 → 1 → 2 → 3), got {got!r}{hint}"
    got = _result(lambda: aff.sum_over_paths([[0, 2, 0], [0, 0, 0.5], [0, 0, 0]], 0, 2), "1.0", "weights 2 and 0.5")
    assert math.isclose(got, 1.0), f"expected 2 × 0.5 = 1.0 (the product of the weights along 0 → 1 → 2), got {got!r}"
    exc = _expect_value_error(lambda: aff.sum_over_paths([[0, 1], [1, 0]], 0, 1), "sum_over_paths([[0, 1], [1, 0]], 0, 1)",
                              "0 → 1 → 0 is a cycle")
    assert "the graph has a cycle" in str(exc), (
        f"expected the message \"the graph has a cycle\" (docstring), got {str(exc)!r}")


@pytest.mark.parametrize("n, seed", [(2, 4917), (5, 4918), (7, 4919), (9, 4920)])
def test_paths_counts_match_an_enumeration(aff, n, seed):
    rng = np.random.default_rng(seed)
    A = _random_dag(rng, n, weighted=False)
    for s, t in itertools.product(range(n), repeat=2):
        expected = _paths_sum(A, s, t)
        got = _result(lambda: aff.sum_over_paths(A, s, t), f"{expected:g} path(s)", f"{s} → {t} in a graph of {n} nodes")
        _python_float(got, "the number of paths")
        assert got == expected, (
            f"expected {expected:g} path(s) from {s} to {t}, got {got!r}, for the adjacency matrix "
            f"{_show(A)}")


@pytest.mark.parametrize("n, seed", [(3, 4921), (6, 4922), (8, 4923)])
def test_paths_weighted_sums_match_the_inverse(aff, n, seed):
    """For distinct nodes, the sum over the paths is the entry of (I - A)⁻¹ = I + A + … + Aⁿ⁻¹."""
    rng = np.random.default_rng(seed)
    A = _random_dag(rng, n, weighted=True)
    inverse = np.linalg.inv(np.eye(n) - A)
    powers = [np.linalg.matrix_power(A, k) for k in range(1, n)]
    for s, t in itertools.product(range(n), repeat=2):
        expected = 0.0 if s == t else float(inverse[s, t])
        got = _result(lambda: aff.sum_over_paths(A, s, t), "a sum of products of weights", f"{s} → {t}")
        hint = ""
        if s != t and math.isclose(got, float(sum(abs(P[s, t]) for P in powers)), abs_tol=1e-9) \
                and not math.isclose(got, expected, abs_tol=1e-9):
            hint = " (keep the signs of the weights: only the cycle test looks at the pattern)"
        elif s != t and math.isclose(got, _paths_sum(A != 0, s, t), abs_tol=1e-9) \
                and not math.isclose(got, expected, abs_tol=1e-9):
            hint = " (the weights count: multiply them along each path, the pattern is only for the cycle test)"
        assert math.isclose(got, expected, rel_tol=1e-9, abs_tol=1e-9), (
            f"expected {expected!r} from {s} to {t} (the entry of (I - A)⁻¹ for distinct nodes, 0 from a node to "
            f"itself), got {got!r}{hint}")


def test_paths_from_a_node_to_itself_and_unreachable(aff):
    A = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
    got = _result(lambda: aff.sum_over_paths(A, 1, 1), "0.0", "source == target",
                  "a path has at least one edge, so from a node to itself it would be a cycle")
    assert got == 0.0, f"expected 0.0 from node 1 to itself (no cycle, the empty path does not count), got {got!r}"
    got = _result(lambda: aff.sum_over_paths(A, 2, 0), "0.0", "no path from 2 to 0")
    assert got == 0.0, f"expected 0.0 when the target cannot be reached (2 → 0), got {got!r}"
    got = _result(lambda: aff.sum_over_paths([[0]], 0, 0), "0.0", "one node, no edge")
    assert got == 0.0, f"expected 0.0 for a single node without edge, got {got!r}"


@pytest.mark.parametrize("A, why", [([[1]], "a loop on the only node"),
                                    ([[0, 1, 0], [0, 1, 0], [0, 0, 0]], "a loop on node 1"),
                                    ([[0, 1, 0], [0, 0, 1], [1, 0, 0]], "the cycle 0 → 1 → 2 → 0"),
                                    ([[0, 2, 0, 0], [0, 0, 1, 0], [0, 0, 0, -2], [0, 1, 0, 0]],
                                     "the cycle 1 → 2 → 3 → 1, out of reach of node 0's target"),
                                    ([[0, 1, 1], [0, 0, 1], [0, -1, 0]],
                                     "a cycle 1 → 2 → 1 whose weights have opposite signs"),
                                    ([[1, 1], [-1, -1]],
                                     "loops and a cycle 0 → 1 → 0 whose weights cancel: A² = 0, but the pattern has "
                                     "a cycle")])
def test_paths_refuses_a_graph_with_a_cycle(aff, A, why):
    exc = _expect_value_error(lambda: aff.sum_over_paths(A, 0, len(A) - 1), f"sum_over_paths({A}, 0, {len(A) - 1})",
                              f"{why}: the graph has a cycle",
                              "test the cycle on the pattern of the non-zero weights, before summing")
    assert "the graph has a cycle" in str(exc), (
        f"expected the message \"the graph has a cycle\" (docstring), got {str(exc)!r}")


def test_paths_on_a_large_graph(aff):
    """The complete graph without cycle on 40 nodes: 2^38 paths from the first node to the last."""
    n = 40
    A = np.triu(np.ones((n, n)), 1)
    got = _result(lambda: aff.sum_over_paths(A, 0, n - 1), "2^38 paths", "40 nodes, every edge i → j for i < j")
    assert got == float(2 ** (n - 2)), (
        f"expected 2^38 = {2 ** (n - 2)} paths from 0 to 39 (choose any subset of the 38 nodes in between), "
        f"got {got!r}")


def test_paths_leaves_its_input_and_accepts_numpy_integers(aff):
    A = np.array([[0.0, 1.5, 0.0], [0.0, 0.0, 2.0], [0.0, 0.0, 0.0]])
    copy = A.copy()
    got = _result(lambda: aff.sum_over_paths(A, np.int64(0), np.int64(2)), "3.0", "NumPy integers as nodes")
    assert math.isclose(got, 3.0) and np.array_equal(A, copy), (
        f"expected 3.0 with NumPy integers as nodes and the matrix unchanged, got {got!r}"
        + ("" if np.array_equal(A, copy) else " (the matrix was modified)"))


@pytest.mark.parametrize("A, s, t, why", [([[0, 1, 0], [0, 0, 1]], 0, 1, "the matrix is not square"),
                                          ([0, 1, 0], 0, 1, "the matrix is 1-D"),
                                          ([[0, 1], [0, 0]], 0, 2, "node 2 does not exist"),
                                          ([[0, 1], [0, 0]], -1, 1, "a negative node"),
                                          ([[0, 1], [0, 0]], 0.0, 1, "a node that is a float"),
                                          ([[0, 1], [0, 0]], True, 1, "a node that is a bool")])
def test_paths_refuses_bad_arguments(aff, A, s, t, why):
    _expect_value_error(lambda: aff.sum_over_paths(A, s, t), f"sum_over_paths({A}, {s!r}, {t!r})", why)


# ---------------------------------------------------------------- variance_of_product
def _moments(values, probs):
    values, probs = np.asarray(values, dtype=float), np.asarray(probs, dtype=float)
    mean = float(values @ probs)
    return mean, float(((values - mean) ** 2) @ probs)


def test_product_docstring_examples(aff):
    got = _result(lambda: aff.variance_of_product(2, 1, 3, 4), "(6.0, 29.0)")
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (mean, variance), got {got!r}"
    _python_float(got[0], "the expectation")
    _python_float(got[1], "the variance")
    hint = ""
    if math.isclose(got[1], 4.0):
        hint = " (Var(X) Var(Y) alone is only true when both means are 0)"
    elif math.isclose(got[1], 13.0) or math.isclose(got[1], 20.0):
        hint = " (three terms: Var X Var Y + Var X E[Y]² + Var Y E[X]²)"
    assert got == (6.0, 29.0), f"expected (6.0, 29.0) = (2 × 3, 1 × 4 + 1 × 9 + 4 × 4), got {got!r}{hint}"
    got = _result(lambda: aff.variance_of_product(0, 2, 5, 0), "(0.0, 50.0)", "Y the constant 5")
    assert got == (0.0, 50.0), f"expected (0.0, 50.0): Var(5 X) = 25 × 2, got {got!r}"


@pytest.mark.parametrize("seed", [4924, 4925, 4926, 4927, 4928])
def test_product_matches_the_exact_law_of_the_product(aff, seed):
    """Two independent discrete variables: the law of X Y is the product of their laws."""
    rng = np.random.default_rng(seed)
    xs, ys = rng.integers(-4, 6, size=4).astype(float), rng.integers(-3, 5, size=3).astype(float)
    px, py = rng.dirichlet(np.ones(4)), rng.dirichlet(np.ones(3))
    products, joint = np.outer(xs, ys).ravel(), np.outer(px, py).ravel()
    expected = _moments(products, joint)
    (mx, vx), (my, vy) = _moments(xs, px), _moments(ys, py)
    got = _result(lambda: aff.variance_of_product(mx, vx, my, vy), "(E[XY], Var(XY))",
                  f"E[X] = {mx:.4f}, Var X = {vx:.4f}, E[Y] = {my:.4f}, Var Y = {vy:.4f}")
    assert np.allclose(got, expected, rtol=1e-10, atol=1e-12), (
        f"expected (E[XY], Var(XY)) = {_show(expected)} (computed on the law of the product), got {_show(got)}")
    assert got[1] >= vx * vy - 1e-12, (
        f"expected Var(XY) ≥ Var X · Var Y = {vx * vy!r} (the other two terms are ≥ 0), got {got[1]!r}")


def test_product_with_centered_variables_and_constants(aff):
    got = _result(lambda: aff.variance_of_product(0, 3, 0, 7), "(0.0, 21.0)", "two centered variables")
    assert got == (0.0, 21.0), f"expected (0.0, 21.0): with both means 0, Var(XY) = Var X · Var Y, got {got!r}"
    got = _result(lambda: aff.variance_of_product(-2, 0, 4, 0), "(-8.0, 0.0)", "two constants")
    assert got == (-8.0, 0.0), f"expected (-8.0, 0.0) for the constants -2 and 4, got {got!r}"
    got = _result(lambda: aff.variance_of_product(np.float64(1.5), np.int64(2), 2, 1), "(3.0, 12.25)",
                  "NumPy numbers")
    _python_float(got[1], "the variance")
    assert got == (3.0, 12.25), f"expected (3.0, 12.25) = (1.5 × 2, 2 × 1 + 2 × 4 + 1 × 2.25), got {got!r}"


@pytest.mark.parametrize("args, why", [((1, -0.5, 2, 1), "var_x < 0"), ((1, 0.5, 2, -1), "var_y < 0"),
                                       ((1, float("nan"), 2, 1), "var_x is NaN"),
                                       ((float("inf"), 1, 2, 1), "mean_x is infinite"),
                                       ((True, 1, 2, 1), "mean_x is a bool")])
def test_product_refuses_bad_arguments(aff, args, why):
    _expect_value_error(lambda: aff.variance_of_product(*args), f"variance_of_product{args}", why)
