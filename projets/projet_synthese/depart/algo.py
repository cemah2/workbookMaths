"""<The name of your algorithm>: the module of your synthesis project (PS.6).

TODO PS.6: replace this paragraph by what the module computes, in three or four lines, and its conventions (row
or column vectors, gradient shaped like the variable or written as a row, sum or mean over the examples). The
article (synthese.ipynb, §3) derives every formula that this module computes.

The rules of the project (projets/projet_synthese/README.md, « Les règles »):

* imports: NumPy, the standard library (math, fractions...) and your library ``mymath``, nothing else;
  scikit-learn, PyTorch, SciPy and SymPy are the oracles of your tests (PS.7), never used in this module;
* at least three functions of ``mymath`` that you wrote yourself (their tests pass with your code), each one useful
  to the computation;
* one public function per final formula of the derivation, whose docstring cites its equation (« Eq. (3.4) »);
* docstrings in English, in the NumPy format: what the function computes, Parameters (with their shapes), Returns
  (with its shape), Raises; an invalid input raises the announced error, with a message that says what was expected;
* the code reads next to the equations (same names, one equation per block), without Python loops over examples
  or coordinates that NumPy can do (a loop over the iterations or over time is normal).
"""

from __future__ import annotations

import numpy as np

import mymath  # your library: mymath.<module>.<function>(...), loaded from mon_travail/mymath


def example_function(x: np.ndarray) -> np.ndarray:
    """One line that says what the function computes, and its equation in the article (Eq. (3.k)).

    TODO PS.6: a model of docstring and of input check. Rename this function, rewrite it, add your own functions,
    and delete what you do not use.

    Parameters
    ----------
    x : ndarray of shape (n, p)
        What x is: n examples, p features.

    Returns
    -------
    ndarray of shape (n,)
        What the result is.

    Raises
    ------
    ValueError
        If x is not a 2-D array (the message says the expected shape and the shape received).
    """
    x = np.asarray(x, dtype=float)
    if x.ndim != 2:
        raise ValueError(f"expected a 2-D array of shape (n, p), got an array of shape {x.shape}")
    raise NotImplementedError("example_function() is not implemented yet")
