"""Tests of the maths answer kinds of wbm.check: fractions, expressions, intervals (BIBLE §14)."""

import json
from fractions import Fraction

import pytest

import wbm
from wbm import checker
from wbm.mathcheck import parse_expression


def entry_of(ex_id, value, **kwargs):
    return checker.make_entry(ex_id, value, **kwargs)


def verdict(ex_id, entry, value):
    passed, status, message = checker.check_entry(ex_id, entry, value)
    return passed, status, message


# ------------------------------------------------------------------ fraction
@pytest.mark.parametrize("value", ["3/4", " 3 / 4 ", "6/8", "(3)/(4)", "0.75", "0,75", 0.75, Fraction(3, 4),
                                   "−3/−4"])
def test_fraction_accepts_every_writing_of_the_value(value):
    entry = entry_of("F.1", Fraction(3, 4), kind="fraction")
    assert verdict("F.1", entry, value)[0], value


def test_fraction_simplified_refuses_a_reducible_fraction_with_a_dedicated_message():
    entry = entry_of("F.2", Fraction(3, 4), kind="fraction", simplified=True)
    passed, status, message = verdict("F.2", entry, "6/8")
    assert not passed and status == "near" and "irréductible" in message
    assert verdict("F.2", entry, "3/4")[0]


@pytest.mark.parametrize("value, words", [
    ("-3/4", "signe"), ("4/3", "à l'envers"), (0.2857, None), ("1/2", "reprends le calcul"), ("abc", "J'attendais"),
])
def test_fraction_diagnoses(value, words):
    entry = entry_of("F.3", Fraction(3, 4), kind="fraction")
    passed, _, message = verdict("F.3", entry, value)
    assert not passed
    if words:
        assert words in message, message


@pytest.mark.parametrize("value", [0.2857, "0,2857", 0.285714285714])
def test_fraction_a_decimal_approximation_is_named_as_such(value):
    entry = entry_of("F.4", Fraction(2, 7), kind="fraction")
    passed, status, message = verdict("F.4", entry, value)
    assert not passed and status == "near" and "valeur approchée" in message, message


def test_fraction_classic_mistake():
    entry = entry_of("F.5", Fraction(3, 4), kind="fraction", mistakes={"tu as additionné les dénominateurs": "3/8"})
    passed, _, message = verdict("F.5", entry, "3/8")
    assert not passed and message == "Erreur classique : tu as additionné les dénominateurs"


def test_fraction_entry_stores_no_clear_value():
    entry = entry_of("F.6", Fraction(37, 91), kind="fraction")
    assert set(entry) == {"kind", "hash", "sign"}, entry
    assert "37/91" not in json.dumps(entry)


# ------------------------------------------------------------------ expr
@pytest.mark.parametrize("value", ["2*x*exp(x**2)", "2x e^(x^2)", "exp(x²)*x*2", "2·x·e^(x²)", "x*exp(x**2)*2",
                                   "2*x*exp(x)**x"])
def test_expression_equivalent_forms_pass(value):
    entry = entry_of("E.1", "2*x*exp(x**2)", kind="expr", variables=("x",))
    assert verdict("E.1", entry, value)[0], value


@pytest.mark.parametrize("value, words", [
    ("-2*x*exp(x**2)", "signe"), ("x*exp(x**2)", "il manque un facteur 2"), ("4*x*exp(x**2)", "facteur 2 de trop"),
    ("2*x*exp(x**2) + 1", "constante"), ("exp(x**2)", "pas la bonne expression"),
    ("2*y*exp(y**2)", "contient aussi : y"), ("2*x*exp(x**2", "je n'arrive pas à lire"),
])
def test_expression_diagnoses(value, words):
    entry = entry_of("E.2", "2*x*exp(x**2)", kind="expr", variables=("x",))
    passed, _, message = verdict("E.2", entry, value)
    assert not passed and words in message, message


