"""Answer kinds specific to maths: exact fractions, expressions and intervals (BIBLE §14).

They plug into :mod:`wbm.checker`: ``wbm.record(id, value, kind="fraction" | "expr" | "interval")`` on the solutions
side, and the usual ``wbm.check(id, value)`` on the learner's side (the stored kind decides how the value is read).
As for the other kinds, only salted hashes are stored, never the answer itself.

* ``fraction``: an exact rational number. Accepted: ``"3/4"``, ``Fraction(3, 4)``, ``sympy.Rational(3, 4)``, an
  integer, ``0.75`` or ``"0,75"`` when the decimal value is exact. ``simplified=True``: a fraction typed as text must
  be irreducible (``"6/8"`` is then refused, with a message that says the value itself is right).
* ``expr``: an expression of one or more variables, read with SymPy (``"2*x*exp(x**2)"``, ``"2x e^(x^2)"``,
  ``"ln(x) + 1/x"``...). Two expressions are equal when they take the same values at a few fixed rational points
  (computed with 30 significant digits, compared on 10); the right expression is never stored, only the hashes of its
  values. ``up_to_constant=True`` (a primitive): two expressions that differ by a constant are equal.
* ``interval``: an interval or a union of intervals, in French (``"]2 ; 5]"``, ``"[0 ; +∞["``) or English notation
  (``"(2, 5]"``), or a SymPy set. Endpoints can be exact (``"1/2"``, ``"sqrt(2)"``, ``"-oo"``).
"""

from __future__ import annotations

import math
import numbers
import re
from decimal import Decimal
from fractions import Fraction

MATH_KINDS = ("fraction", "expr", "interval")

SIGNIFICANT = 10          # significant digits compared for expressions and interval endpoints
_PRECISION = 30           # digits used to evaluate
_DEFAULT_POINTS = ("1/3", "5/7", "6/5", "-2/5", "9/4", "-7/3", "3/11", "13/6")
_N_POINTS = 5


class MathNormalizationError(ValueError):
    """The value cannot be read as the expected kind; the message says what was expected."""


def _hash(ex_id: str, kind: str, normalized: str) -> str:
    from wbm.checker import hash_answer

    return hash_answer(ex_id, kind, normalized)


def _clean_text(text: str) -> str:
    """Typographic signs a French keyboard or a copy-paste produces -> ASCII."""
    table = {"−": "-", "–": "-", "—": "-", "×": "*", "·": "*", "⋅": "*", "÷": "/",
             "√": "sqrt", "∞": "oo", "π": "pi", " ": " ", " ": " "}
    for old, new in table.items():
        text = text.replace(old, new)
    # x², x⁴, x¹⁰, x⁻¹ -> x**(2), x**(4), x**(10), x**(-1)
    text = _SUPERSCRIPTS.sub(lambda m: "**(" + m.group().translate(_SUPERSCRIPT_DIGITS) + ")", text)
    return text.strip()


_SUPERSCRIPT_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")
_SUPERSCRIPTS = re.compile(r"⁻?[⁰¹²³⁴⁵⁶⁷⁸⁹]+")
# "Ln(5)", "LOG(x)" -> lower case; "ln5", "ln2.5" -> "ln(5)", "ln(2.5)"; "f'(x) = ...", "y = ..." -> the right side
_FUNCTION_CASE = re.compile(r"\b(ln|log|exp|sqrt|sin|cos|tan)\b", re.IGNORECASE)
_FUNCTION_NUMBER = re.compile(r"\b(ln|log|exp|sqrt)(\d+(?:\.\d+)?)\b")
_NAME_PREFIX = re.compile(r"\s*[A-Za-z]'*\s*(?:\(\s*[a-z]\s*\))?\s*")


