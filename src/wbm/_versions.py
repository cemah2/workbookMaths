"""Versions workbookMaths is built and tested with.

Kept in sync with ``requirements.txt`` (a test checks it) and with ``docs/BIBLE.md`` §22.
Policy: the versions pre-installed on Google Colab (googlecolab/backend-info), and, for the packages shared with
workbookIA, the same pins as workbookIA, so that both repositories live in one environment. Colab's runtime of
2026-11-04 moved NumPy to 2.4: both minor versions are accepted without a warning (the tests pass with both).
Verified on 2026-11-06.
"""

__version__ = "0.1.0"

PYTHON_EXPECTED = "3.13"

# import name -> expected version, or a tuple of accepted versions (the distribution name may differ)
EXPECTED_VERSIONS = {
    "numpy": ("2.1.3", "2.4.6"),
    "scipy": "1.16.3",
    "sympy": "1.14.0",
    "matplotlib": "3.10.0",
    "pandas": "2.2.3",
    "sklearn": "1.6.1",
}

# import name -> distribution name used in requirements.txt
DIST_NAMES = {
    "sklearn": "scikit-learn",
}

VERIFIED_ON = "2026-11-06"