def test_expression_up_to_a_constant():
    entry = entry_of("E.3", "x**3/3 + ln(x)", kind="expr", variables=("x",), up_to_constant=True)
    for value in ("x**3/3 + log(x)", "x^3/3 + ln(x) + 7", "(x**3 + 3*ln(x) - 2)/3"):
        assert verdict("E.3", entry, value)[0], value
    assert not verdict("E.3", entry, "x**3 + ln(x)")[0]


def test_expression_undefined_where_the_answer_is_defined():
    entry = entry_of("E.4", "x**2", kind="expr", variables=("x",))
    passed, _, message = verdict("E.4", entry, "x**2 + ln(-abs(x))")
    assert not passed and "pas définie" in message, message


def test_expression_of_two_variables():
    entry = entry_of("E.5", "x*y**2 + sin(x)", kind="expr", variables=("x", "y"))
    assert verdict("E.5", entry, "y^2 x + sin(x)")[0]
    assert not verdict("E.5", entry, "x*y**2 + cos(x)")[0]


def test_expression_entry_stores_points_but_not_the_expression():
    entry = entry_of("E.6", "3*x**2 + 7*x", kind="expr", variables=("x",))
    assert set(entry) == {"kind", "hash", "variables", "points"}, entry
    assert entry["variables"] == ["x"]
    assert len(entry["points"]) >= 3


def test_expression_classic_mistake():
    entry = entry_of("E.7", "cos(x)", kind="expr", variables=("x",),
                     mistakes={"la dérivée de sin est cos, pas -cos": "-cos(x)"})
    passed, _, message = verdict("E.7", entry, "-cos(x)")
    assert not passed and message.startswith("Erreur classique : la dérivée de sin")


def test_expression_needs_variables():
    with pytest.raises(ValueError, match="variables"):
        entry_of("E.8", "x**2", kind="expr")


def test_parse_expression_reads_e_as_euler_unless_it_is_a_variable():
    import sympy

    assert parse_expression("e^x", ["x"]) == sympy.exp(sympy.Symbol("x"))
    assert parse_expression("e*x", ["e", "x"]) == sympy.Symbol("e") * sympy.Symbol("x")


# ------------------------------------------------------------------ interval
@pytest.mark.parametrize("value", ["]-oo ; 3] U [5 ; +oo[", "]−∞ ; 3] ∪ [5 ; +∞[", "(-oo, 3] U [5, +oo)",
                                   "[5;+oo[ U ]-oo;3]"])
def test_interval_writings(value):
    entry = entry_of("I.1", "]-oo ; 3] U [5 ; +oo[", kind="interval")
    assert verdict("I.1", entry, value)[0], value


def test_interval_reads_the_reals_minus_a_few_points():
    entry = entry_of("I.9", "]-oo ; -1[ U ]-1 ; 2[ U ]2 ; +oo[", kind="interval")
    for value in ("R \\ {-1 ; 2}", "ℝ∖{2, -1}", "R privé de {-1; 2}", "]-oo ; -1[ U ]-1 ; 2[ U ]2 ; +oo["):
        assert verdict("I.9", entry, value)[0], value
    assert not verdict("I.9", entry, "R \\ {-1}")[0]


def test_expression_reads_absolute_value_bars():
    entry = entry_of("E.abs", "Abs(x - 1) + Abs(x + 1)", kind="expr", variables=("x",))
    for value in ("|x - 1| + |x + 1|", "abs(x-1)+abs(x+1)", "Abs(x+1) + |x-1|"):
        assert verdict("E.abs", entry, value)[0], value
    assert not verdict("E.abs", entry, "|x - 1| + |x - 1|")[0]


