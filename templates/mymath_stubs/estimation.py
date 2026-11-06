"""Estimation: sample means, bias and mean squared error of an estimator, standard error, confidence interval (M02c).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m02c_estimation.py``.
Do not use ``scipy.stats``: the tests compare your results with it. NumPy is allowed. Randomness always comes from
one generator ``numpy.random.default_rng(seed)``, passed to your random functions in a fixed order, so that the
same seed gives the same result. Every number returned is a Python ``float``.
"""


def sample_means(draw, n, repeats, seed=0):
    """Draw ``repeats`` samples of size ``n`` and return the mean of each sample.

    Parameters
    ----------
    draw : callable
        ``draw(rng, n)`` returns a sample of ``n`` values (a list or an array) drawn with the NumPy generator
        ``rng``, e.g. ``lambda rng, n: rng.exponential(2.0, n)``.
    n : int
        Size of each sample, at least 1.
    repeats : int
        Number of samples, at least 1.
    seed : int, default 0
        Seed of the single generator ``numpy.random.default_rng(seed)``; ``draw`` is called ``repeats`` times with
        it, one sample after the other.

    Returns
    -------
    numpy.ndarray
        Shape ``(repeats,)``: the mean of each sample, in the order of the draws.

    Raises
    ------
    ValueError
        If ``n < 1`` or ``repeats < 1``.

    Examples
    --------
    >>> means = sample_means(lambda rng, n: rng.random(n), 12, 4_000)   # 4 000 means of 12 uniforms
    >>> means.shape
    (4000,)
    >>> bool(abs(means.mean() - 0.5) < 0.01), bool(abs(means.std() - 1 / 12) < 0.005)
    (True, True)
    """
    # TODO: one generator for everything, then one mean per call to draw.
    raise NotImplementedError("sample_means() is not implemented yet")


def estimator_bias(estimator, draw_sample, true_value, repeats, seed=0):
    """Estimate by simulation the bias ``E[θ̂] - θ`` of an estimator.

    Parameters
    ----------
    estimator : callable
        ``estimator(sample)`` returns a number, the estimate ``θ̂`` computed from one sample.
    draw_sample : callable
        ``draw_sample(rng)`` returns one sample drawn with the NumPy generator ``rng``.
    true_value : float
        The true value ``θ`` of the parameter.
    repeats : int
        Number of simulated samples, at least 1.
    seed : int, default 0
        Seed of the single generator; ``draw_sample`` is called ``repeats`` times with it, in order. With the same
        seed, :func:`estimator_mse` sees the same samples.

    Returns
    -------
    float
        The mean of the ``repeats`` estimates, minus ``true_value``.

    Raises
    ------
    ValueError
        If ``repeats < 1``.

    Examples
    --------
    >>> b = estimator_bias(max, lambda rng: rng.random(4), 1.0, 20_000)   # the largest of 4 uniforms estimates 1
    >>> round(b, 2)
    -0.2
    """
    # TODO: simulate the estimates (one per sample), then compare their mean with the true value.
    raise NotImplementedError("estimator_bias() is not implemented yet")


def estimator_mse(estimator, draw_sample, true_value, repeats, seed=0):
    """Estimate by simulation the mean squared error ``E[(θ̂ - θ)²]`` of an estimator.

    Parameters
    ----------
    estimator, draw_sample, true_value, repeats, seed
        As in :func:`estimator_bias` (same seed, same samples).

    Returns
    -------
    float
        The mean of the ``repeats`` squared errors ``(θ̂ - θ)²``.

    Raises
    ------
    ValueError
        If ``repeats < 1``.

    Examples
    --------
    >>> round(estimator_mse(max, lambda rng: rng.random(4), 1.0, 20_000), 2)
    0.07
    """
    # TODO: the same simulation as estimator_bias, but average the squared errors.
    raise NotImplementedError("estimator_mse() is not implemented yet")


def standard_error(sample, ddof=1):
    """Return the standard error of the mean of a sample, ``s / sqrt(n)``.

    Parameters
    ----------
    sample : sequence of float
        The ``n`` observed values.
    ddof : int, default 1
        The standard deviation ``s`` divides the sum of squared deviations by ``n - ddof`` (``ddof = 1``: the
        unbiased variance of the sample).

    Returns
    -------
    float
        ``s / sqrt(n)``.

    Raises
    ------
    ValueError
        If the sample has ``ddof`` values or fewer.

    Examples
    --------
    >>> round(standard_error([3, 5, 6, 10]), 3)
    1.472
    """
    # TODO: mean, sum of squared deviations, divide by n - ddof, square root, then divide by sqrt(n).
    raise NotImplementedError("standard_error() is not implemented yet")


def confidence_interval_mean(sample, z=1.96):
    """Return the confidence interval ``mean ± z × standard error`` of the mean of a sample.

    Parameters
    ----------
    sample : sequence of float
        At least two values.
    z : float, default 1.96
        The normal quantile of the level: 1.96 for 95 %, positive.

    Returns
    -------
    tuple of float
        ``(low, high)``, with the standard error of :func:`standard_error` (``ddof = 1``).

    Raises
    ------
    ValueError
        If the sample has fewer than two values or ``z <= 0``.

    Examples
    --------
    >>> low, high = confidence_interval_mean([1, 2, 3, 4, 5], z=2)
    >>> round(low, 4), round(high, 4)
    (1.5858, 4.4142)
    """
    # TODO: reuse standard_error (it is in this module).
    raise NotImplementedError("confidence_interval_mean() is not implemented yet")