# ---------------------------------------------------------------------------
# fraction
# ---------------------------------------------------------------------------
_FRACTION_TEXT = re.compile(r"\s*([+-]?)\s*\(?\s*([+-]?\d+)\s*\)?\s*/\s*\(?\s*([+-]?\d+)\s*\)?\s*")
_DECIMAL_TEXT = re.compile(r"\s*[+-]?\d+(?:[.,]\d+)?\s*")


def _parse_fraction(value) -> tuple[Fraction, bool | None]:
    """(exact value, typed as an irreducible fraction?) ; the flag is None when no fraction was typed."""
    try:
        import sympy

        if isinstance(value, sympy.Basic):
            if value.is_Rational:
                return Fraction(int(value.p), int(value.q)), None
            raise MathNormalizationError("une fraction exacte (la valeur n'est pas rationnelle)")
    except ImportError:  # pragma: no cover
        pass
    if isinstance(value, Fraction):
        return value, None
    if isinstance(value, bool):
        raise MathNormalizationError("une fraction comme \"3/4\" (pas un booléen)")
    if (isinstance(value, tuple) and len(value) == 2
            and all(isinstance(v, numbers.Integral) and not isinstance(v, bool) for v in value)):
        raise MathNormalizationError(_DECIMAL_COMMA)
    if isinstance(value, numbers.Integral):
        return Fraction(int(value)), None
    if isinstance(value, numbers.Real):
        x = float(value)
        if not math.isfinite(x):
            raise MathNormalizationError("une fraction exacte, pas l'infini ni NaN")
        candidate = Fraction(x).limit_denominator(10**6)
        if abs(float(candidate) - x) <= 1e-12 * max(1.0, abs(x)) and len(repr(x)) <= 12:
            return candidate, None
        raise _ApproximateValue(x)
    if isinstance(value, str):
        text = _clean_text(value).replace(" ", "")
        match = _FRACTION_TEXT.fullmatch(text)
        if match:
            outer, num, den = match.groups()
            numerator, denominator = int(num), int(den)
            if denominator == 0:
                raise MathNormalizationError("une fraction dont le dénominateur n'est pas nul")
            sign = -1 if outer == "-" else 1
            irreducible = math.gcd(numerator, denominator) == 1 and denominator > 0
            return sign * Fraction(numerator, denominator), irreducible
        if _DECIMAL_TEXT.fullmatch(text):
            decimal = Decimal(text.replace(",", "."))
            return Fraction(decimal), None
        number = _exact_number(text)
        if number is not None:
            if number.is_Rational:
                return Fraction(int(number.p), int(number.q)), None
            raise _IrrationalValue()
        raise MathNormalizationError("une fraction écrite comme \"3/4\" ou \"-5/2\" (ou un entier)")
    raise MathNormalizationError("une fraction écrite comme \"3/4\" (texte), ou Fraction(3, 4)")


_DECIMAL_COMMA = ("un décimal écrit avec un point : en Python, `0,5` sans guillemets est un couple de deux nombres, "
                  "`(0, 5)`. Écris `0.5`, ou `\"0,5\"` entre guillemets, ou une fraction entre guillemets")


def _exact_number(text: str):
    """The exact real number written in ``text`` ("sqrt(3)/2", "(1 + 2)/4"...), or None if it is not one."""
    try:
        number = parse_expression(text, [])
    except MathNormalizationError:
        return None
    return number if number.is_number and number.is_real else None


class _IrrationalValue(MathNormalizationError):
    """A number typed as text that is not rational ("sqrt(3)/2"): a wrong value, not a wrong form."""

    def __init__(self):
        super().__init__("une fraction")


class _ApproximateValue(MathNormalizationError):
    """A float that is not a short exact decimal: maybe an approximation of the right fraction."""

    def __init__(self, x: float):
        super().__init__("la valeur exacte, sous forme de fraction (\"2/7\"), pas une valeur approchée")
        self.x = x