def test_interval_reads_decimal_commas_the_whole_line_and_the_empty_set():
    entry = entry_of("I.5", "]-2.5 ; +oo[", kind="interval")
    for value in ("]-2,5 ; +oo[", "]-2,5;+oo[", "]-2.5 ; +oo["):
        assert verdict("I.5", entry, value)[0], value
    entry = entry_of("I.6", "]-oo ; +oo[", kind="interval")
    assert verdict("I.6", entry, "R")[0] and verdict("I.6", entry, "ℝ")[0]
    entry = entry_of("I.7", "vide", kind="interval")
    for value in ("Ø", "∅", [], "vide"):
        assert verdict("I.7", entry, value)[0], value
    entry = entry_of("I.8", "]-oo ; -2[ U [3 ; +oo[", kind="interval")
    assert verdict("I.8", entry, "]-oo ; -2[ ou [3 ; +oo[")[0]
    passed, status, message = verdict("I.8", entry, "]-oo ; -2[ et [3 ; +oo[")
    assert not passed and "intersection" in message and "-2[" not in message


def test_interval_with_exact_endpoints_and_sympy_sets():
    import sympy

    entry = entry_of("I.2", "[1/2 ; sqrt(2)[", kind="interval")
    assert verdict("I.2", entry, "[0.5 ; sqrt(2)[")[0]
    assert verdict("I.2", entry, sympy.Interval.Ropen(sympy.Rational(1, 2), sympy.sqrt(2)))[0]
    assert not verdict("I.2", entry, "[1/2 ; sqrt(2)]")[0]


@pytest.mark.parametrize("value, words", [
    ("]-oo ; 3] U [5 ; +oo]", "infini"), ("[5 ; 3]", "dans l'ordre"), ("n'importe quoi", "J'attendais"),
    ("[1 ; 2]", "bon ensemble"),
])
def test_interval_diagnoses(value, words):
    entry = entry_of("I.3", "]-oo ; 3] U [5 ; +oo[", kind="interval")
    passed, _, message = verdict("I.3", entry, value)
    assert not passed and words in message, message


def test_empty_set():
    entry = entry_of("I.4", "∅", kind="interval")
    assert verdict("I.4", entry, "vide")[0] and not verdict("I.4", entry, "[0 ; 1]")[0]


# ------------------------------------------------------------------ record / check round trip
def test_record_then_check_for_each_math_kind(capsys):
    wbm.record("R.1", Fraction(5, 6), kind="fraction")
    wbm.record("R.2", "sin(x)/x", kind="expr", variables=("x",))
    wbm.record("R.3", "[0 ; 1[", kind="interval")
    capsys.readouterr()
    assert wbm.check("R.1", "10/12", quiet=True)
    assert wbm.check("R.2", "sin(x) * x**-1", quiet=True)
    assert wbm.check("R.3", "[0, 1)", quiet=True)
    assert not wbm.check("R.3", "[0, 1]", quiet=True)


def test_record_refuses_math_options_without_a_math_kind():
    with pytest.raises(ValueError, match="kind"):
        checker.make_entry("R.4", 3, variables=("x",))


def test_infer_kind_of_a_fraction():
    assert checker.infer_kind(Fraction(1, 3)) == "fraction"


# ------------------------------------------------------------------ writings found by the POS learner run (session 4)
@pytest.mark.parametrize("value", [(0, 75), (-0, 5)])
def test_fraction_a_decimal_comma_without_quotes_is_named(value):
    entry = entry_of("F.6", Fraction(3, 4), kind="fraction")
    passed, status, message = verdict("F.6", entry, value)
    assert not passed and status == "type" and "avec un point" in message and "(0, 5)" in message, message
    assert "3/5" in message, message   # a pair (numerator, denominator) is answered too


@pytest.mark.parametrize("value", ["sqrt(3)/2", "√3/2", "pi/4"])
def test_fraction_an_irrational_value_is_a_wrong_value_not_a_wrong_form(value):
    entry = entry_of("F.7", Fraction(1, 2), kind="fraction")
    passed, status, message = verdict("F.7", entry, value)
    assert not passed and status == "wrong" and "rationnel" in message, message


def test_fraction_an_exact_rational_expression_is_read():
    entry = entry_of("F.8", Fraction(3, 4), kind="fraction")
    assert verdict("F.8", entry, "(1 + 2)/4")[0]


@pytest.mark.parametrize("value", ["10x⁴ - 6x", "10*x**4 - 6*x", "f'(x) = 10x^4 - 6x", "y = 10x^4 - 6x",
                                   "10 x⁴ − 6 x"])
def test_expr_superscripts_and_a_name_prefix(value):
    entry = entry_of("X.20", "10*x**4 - 6*x", kind="expr", variables=("x",))
    assert verdict("X.20", entry, value)[0], value


@pytest.mark.parametrize("value", ["ln5", "Ln(5)", "LN 5", "log(5)"])
def test_expr_function_names_without_parentheses_or_in_capitals(value):
    entry = entry_of("X.21", "ln(5)", kind="expr", variables=("x",))
    assert verdict("X.21", entry, value)[0], value


def test_expr_superscript_with_several_digits_and_a_minus():
    entry = entry_of("X.22", "x**10 + x**(-1)", kind="expr", variables=("x",))
    assert verdict("X.22", entry, "x¹⁰ + x⁻¹")[0]


@pytest.mark.parametrize("value", ["]-OO ; 2]", "]-Inf ; 2]", "]-INFINI ; 2]"])
def test_interval_infinity_in_capitals(value):
    entry = entry_of("I.20", "]-oo ; 2]", kind="interval")
    assert verdict("I.20", entry, value)[0], value


# ------------------------------------------------------------------ R3: learner simulation
def test_fraction_reads_a_decimal_without_leading_zero():
    e = entry_of("t3.m1", "9/20", kind="fraction")
    assert verdict("t3.m1", e, ".45")[0] and verdict("t3.m1", e, "0,45")[0]
    assert "rationnel" not in verdict("t3.m1", e, "-.8")[2]


def test_fraction_typed_as_a_python_calculation_finds_the_recorded_mistake():
    e = entry_of("t3.m2", "9/20", kind="fraction", mistakes={"retire le minimum avant de diviser": "13/24"})
    assert "retire le minimum" in verdict("t3.m2", e, 65 / 120)[2]


def test_interval_with_a_rounded_endpoint_is_named_as_such():
    e = entry_of("t3.m3", "]-1/3 ; 2[", kind="interval")
    for rounded in ("]-0.33 ; 2[", "]-0,333 ; 2["):
        passed, status, message = verdict("t3.m3", e, rounded)
        assert not passed and status == "near" and "arrondie" in message
    assert "arrondie" not in verdict("t3.m3", e, "]-0.34 ; 2[")[2]


def test_fraction_prediction_gets_no_hint_about_its_sign():
    e = entry_of("t3.m4", "3/2", kind="fraction", prediction=True)
    assert verdict("t3.m4", e, "-3/2")[2].startswith("Prédiction ratée")


def test_fraction_typed_as_a_python_calculation_is_exact():
    """2/7 typed without quotes is the float nearest to 2/7: the learner typed the fraction (R4)."""
    entry = entry_of("F.4b", Fraction(2, 7), kind="fraction")
    assert verdict("F.4b", entry, 2 / 7)[0]
    assert not verdict("F.4b", entry, 0.2857142857)[0]


@pytest.mark.parametrize("value", [0.3 / 0.7, "0.3/0.7", "0.3 / (1 - 0.3)", "3/7"])
def test_fraction_calculated_from_decimals_is_exact(value):
    """0.3/0.7 is a few units of the last place away from the float nearest to 3/7; "0.3/0.7" is read exactly (R5)."""
    entry = entry_of("F.4c", Fraction(3, 7), kind="fraction")
    assert verdict("F.4c", entry, value)[0], verdict("F.4c", entry, value)[2]
    assert not verdict("F.4c", entry, 0.4285714286)[0]


def test_pi_glued_to_letters_is_read_as_a_factor():
    """Session 11 (R7): « 2πrh » typed with the π key is 2·π·r·h, like « 2*pi*r*h »."""
    entry = entry_of("E.40", "2*pi*r*h", kind="expr", variables=("r", "h"))
    for value in ("2πrh", "2π r h", "2*π*r*h", "2*pi*r*h"):
        assert verdict("E.40", entry, value)[0], value
    assert not verdict("E.40", entry, "πr²")[0]