def _norm_fraction(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


# ---------------------------------------------------------------------------
# expr
# ---------------------------------------------------------------------------
def _symbols(variables):
    import sympy

    return [sympy.Symbol(name) for name in variables]


def parse_expression(value, variables):
    """A SymPy expression from a string or a SymPy object; MathNormalizationError with a helpful message."""
    import sympy
    from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application, parse_expr,
                                            standard_transformations)

    names = list(variables)
    if isinstance(value, sympy.Basic):
        expr = value
    elif isinstance(value, numbers.Number) and not isinstance(value, bool):
        expr = sympy.nsimplify(value) if isinstance(value, float) else sympy.Integer(int(value))
    elif isinstance(value, str):
        text = _clean_text(value)
        if text.count("=") == 1 and _NAME_PREFIX.fullmatch(text.split("=")[0]):
            text = text.split("=")[1].strip()   # "f'(x) = 2x", "y = 3x - 1": the expression is on the right
        text = _FUNCTION_CASE.sub(lambda m: m.group().lower(), text)
        text = _FUNCTION_NUMBER.sub(r"\1(\2)", text)
        if not text:
            raise MathNormalizationError("une expression, par exemple \"3*x**2 + exp(x)\"")
        local = {name: sympy.Symbol(name) for name in names}
        local.update({"ln": sympy.log, "log": sympy.log, "exp": sympy.exp, "sqrt": sympy.sqrt, "pi": sympy.pi,
                      "oo": sympy.oo, "sin": sympy.sin, "cos": sympy.cos, "tan": sympy.tan, "abs": sympy.Abs,
                      "Abs": sympy.Abs, "tanh": sympy.tanh, "sinh": sympy.sinh, "cosh": sympy.cosh})
        if "e" not in names:
            local["e"] = sympy.E
        transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
        try:
            expr = parse_expr(text, local_dict=local, transformations=transformations, evaluate=True)
        except Exception as exc:  # SyntaxError, TokenError, TypeError...: the learner's text
            raise MathNormalizationError(
                "une expression lisible, écrite comme en Python : 3*x**2 + exp(x), ln(x)/x, sqrt(1 - x**2) "
                f"(je n'arrive pas à lire {value!r})") from exc
    elif callable(value):
        raise MathNormalizationError("l'expression sous forme de texte, par exemple \"2*x*exp(x**2)\", "
                                     "pas une fonction Python")
    else:
        raise MathNormalizationError("une expression sous forme de texte, par exemple \"2*x*exp(x**2)\"")
    if not isinstance(expr, sympy.Basic):
        raise MathNormalizationError("une expression mathématique, par exemple \"2*x*exp(x**2)\"")
    unknown = sorted(str(s) for s in expr.free_symbols if str(s) not in names)
    if unknown:
        allowed = ", ".join(names) if names else "aucune variable"
        raise MathNormalizationError(
            f"une expression de {allowed} seulement (ton expression contient aussi : {', '.join(unknown)} ; "
            "pour une multiplication, écris le signe *)")
    return expr


def _round_significant(value) -> str | None:
    """A SymPy number evaluated with 30 digits -> its 10 significant digits as text; None if not a finite real."""
    import sympy

    try:
        number = sympy.N(value, _PRECISION)
    except Exception:  # noqa: BLE001  (SymPy can raise many things on a bad point)
        return None
    if number.has(sympy.zoo, sympy.nan, sympy.oo, -sympy.oo) or not number.is_number:
        return None
    re_part, im_part = number.as_real_imag()
    try:
        re_value, im_value = Decimal(str(sympy.N(re_part, _PRECISION))), Decimal(str(sympy.N(im_part, _PRECISION)))
    except Exception:  # noqa: BLE001
        return None
    if not re_value.is_finite() or not im_value.is_finite():
        return None
    scale = max(abs(re_value), Decimal(1))
    if abs(im_value) > scale * Decimal("1e-20"):
        return None                                   # not a real number at this point (ln of a negative...)
    if abs(re_value) < Decimal("1e-20"):
        return "0"
    return f"{re_value:.{SIGNIFICANT - 1}e}"


def _evaluate(expr, variables, point: tuple) -> str | None:
    import sympy

    subs = {sympy.Symbol(name): sympy.Rational(p) for name, p in zip(variables, point)}
    try:
        value = expr.subs(subs)
    except Exception:  # noqa: BLE001
        return None
    return _round_significant(value)


def _default_points(n_vars: int) -> list[tuple[str, ...]]:
    """Fixed rational points: point i takes the values i, i+1, ... of the default list (shifted per variable)."""
    pool = _DEFAULT_POINTS
    return [tuple(pool[(i + 3 * j) % len(pool)] for j in range(n_vars)) for i in range(len(pool))]


def _fingerprint(expr, variables, points, up_to_constant: bool) -> list[str] | None:
    values = [_evaluate(expr, variables, point) for point in points]
    if any(v is None for v in values):
        return None
    if up_to_constant:
        import sympy

        base = sympy.N(expr.subs({sympy.Symbol(n): sympy.Rational(p) for n, p in zip(variables, points[0])}),
                       _PRECISION)
        diffs = []
        for point in points[1:]:
            subs = {sympy.Symbol(n): sympy.Rational(p) for n, p in zip(variables, point)}
            diffs.append(_round_significant(expr.subs(subs) - base))
        if any(d is None for d in diffs):
            return None
        return diffs
    return values


def _expr_hash(ex_id: str, fingerprint: list[str]) -> str:
    return _hash(ex_id, "expr", "|".join(fingerprint))


# ---------------------------------------------------------------------------
# interval
# ---------------------------------------------------------------------------
_UNION = re.compile(r"\s*(?:∪|\bU\b|\bu\b|\bunion\b)\s*")
_ONE_INTERVAL = re.compile(r"\s*([\[\]\(])\s*(.+?)\s*([;,])\s*(.+?)\s*([\[\]\)])\s*")


def _endpoint(text: str):
    import sympy

    text = _clean_text(text).replace(" ", "")
    if text.lower() in {"oo", "+oo", "inf", "+inf", "infini", "+infini"}:
        return sympy.oo
    if text.lower() in {"-oo", "-inf", "-infini"}:
        return -sympy.oo
    try:
        value = parse_expression(text.replace(",", "."), [])
    except MathNormalizationError as exc:
        raise MathNormalizationError(f"des bornes qui sont des nombres (je n'arrive pas à lire {text!r})") from exc
    if not value.is_real:
        raise MathNormalizationError(f"des bornes réelles ({text!r} n'en est pas une)")
    return value


def _parse_intervals(value):
    """A list of (left_closed, a, b, right_closed) with SymPy endpoints, sorted; [] for the empty set."""
    import sympy

    if isinstance(value, sympy.Set):
        if value is sympy.S.EmptySet:
            return []
        parts = value.args if isinstance(value, sympy.Union) else (value,)
        intervals = []
        for part in parts:
            if isinstance(part, sympy.FiniteSet):
                intervals += [(True, x, x, True) for x in part.args]
            elif isinstance(part, sympy.Interval):
                intervals.append((not part.left_open, part.start, part.end, not part.right_open))
            else:
                raise MathNormalizationError("un intervalle ou une réunion d'intervalles")
        return sorted(intervals, key=lambda t: (float(t[1]), not t[0]))
    if not isinstance(value, str):
        raise MathNormalizationError("un intervalle écrit comme \"[2 ; 5[\" ou \"(2, 5]\"")
    text = _clean_text(value)
    if text.lower() in {"∅", "{}", "vide", "ensemble vide", "empty", "emptyset"}:
        return []
    intervals = []
    for piece in _UNION.split(text):
        match = _ONE_INTERVAL.fullmatch(piece)
        if not match:
            raise MathNormalizationError(
                "un intervalle écrit comme \"[2 ; 5[\" ou \"]-oo ; 3]\" (réunion : \"[0 ; 1] U [2 ; 3]\")")
        left, a_text, separator, b_text, right = match.groups()
        if separator == "," and ";" in piece:
            raise MathNormalizationError("un seul séparateur entre les bornes (« ; » en français)")
        a, b = _endpoint(a_text), _endpoint(b_text)
        left_closed, right_closed = left == "[", right == "]"
        if (a == -sympy.oo and left_closed) or (b == sympy.oo and right_closed):
            raise _ClosedAtInfinity()
        if a > b or (a == b and not (left_closed and right_closed)):
            raise MathNormalizationError("des bornes dans l'ordre : la plus petite d'abord")
        intervals.append((left_closed, a, b, right_closed))
    return sorted(intervals, key=lambda t: (float(t[1]), not t[0]))


class _ClosedAtInfinity(MathNormalizationError):
    def __init__(self):
        super().__init__("un crochet ouvert du côté de l'infini : on écrit \"[0 ; +oo[\", jamais \"[0 ; +oo]\"")


def _norm_endpoint(x) -> str:
    import sympy

    if x == sympy.oo:
        return "+oo"
    if x == -sympy.oo:
        return "-oo"
    return _round_significant(x) or "?"


def _norm_intervals(intervals) -> str:
    if not intervals:
        return "empty"
    return "U".join(f"{'[' if lc else '('}{_norm_endpoint(a)},{_norm_endpoint(b)}{']' if rc else ')'}"
                    for lc, a, b, rc in intervals)


# ---------------------------------------------------------------------------
# entries (solutions side) and checks (learner side)
# ---------------------------------------------------------------------------
def make_math_entry(ex_id: str, value, kind: str, *, variables=None, simplified: bool = False,
                    up_to_constant: bool = False, mistakes: dict | None = None) -> dict:
    """The hash-only entry of a fraction, expression or interval answer."""
    entry: dict = {"kind": kind}
    if kind == "fraction":
        q, _ = _parse_fraction(value)
        entry["hash"] = _hash(ex_id, kind, _norm_fraction(q))
        entry["sign"] = 0 if q == 0 else (1 if q > 0 else -1)
        if simplified:
            entry["simplified"] = True
        wrong = {message: _norm_fraction(_parse_fraction(w)[0]) for message, w in (mistakes or {}).items()}
        right = _norm_fraction(q)
    elif kind == "expr":
        if not variables:
            raise ValueError(f"Ex {ex_id}: give `variables` for an expression answer, e.g. variables=('x',)")
        variables = [str(v) for v in variables]
        expr = parse_expression(value, variables)
        points = [p for p in _default_points(len(variables))
                  if _evaluate(expr, variables, p) is not None][:_N_POINTS + (1 if up_to_constant else 0)]
        if len(points) < 3 + (1 if up_to_constant else 0):
            raise ValueError(f"Ex {ex_id}: the expression is undefined at too many default points")
        fingerprint = _fingerprint(expr, variables, points, up_to_constant)
        if len(set(fingerprint)) == 1 and not up_to_constant and len(variables) and expr.free_symbols:
            raise ValueError(f"Ex {ex_id}: the expression takes the same value at every point")
        entry.update(hash=_expr_hash(ex_id, fingerprint), variables=variables, points=[list(p) for p in points])
        if up_to_constant:
            entry["up_to_constant"] = True
        wrong = {}
        for message, w in (mistakes or {}).items():
            fp = _fingerprint(parse_expression(w, variables), variables, points, up_to_constant)
            if fp is None:
                raise ValueError(f"Ex {ex_id}: mistake {message!r} is undefined at a check point")
            wrong[message] = "|".join(fp)
        right = "|".join(fingerprint)
    elif kind == "interval":
        norm = _norm_intervals(_parse_intervals(value))
        entry["hash"] = _hash(ex_id, kind, norm)
        wrong = {message: _norm_intervals(_parse_intervals(w)) for message, w in (mistakes or {}).items()}
        right = norm
    else:
        raise ValueError(f"unknown math kind: {kind!r}")
    if wrong:
        entry["mistakes"] = {}
        for message, norm_wrong in wrong.items():
            if not isinstance(message, str) or " " not in message.strip():
                raise ValueError(f"Ex {ex_id}: `mistakes` maps a MESSAGE (a sentence) to a wrong value, but "
                                 f"{message!r} looks like a value: is the dictionary inverted?")
            if norm_wrong == right:
                raise ValueError(f"Ex {ex_id}: mistake {message!r} equals the right answer")
            entry["mistakes"][_hash(ex_id, kind, norm_wrong)] = message
    return entry


def _classic(entry: dict, digest: str) -> str | None:
    message = entry.get("mistakes", {}).get(digest)
    return f"Erreur classique : {message}" if message else None


def check_math_entry(ex_id: str, entry: dict, value) -> tuple[bool, str, str]:
    """Compare ``value`` with a fraction, expression or interval entry: (passed, status, message)."""
    from wbm.checker import _praise

    kind = entry["kind"]
    try:
        if kind == "fraction":
            return _check_fraction(ex_id, entry, value)
        if kind == "expr":
            return _check_expr(ex_id, entry, value)
        if kind == "interval":
            norm = _norm_intervals(_parse_intervals(value))
            digest = _hash(ex_id, kind, norm)
            if digest == entry["hash"]:
                return True, "ok", _praise(ex_id)
            classic = _classic(entry, digest)
            if classic:
                return False, "wrong", classic
            return False, "wrong", ("Ce n'est pas le bon ensemble : vérifie les bornes, puis chaque crochet "
                                    "(la borne est-elle atteinte ?).")
    except MathNormalizationError as exc:
        return False, "type", f"j'attendais {exc}."
    raise ValueError(f"unknown math kind: {kind!r}")


def _decimals_typed(value) -> int | None:
    """Number of decimals of a decimal number typed as a float or a text ("0,2857" -> 4); None otherwise."""
    if isinstance(value, bool) or isinstance(value, (numbers.Integral, Fraction)):
        return None
    if isinstance(value, numbers.Real):
        text = repr(float(value))
    elif isinstance(value, str) and _DECIMAL_TEXT.fullmatch(_clean_text(value).replace(" ", "")):
        text = _clean_text(value).replace(" ", "").replace(",", ".")
    else:
        return None
    if "e" in text or "." not in text:
        return None
    return len(text.split(".")[1])


def _approximates_answer(ex_id: str, entry: dict, x: float, decimals: int) -> bool:
    """Is ``x`` the right fraction rounded to ``decimals`` decimals (denominators up to 1000)?"""
    tolerance = 0.5 * 10.0 ** -decimals + 1e-12
    for denominator in range(1, 1001):
        candidate = Fraction(round(x * denominator), denominator)
        if abs(float(candidate) - x) <= tolerance and candidate.denominator == denominator and \
                _hash(ex_id, "fraction", _norm_fraction(candidate)) == entry["hash"]:
            return True
    return False


_APPROXIMATE = ("C'est une valeur approchée de la bonne réponse : donne la valeur exacte, sous forme de fraction "
                "(texte comme \"2/7\").")


def _check_fraction(ex_id: str, entry: dict, value) -> tuple[bool, str, str]:
    from wbm.checker import _praise

    try:
        q, irreducible = _parse_fraction(value)
    except _IrrationalValue:
        return False, "wrong", ("Ce n'est pas la bonne valeur : la réponse attendue est une fraction (un nombre "
                                "rationnel), et ta valeur n'en est pas une. Relis ce que la question demande.")
    except _ApproximateValue as exc:
        if _approximates_answer(ex_id, entry, exc.x, min(_decimals_typed(value) or 12, 12)):
            return False, "near", _APPROXIMATE
        return False, "wrong", ("Ce n'est pas la bonne valeur ; et donne la valeur exacte, sous forme de fraction "
                                "(texte comme \"2/7\"), pas une valeur approchée.")
    digest = _hash(ex_id, "fraction", _norm_fraction(q))
    if digest == entry["hash"]:
        if entry.get("simplified") and irreducible is False:
            return False, "near", "La valeur est juste, mais la fraction n'est pas irréductible : simplifie-la."
        return True, "ok", _praise(ex_id)
    classic = _classic(entry, digest)
    if classic:
        return False, "wrong", classic
    decimals = _decimals_typed(value)
    if decimals is not None and _approximates_answer(ex_id, entry, float(q), decimals):
        return False, "near", _APPROXIMATE
    if q != 0 and _hash(ex_id, "fraction", _norm_fraction(-q)) == entry["hash"]:
        return False, "wrong", "La valeur absolue est bonne, mais le signe est inversé."
    if q != 0 and _hash(ex_id, "fraction", _norm_fraction(1 / q)) == entry["hash"]:
        return False, "wrong", "Ta fraction est à l'envers : échange le numérateur et le dénominateur."
    return False, "wrong", "Ce n'est pas la bonne valeur : reprends le calcul étape par étape."


def _check_expr(ex_id: str, entry: dict, value) -> tuple[bool, str, str]:
    from wbm.checker import _praise

    variables = entry["variables"]
    points = [tuple(p) for p in entry["points"]]
    up_to_constant = bool(entry.get("up_to_constant"))
    expr = parse_expression(value, variables)
    fingerprint = _fingerprint(expr, variables, points, up_to_constant)
    if fingerprint is None:
        return False, "wrong", ("Ton expression n'est pas définie (ou pas réelle) en certains points où la bonne "
                                "réponse l'est : vérifie les racines, les logarithmes et les divisions.")
    digest = _expr_hash(ex_id, fingerprint)
    if digest == entry["hash"]:
        return True, "ok", _praise(ex_id)
    classic = _classic(entry, digest)
    if classic:
        return False, "wrong", classic
    for factor, message in ((-1, "Presque : tout le signe est inversé."),
                            (2, "Presque : il manque un facteur 2."),
                            (Fraction(1, 2), "Presque : il y a un facteur 2 de trop.")):
        import sympy

        scaled = _fingerprint(sympy.Rational(factor) * expr, variables, points, up_to_constant)
        if scaled is not None and _expr_hash(ex_id, scaled) == entry["hash"]:
            return False, "wrong", message
    if not up_to_constant:
        for constant in (1, -1):  # a constant forgotten or added (a +1 dropped while differentiating...)
            shifted = _fingerprint(expr + constant, variables, points, False)
            if shifted is not None and _expr_hash(ex_id, shifted) == entry["hash"]:
                return False, "wrong", "Presque : ton expression diffère de la bonne d'une constante (±1)."
    hint = "à une constante près, " if up_to_constant else ""
    return False, "wrong", (f"Ce n'est pas la bonne expression ({hint}elle ne prend pas les bonnes valeurs) : "
                            "reprends le calcul, ou vérifie-le avec SymPy.")


def perturbed(value, entry: dict):
    """A value that must be rejected (used by ``record`` to prove the check can fail)."""
    kind = entry["kind"]
    if kind == "fraction":
        q, _ = _parse_fraction(value)
        return _norm_fraction(q + 1)
    if kind == "expr":
        expr = parse_expression(value, entry["variables"])
        import sympy

        bump = sympy.Symbol(entry["variables"][0]) if entry.get("up_to_constant") else sympy.Integer(3)
        return expr + bump
    if kind == "interval":
        return "[1000 ; 1001]"
    raise ValueError(kind)
