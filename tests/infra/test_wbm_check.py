"""Tests of wbm.check / wbm.record: right values pass, wrong values fail, no leak."""

import json
import math

import numpy as np
import pytest

import wbm
from wbm import checker as C


def entry(ex_id, value, **kwargs):
    return C.make_entry(ex_id, value, **kwargs)


def passes(ex_id, e, value):
    return C.check_entry(ex_id, e, value)[0]


def message(ex_id, e, value):
    return C.check_entry(ex_id, e, value)[2]


# ---------------------------------------------------------------- floats
def test_float_right_value_and_rounding_variants_pass():
    e = entry("x.1", 3.14159, decimals=2)
    for v in (3.14159, 3.14, 3.1449, "3.14", "3,14", np.float32(3.14159)):
        assert passes("x.1", e, v), v


def test_float_wrong_values_fail():
    e = entry("x.1", 3.14159, decimals=2)
    for v in (3.16, 3.0, -3.14, 31.4, 0.0):
        assert not passes("x.1", e, v), v


def test_float_boundary_tolerance():
    e = entry("x.2", 0.125000001, decimals=2)  # stored as "0.13"
    assert passes("x.2", e, 0.124999999)


def test_hash_never_contains_the_value():
    e = entry("x.3", 42.4242, decimals=4)
    dumped = json.dumps(e)
    assert "42.42" not in dumped and "42.4242" not in dumped


def test_decimals_required_for_floats():
    with pytest.raises(ValueError):
        entry("x.4", 1.5)


def test_same_value_different_ids_give_different_hashes():
    assert entry("a.1", 7)["hash"] != entry("a.2", 7)["hash"]


# ---------------------------------------------------------------- diagnostics
@pytest.mark.parametrize(
    "value, expected_fragment",
    [
        (-3.14159, "signe"),
        (314.159, "proportion"),
        (0.0314159, "pourcentage"),
        (3.2, "ordre de grandeur est bon"),
        (31.0, "trop grande"),
        (0.2, "trop petite"),
    ],
)
def test_float_diagnostics(value, expected_fragment):
    e = entry("d.1", 3.14159, decimals=2)
    assert expected_fragment in message("d.1", e, value)


def test_complement_and_coarse_diagnostics():
    e = entry("d.2", 0.25, decimals=2)
    assert "complément" in message("d.2", e, 0.75)
    e = entry("d.3", 0.123, decimals=3)
    assert "presque" in message("d.3", e, 0.12)


def test_int_off_by_one_and_type():
    e = entry("d.4", 344)
    assert passes("d.4", e, 344.0)
    assert "à 1 près" in message("d.4", e, 345)
    assert "entier" in message("d.4", e, 12.5)



def test_int_non_integer_number_is_a_wrong_value_not_a_wrong_type():
    e = entry("d.4b", 0)
    assert passes("d.4b", e, 0.0)
    ok, status, text = C.check_entry("d.4b", e, 0.5)
    assert not ok and status == "wrong" and "entier" in text
    assert C.check_entry("d.4b", e, "abc")[1] == "type"


@pytest.mark.parametrize(
    "value, fragment, factor_claimed",
    [
        (11, "trop grande", False),     # 9 -> 11: one power of ten apart, but only 1.2 times too big
        (100, "trop grande", True),     # two powers of ten apart: at least a factor 10
        (1, "ordre de grandeur est bon", False),
    ],
)
def test_magnitude_messages_claim_a_factor_10_only_when_true(value, fragment, factor_claimed):
    e = entry("d.4c", 9)
    text = message("d.4c", e, value)
    assert fragment in text
    assert ("facteur 10" in text) is factor_claimed


def test_magnitude_messages_for_too_small_values():
    e = entry("d.4d", 12.0, decimals=1)
    assert "facteur 10" not in message("d.4d", e, 9.0) and "trop petite" in message("d.4d", e, 9.0)
    assert "facteur 10" in message("d.4d", e, 0.5)


def test_integer_arrays_accept_integers_computed_in_floating_point():
    e = entry("d.4e", [-1, 3])
    assert passes("d.4e", e, [-0.9999999999999998, 3.0000000000000004])   # np.roots, a grid read-out...
    ok, status, text = C.check_entry("d.4e", e, [-0.9, 3.2])
    assert not ok and "entiers" in text and "round" not in text      # far from integers: rounding would not help


def test_angles_in_radians_where_degrees_are_asked():
    """2.356 or "3*pi/4" for 135°, [1.57, 4.71] for [90, 270], 30 for 0.5236 rad (session 14, R9 learner C4)."""
    e = entry("d.4r", 135)
    for value in (2.356, 2.3562, "3*pi/4"):
        assert "en radians" in C.check_entry("d.4r", e, value)[2]
    assert "en radians" not in C.check_entry("d.4r", e, 2.0)[2]
    e = entry("d.4s", 77.47, decimals=1)
    assert "en radians" in C.check_entry("d.4s", e, 1.3521)[2]
    e = entry("d.4t", [90, 270])
    assert "en radians" in C.check_entry("d.4t", e, [1.57, 4.71])[2]
    e = entry("d.4u", 0.5236, decimals=4)
    assert "en degrés" in C.check_entry("d.4u", e, 30)[2]
    e = entry("d.4p", 0.026, decimals=4)          # a p-value, not an angle: 0.000454 rad is 0.026° (session 28)
    assert "radians" not in C.check_entry("d.4p", e, 0.000454, computed=True)[2]
    assert "radians" not in C.check_entry("d.4p", e, 0.000454)[2]


def test_an_equation_typed_where_its_coefficients_are_asked():
    e = entry("d.4v", [3, 2, -4])
    assert "[a, b, c]" in C.check_entry("d.4v", e, "3x + 2y - 4 = 0")[2]

def test_integer_arrays_accept_bytes_and_bytearray():
    e = entry("d.4f", [0xC3, 0xAB], mistakes={"le premier octet commence par 110": [0x03, 0xAB]})
    for v in ("ë".encode("utf-8"), b"\xc3\xab", bytearray(b"\xc3\xab"), memoryview(b"\xc3\xab")):
        assert passes("d.4f", e, v), v
    assert not passes("d.4f", e, b"\xab\xc3")
    assert "110" in message("d.4f", e, b"\x03\xab")      # a classic mistake typed as bytes is still recognised
    assert not passes("d.4f", e, "ë")              # a str is not its bytes


def test_common_mistakes_are_reported():
    e = entry("d.5", 10.0, decimals=1, mistakes={"somme au lieu de moyenne": 50.0})
    assert "somme au lieu de moyenne" in message("d.5", e, 50.0)
    with pytest.raises(ValueError):
        entry("d.6", 10.0, decimals=1, mistakes={"identique": 10.0})


def test_a_mistake_at_a_rounding_boundary_gets_both_roundings():
    """5/8 at 2 decimals is formatted 0.62, the school rounding gives 0.63: both read the classic mistake (M04.4f)."""
    e = entry("d.6b", 1.6, decimals=2, mistakes={"la durée moyenne est l'inverse du taux": 5 / 8})
    for typed in (0.62, 0.63):
        assert "la durée moyenne est l'inverse du taux" in message("d.6b", e, typed)
    # the other rounding is never the right answer, and a real mistake on it keeps its own message
    e = entry("d.6c", 0.63, decimals=2, mistakes={"un arrondi trop tôt": 0.625})
    assert passes("d.6c", e, 0.63) and "un arrondi trop tôt" in message("d.6c", e, 0.62)
    e = entry("d.6d", 2.0, decimals=2, mistakes={"première erreur classique": 0.625, "seconde erreur classique": 0.63})
    assert "première erreur classique" in message("d.6d", e, 0.62)
    assert "seconde erreur classique" in message("d.6d", e, 0.63)


def test_a_missed_prediction_is_not_called_a_classic_mistake():
    """The prediction of a 🔮 (prediction=True): its wrong value says « Prédiction ratée », with the same hint."""
    e = entry("d.7", False, mistakes={"relis la dernière ligne du tableau": True}, prediction=True)
    assert e["prediction"] is True and passes("d.7", e, False)
    text = message("d.7", e, True)
    assert text.startswith("Prédiction ratée (tu as prédit « True »). Piste : relis la dernière ligne")
    assert "Erreur classique" not in text
    plain = entry("d.8", False, mistakes={"relis la dernière ligne du tableau": True})
    assert "prediction" not in plain and message("d.8", plain, True).startswith("Erreur classique. Piste : relis")


def test_a_missed_choice_prediction_recalls_the_letter_before_the_hint():
    """« Piste : « B » : lis… » read as « the hint is B »: the lead says what was predicted, the hint has no letter."""
    e = entry("d.7b", "C", mistakes={"lis la part des courbes sous la figure": {"A", "B", "D"}}, prediction=True)
    for letter in "ABD":
        assert message("d.7b", e, letter) == ("Prédiction ratée (tu as prédit « " + letter + " »). Piste : lis la part "
                                              "des courbes sous la figure.")
    assert passes("d.7b", e, "C") and passes("d.7b", e, "c")


def test_a_set_of_wrong_values_shares_one_message():
    e = entry("d.7c", 3, mistakes={"compte les cases du tableau": {1, 2}, "relis la question": 4})
    assert "compte les cases" in message("d.7c", e, 1) and "compte les cases" in message("d.7c", e, 2)
    assert "relis la question" in message("d.7c", e, 4)
    with pytest.raises(ValueError, match="equals the right answer"):
        entry("d.7d", "C", mistakes={"lis la figure": {"A", "C"}})
    with pytest.raises(ValueError, match="give the same value"):
        entry("d.7e", "C", mistakes={"lis la figure": {"A", "B"}, "relis la question": "B"})


# ---------------------------------------------------------------- other kinds
def test_strings_ignore_case_accents_and_spaces():
    e = entry("s.1", "Rétropropagation du gradient")
    for v in ("retropropagation du gradient", "RÉTROPROPAGATIONDUGRADIENT", " rétro propagation du gradient "):
        assert passes("s.1", e, v)
    assert not passes("s.1", e, "backprop")
    assert "chaîne" in message("s.1", e, 3)


def test_an_einsum_formula_keeps_its_arrow():
    e = entry("s.2", "ij,ji->")
    for v in ("ij,ji->", " ij, ji -> ", "IJ,JI->", "ij,ji→"):
        assert passes("s.2", e, v), v
    for v in ("ij,j->i", "ij,ji", "i->j,ji"):
        assert not passes("s.2", e, v), v


def test_a_number_given_for_a_shape_text_gets_the_trailing_comma_hint():
    e = entry("s.3", "(3,)")
    assert passes("s.3", e, (3,)) and passes("s.3", e, "(3,)")
    assert "(3,)" in message("s.3", e, 3) and "virgule" in message("s.3", e, 3)


def test_booleans_accept_french_words():
    e = entry("b.1", True)
    assert passes("b.1", e, "vrai") and passes("b.1", e, "Oui") and passes("b.1", e, 1)
    assert passes("b.1", e, "V") and passes("b.1", e, "T") and not passes("b.1", e, "F")   # abbreviations on a sheet
    assert not passes("b.1", e, False)


def test_arrays_shape_values_and_diagnostics():
    value = np.array([[1.5, 2.25], [3.0, 4.125]])
    e = entry("r.1", value, decimals=3)
    assert passes("r.1", e, value.tolist())
    assert "transposé" in message("r.1", e, value.T + 0) or "élément" in message("r.1", e, value.T)
    assert "reshape" in message("r.1", e, value.ravel())
    assert "3 éléments sur 4" in message("r.1", e, [[1.5, 2.25], [3.0, 9.0]])
    assert "Forme attendue" in message("r.1", e, np.zeros((3, 2)))


def test_array_with_every_sign_inverted_is_diagnosed_before_the_element_count():
    value = np.array([-3.578, -0.894, 0.0, 1.789, 2.683])     # coordinates on u; -u flips every non-zero one
    e = entry("r.5", value, decimals=3)
    assert message("r.5", e, (-value).tolist()) == "Tous les signes sont inversés."
    assert message("r.5", e, [-2, -200]).startswith("Ta liste a 2 éléments, il en faut 5")
    e = entry("r.6", [2, 200])
    assert message("r.6", e, [-2, -200]) == "Tous les signes sont inversés."
    assert "1 élément sur 2" in message("r.6", e, [2, -200])           # one sign only: the element count


def test_transposed_rectangular_array():
    value = np.arange(6.0).reshape(2, 3)
    e = entry("r.2", value, decimals=1)
    assert "transposé" in message("r.2", e, value.T)


def test_integer_arrays_need_no_decimals():
    e = entry("r.3", [1, 2, 3])
    assert passes("r.3", e, np.array([1, 2, 3]))
    with pytest.raises(ValueError):
        entry("r.4", [0.5, 1.5])


def test_sets_ignore_order():
    e = entry("t.1", ["b", "a", "c"], ordered=False)
    assert passes("t.1", e, {"a", "b", "c"})
    assert not passes("t.1", e, ["a", "b"])


def test_torch_tensor_accepted():
    torch = pytest.importorskip("torch")
    e = entry("r.5", [0.5, 0.25], decimals=2)
    assert passes("r.5", e, torch.tensor([0.5, 0.25]))
    e = entry("r.6", 2.5, decimals=1)
    assert passes("r.6", e, torch.tensor(2.5))


# ---------------------------------------------------------------- public API
def test_record_then_check_roundtrip(capsys):
    wbm.record("rt.1", 0.8123, decimals=3)
    out = capsys.readouterr().out
    assert out.startswith(C.ANSWER_PREFIX)
    assert "0.812" not in out
    assert wbm.check("rt.1", 0.8123)
    assert not wbm.check("rt.1", 0.7)
    assert "✅" in capsys.readouterr().out


def test_record_with_one_decimal():
    # 1 decimal on a value with digits: fine; a wrong value must be rejected
    wbm.record("rt.2", 12.34, decimals=1)
    assert not wbm.check("rt.2", 12.6, quiet=True)


def test_pending_and_unknown(capsys):
    assert wbm.check("rt.3", ...).status == "pending"
    assert wbm.check("rt.3", None).status == "pending"
    assert wbm.check("does.not.exist", 1).status == "unknown"
    out = capsys.readouterr().out
    assert "⏳" in out and "❓" in out


def test_a_function_without_return_is_wrong_not_pending(capsys):
    # computed=True: the value comes from the learner's function; None means a forgotten `return`
    result = wbm.check("rt.3", None, computed=True)
    assert result.status == "wrong" and not result
    out = capsys.readouterr().out
    assert "❌" in out and "return" in out
    # a typed answer left as None stays pending, and the message mentions the forgotten return too
    assert wbm.check("rt.3", None).status == "pending"
    assert "return" in capsys.readouterr().out
    # `...` is only a placeholder: no word about functions
    assert wbm.check("rt.3", ...).status == "pending"
    assert "return" not in capsys.readouterr().out


def test_check_reads_answers_file(tmp_path):
    e = entry("f.1", 17)
    path = tmp_path / "answers.json"
    path.write_text(json.dumps({"_meta": {}, "answers": {"f.1": e}}))
    assert wbm.check("f.1", 17, answers_path=path, quiet=True)
    assert not wbm.check("f.1", 18, answers_path=path, quiet=True)


def test_decimals_argument_mismatch_is_harmless(capsys):
    wbm.record("rt.4", 2.71828, decimals=3)
    assert wbm.check("rt.4", 2.71828, decimals=2)
    assert "3 décimales" in capsys.readouterr().out


def test_check_result_displays_nothing():
    result = wbm.check("rt.3", ..., quiet=True)
    assert result._ipython_display_() is None
    assert "pending" in repr(result)


def test_record_returns_a_dict_that_displays_nothing(capsys):
    # the last line of an `answer` cell must not echo the entry (hash, mistakes) in the notebook
    recorded = wbm.record("rt.5", 3.14159, decimals=2)
    capsys.readouterr()
    assert isinstance(recorded, dict) and "hash" in json.dumps(recorded)
    assert recorded._ipython_display_() is None
    assert capsys.readouterr().out == ""


def test_attempt_catches_only_todo(capsys):
    with wbm.attempt("z.1"):
        raise NotImplementedError("todo")
    assert "⏳ Ex z.1" in capsys.readouterr().out
    with pytest.raises(ZeroDivisionError):
        with wbm.attempt("z.2"):
            1 / 0


def test_attempt_turns_a_forgotten_return_into_one_line(capsys):
    def no_return(values):
        sorted(values)                       # the learner forgot `return`

    with wbm.attempt("z.5"):
        first, second = no_return([2, 1])
    out = capsys.readouterr().out
    assert out.startswith("❌ Ex z.5 :") and "`return`" in out and "NoneType" in out, out
    with pytest.raises(TypeError):           # another TypeError is a real bug: its traceback stays
        with wbm.attempt("z.6"):
            len(5)


@pytest.mark.parametrize("message", [
    "'NoneType' object is not subscriptable", "cannot unpack non-iterable NoneType object",
    "unsupported operand type(s) for *: 'NoneType' and 'float'", "argument after * must be an iterable, not NoneType",
    "object of type 'NoneType' has no len()", "unsupported format string passed to NoneType.__format__",
])
def test_attempt_recognises_the_messages_of_a_none(capsys, message):
    with wbm.attempt("z.9"):
        raise TypeError(message)
    assert "oublié son `return`" in capsys.readouterr().out


def test_attempt_does_not_take_a_tensor_given_to_numpy_for_a_forgotten_return():
    """PyTorch's message names NoneType for its arguments: a real bug, not a None (audit P5 V-VI, A10 14)."""
    torch = pytest.importorskip("torch")
    with pytest.raises(TypeError, match="invalid combination of arguments"):
        with wbm.attempt("z.10"):
            np.mean(torch.ones(3))


def test_attempt_turns_an_attribute_of_none_into_one_line(capsys):
    class Scaler:
        def fit(self, X):
            self.mean_ = sum(X) / len(X)     # the learner forgot `return self`

        def transform(self, X):
            return [x - self.mean_ for x in X]

    with wbm.attempt("z.7"):
        Scaler().fit([1.0, 3.0]).transform([2.0])
    out = capsys.readouterr().out
    assert out.startswith("❌ Ex z.7 :") and "`return`" in out and "has no attribute 'transform'" in out, out
    with pytest.raises(AttributeError):      # another AttributeError is a real bug: its traceback stays
        with wbm.attempt("z.8"):
            [1, 2].shape


def test_attempt_catches_missing_mymath(capsys, tmp_path):
    placeholder = wbm.load_mymath("learner", path=tmp_path / "nothing", missing_ok=True)
    with wbm.attempt("z.3"):
        placeholder.metrics.f1([1], [1])
    assert "⏳ Ex z.3" in capsys.readouterr().out


# ---------------------------------------------------------------- regressions (independent review)
def test_integer_arrays_reject_probabilities():
    e = entry("g.1", [0, 1, 1, 0, 1])
    assert passes("g.1", e, np.array([0, 1, 1, 0, 1]))
    assert passes("g.1", e, [True, False, False, True, False]) is False
    assert not passes("g.1", e, [0.21, 0.74, 0.93, 0.08, 0.66])
    assert "entiers" in message("g.1", e, [0.21, 0.74, 0.93, 0.08, 0.66])


def test_sets_of_floats_need_decimals():
    with pytest.raises(ValueError):
        entry("g.2", [0.1, 0.2], ordered=False)
    e = entry("g.3", [0.1, 0.2], decimals=1, ordered=False)
    assert passes("g.3", e, {0.2, 0.1}) and not passes("g.3", e, [0.3, 0.4])
    assert "liste" in message("g.3", e, 5) and "crochets" in message("g.3", e, 5)


def test_torch_non_tensors_and_special_tensors():
    torch = pytest.importorskip("torch")
    e = entry("g.4", [3, 4])
    assert passes("g.4", e, torch.zeros(3, 4).shape)  # torch.Size is a tuple
    e = entry("g.5", 2.5, decimals=1)
    assert passes("g.5", e, torch.tensor(2.5, dtype=torch.bfloat16))
    e = entry("g.6", [1.0, 2.0], decimals=1)
    grad = [torch.tensor(1.0, requires_grad=True), torch.tensor(2.0, requires_grad=True)]
    assert passes("g.6", e, grad)
    ok, status, _ = C.check_entry("g.4", entry("g.4", [3, 4]), torch.float32)
    assert not ok and status == "type"


def test_float32_array_and_rounding_boundary():
    e = entry("g.7", [0.125, 1.0], decimals=2)
    assert passes("g.7", e, np.array([0.125, 1.0], dtype=np.float32))
    assert passes("g.7", e, [0.12500001, 1.0])
    e = entry("g.8", 0.125, decimals=2)  # exactly on a boundary: both roundings accepted
    assert passes("g.8", e, 0.13) and passes("g.8", e, 0.12) and passes("g.8", e, 0.125)
    assert not passes("g.8", e, 0.14)


def test_value_rounding_to_zero_is_refused():
    with pytest.raises(ValueError):
        entry("g.9", 0.00023, decimals=3)


def test_zero_nan_and_inf_hints_do_not_leak():
    e = entry("g.10", 0.0, decimals=1)
    assert "signe" not in message("g.10", e, 0.5) and "signe" not in message("g.10", e, -0.5)
    e = entry("g.11", 2.5, decimals=1)
    assert "NaN" in message("g.11", e, float("nan"))
    assert "infinie" in message("g.11", e, float("inf"))
    assert "signe" not in message("g.11", e, 0.0)


def test_unusual_inputs_do_not_crash():
    import pandas as pd

    e = entry("g.12", 3.5, decimals=1)
    assert "trop grand" in message("g.12", e, 2**1100)
    assert not passes("g.12", e, pd.NA)
    assert passes("g.12", e, pd.Series([3.5]))  # e.g. the result of .mode()
    e = entry("g.13", 2**60)
    assert passes("g.13", e, 2**60) and not passes("g.13", e, 2**60 + 1)
    e = entry("g.14", 1000.5, decimals=1)
    assert passes("g.14", e, "1 000,5") and passes("g.14", e, "1,000.5")
    e = entry("g.16", -0.25, decimals=2)
    assert passes("g.16", e, "\u22120,25") and passes("g.16", e, "-0,25")  # typographic minus sign


def test_string_normalisation_extensions():
    e = entry("g.15", "sur-apprentissage")
    for v in ("surapprentissage", "Sur apprentissage", "sur‑apprentissage"):
        assert passes("g.15", e, v), v
    e = entry("g.16", "l'œuvre d'art")
    assert passes("g.16", e, "l’oeuvre d’art")
    e = entry("g.17", "Gentoo")
    import pandas as pd

    assert passes("g.17", e, pd.Series(["Gentoo"]))


def test_a_choice_copied_with_brackets_or_punctuation_is_read_as_the_bare_choice():
    e = entry("g.18", "C", mistakes={"A n'est pas la bonne lettre, relis la définition": "A"})
    for v in ("(C)", "C)", "« C »", "c.", " (c) ", "[C]"):
        assert passes("g.18", e, v), v
    assert "Erreur classique" in message("g.18", e, "(A)")
    assert not passes("g.18", e, "(B)")
    assert not passes("g.18", e, "()")
    e = entry("g.19", "l'œuvre d'art")        # punctuation INSIDE a text answer still counts
    assert not passes("g.19", e, "l'œuvre, d'art")


def test_a_shape_or_position_written_another_way_is_read_as_its_tuple_text():
    e = entry("g.40", "(256, 28, 28)", mistakes={"les canaux d'abord": "(28, 28, 256)"})
    for v in ("(256, 28, 28)", "256, 28, 28", "[256, 28, 28]", "torch.Size([256, 28, 28])", "256 x 28 x 28",
              (256, 28, 28), [256, 28, 28]):
        assert passes("g.40", e, v), v
    assert "Erreur classique" in message("g.40", e, "[28, 28, 256]")
    assert "Erreur classique" in message("g.40", e, (28, 28, 256))
    assert not passes("g.40", e, "256")
    assert not passes("g.40", e, "(256, 56, 56)")
    e = entry("g.41", "(25088,)")
    for v in ("(25088,)", "[25088]", "25088,", (25088,)):
        assert passes("g.41", e, v), v
    e = entry("g.42", "(1, 2)")
    assert not passes("g.42", e, "12")         # a single number is not read as a shape
    e = entry("g.43", "1,2")                   # nor is a text answer without brackets turned into one
    assert passes("g.43", e, "1, 2")
    assert passes("g.40", entry("g.40", "(256, 28, 28)"), "256 28 28")     # numbers separated by spaces


def test_a_wrong_shape_gets_a_shape_hint_not_a_spelling_hint():
    e = entry("g.44", "(16, 3, 32, 32)")
    for v in ("(16, 32, 32, 3)", "16 32 32 3", (3, 32, 32)):
        text = message("g.44", e, v)
        assert "forme" in text and "orthographe" not in text, (v, text)
    assert "orthographe" in message("g.44", e, "seize")            # a text that is not a shape keeps the old hint


def test_several_choice_letters_in_another_order_or_with_separators_are_read_glued():
    e = entry("g.20", "BDE", mistakes={"il manque une lettre": "BD"})
    for v in ("BDE", "bde", "EDB", "E, D, B", "b, d, e", "B; D; E", "(B, D, E)", "D+B+E", "B D E", "B, D, D, E",
              "B, D et E", "E et D et B", "b, d ET e", "(B), (D), (E)", "(B) et (D) et (E)", "(B) (D) (E)",
              "(B)(D)(E)", "[B][D][E]"):
        assert passes("g.20", e, v), v
    assert "Erreur classique" in message("g.20", e, "D, B")      # the mistakes are read the same way
    for v in ("BD", "B, D, E, F", "ABDE", "B, DE", "B et D", "B, D et", "bdee", "bdd"):
        assert not passes("g.20", e, v), v
    assert "Erreur classique" in message("g.20", e, "B et D")


def test_several_choice_letters_glued_in_lower_case_and_another_order_are_read_as_letters():
    e = entry("g.27", "ACD", mistakes={"il manque au moins une lettre": {"AC", "AD", "CD"}})
    for v in ("acd", "dca", "cda", "dac", "cad", "DCA"):                  # « dans n'importe quel ordre »
        assert passes("g.27", e, v), v
    for v in ("dcab", "dc a b", "dcc", "abd"):
        assert not passes("g.27", e, v), v
    assert "Erreur classique" in message("g.27", e, "dc")               # the mistakes are read the same way
    assert "Erreur classique" in message("g.27", e, "ca")
    e = entry("g.28", "BDEAC")                                   # an ordering is never re-sorted
    assert passes("g.28", e, "bdeac") and not passes("g.28", e, "abcde") and not passes("g.28", e, "edcba")
    e = entry("g.24", "BD")                                      # "et" only counts BETWEEN two letters
    for v in ("B, D et", "et B, D", "B et D et"):
        assert not passes("g.24", e, v), v
    assert passes("g.24", e, "B et D") and passes("g.24", e, "(D) et (B)")
    e = entry("g.23", "et")                                      # the word "et" itself is still an answer
    assert passes("g.23", e, "et") and passes("g.23", e, "ET")
    e = entry("g.21", "C")                                       # a single letter is not affected
    assert not passes("g.21", e, "C, A") and passes("g.21", e, "c")
    e = entry("g.22", "cab")                                     # a word answer is never re-sorted
    assert passes("g.22", e, "cab") and not passes("g.22", e, "ABC") and not passes("g.22", e, "A, B, C")


def test_an_ordering_of_letters_typed_with_separators_keeps_its_order():
    e = entry("g.25", "BDEAC", mistakes={"A et E sont inversés": "BDAEC"})
    for v in ("BDEAC", "bdeac", "B, D, E, A, C", "b d e a c", "B; D; E; A; C", "(B), (D), (E), (A), (C)", "B-D-E-A-C"):
        assert passes("g.25", e, v), v
    for v in ("A, B, C, D, E", "ABCDE", "C, A, E, D, B", "B, D, E, A", "B, D, E, A, C, C"):
        assert not passes("g.25", e, v), v
    assert "Erreur classique" in message("g.25", e, "B, D, A, E, C")     # the mistakes are read in order too
    e = entry("g.26", "ABD")                                     # a set of letters still accepts any order
    assert passes("g.26", e, "D, B, A") and passes("g.26", e, "A, B, D")


def test_a_boolean_copied_with_brackets_or_punctuation_is_read_as_the_bare_word():
    e = entry("b.7", True)
    for v in ("Vrai.", "vrai !", "(V)", "« vrai »", " [v] ", "Oui."):
        assert passes("b.7", e, v), v
    for v in ("(F)", "« faux »", "Faux."):
        ok, status, _ = C.check_entry("b.7", e, v)
        assert not ok and status == "wrong", v      # read as False: a wrong answer, not a wrong type
    ok, status, text = C.check_entry("b.7", e, "peut-être")
    assert status == "type" and "« vrai »" in text and "« peut-être »" in text   # says what was read
    assert "objet de type" not in text


def test_english_thousands_separators_get_their_own_message():
    e = entry("d.20", 500_000)
    assert passes("d.20", e, "500 000") and passes("d.20", e, "500000")
    ok, status, text = C.check_entry("d.20", e, "500,000")       # read 500 (French decimal comma)
    assert not ok and status == "type" and "milliers" in text and "bonne valeur" in text
    e = entry("d.21", 2_000_000)
    ok, status, text = C.check_entry("d.21", e, "2,000,000")     # cannot be French at all
    assert not ok and status == "type" and "milliers" in text and "bonne valeur" in text
    ok, status, text = C.check_entry("d.21", e, "3,000,000")     # wrong value: no "right value" claim
    assert status == "type" and "milliers" in text and "bonne valeur" not in text
    e = entry("d.22", 93_312)
    assert C.check_entry("d.22", e, "93,312")[1] == "type"       # not a whole number in French: thousands meant
    e = entry("d.23", 1.667, decimals=3)
    assert passes("d.23", e, "1,667")                            # a French decimal comma stays one
    assert "milliers" not in message("d.23", e, "1,668")
    e = entry("d.24", 0.125, decimals=3)
    assert "milliers" not in message("d.24", e, "0,126")


def test_type_message_names_the_original_type():
    import pandas as pd

    e = entry("g.18", 3)
    assert "`Series`" in message("g.18", e, pd.Series([1.5, 2.5]))


def test_attempt_catches_from_import(capsys, tmp_path):
    pkg = tmp_path / "mymath"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("")
    wbm.load_mymath("learner", path=pkg)
    with wbm.attempt("z.4"):
        from mymath import metrics  # noqa: F401
    assert "⏳ Ex z.4" in capsys.readouterr().out
    wbm.load_mymath("ref")


def test_factor_100_messages_do_not_claim_which_one_is_the_percentage():
    e = entry("d.8", 0.95, decimals=2)          # e.g. an error rate of 0.95 %
    big = message("d.8", e, 95)                 # 95 errors, not a percentage at all
    assert "100 fois trop grande" in big and "pourcentage" in big and "proportion" in big
    e = entry("d.9", 4000)                      # 4000 euros: not a proportion
    assert "100 fois trop grande" in message("d.9", e, 400_000)
    assert "100 fois trop petite" in message("d.9", e, 40)


def test_integer_answer_given_unrounded_is_told_to_round_or_gets_its_mistake():
    e = entry("d.10", 11185, mistakes={"arrondi trop tôt": 11280, "7 intervalles, pas 8": 44})
    text = message("d.10", e, 11185.448)
    assert "arrondis" in text and "11185" not in text
    assert "7 intervalles" in C.check_entry("d.10", e, 43.75)[2]       # round(43.75) = 44, a declared mistake
    assert "arrondi trop tôt" in C.check_entry("d.10", e, 11279.6)[2]
    assert "entier" in message("d.10", e, 12.5)


def test_a_date_is_a_wrong_type_with_a_useful_message():
    import pandas as pd

    e = entry("d.11", 1778)
    ok, status, text = C.check_entry("d.11", e, pd.Timestamp("1778-05-01"))
    assert not ok and status == "type" and ".year" in text



def test_factor_100_is_not_claimed_when_the_answer_has_one_significant_digit():
    e = entry("d.12", 0.00926, decimals=2)      # stored as "0.01": 0.6 / 100 also rounds to 0.01
    for wrong in (0.6, 0.99, 1.0):
        assert "100 fois" not in message("d.12", e, wrong), wrong
    e = entry("d.13", 0.684, decimals=3)        # 3 significant digits: 68.4 is a percentage
    assert "100 fois trop grande" in message("d.13", e, 68.4)


def test_array_of_percentages_gets_the_factor_100_message():
    e = entry("d.14", [0.68391, 0.9546, 0.99708], decimals=3)
    text = message("d.14", e, [68.391, 95.46, 99.708])
    assert "100 fois trop grandes" in text and "0,684" not in text
    assert "100 fois trop petites" in message("d.14", e, [0.0068391, 0.009546, 0.0099708])
    small = entry("d.15", [0.01, 0.02], decimals=2)   # one significant digit: no claim
    assert "100 fois" not in message("d.15", small, [1.3, 1.7])
    counts = entry("d.16", [3, 5, 9, 0])            # integers: no percentage message
    assert "100 fois" not in message("d.16", counts, [300, 500, 900, 0])


def test_almost_only_one_unit_away_or_too_few_decimals():
    e = entry("d.17", 0.3, decimals=1)                 # one significant digit: 0.2 or 0.1 are far off
    for wrong in (0.1, 0.0, 0.2, 0.4, 0.45, -0.2):
        assert "presque" not in message("d.17", e, wrong), wrong
    e = entry("d.18", 0.86840, decimals=3)             # stored as "0.868"
    for early in (0.869, 0.867, 0.86865):              # a mean of rounded values, a truncation
        assert "presque" in message("d.18", e, early), early
    assert "presque" not in message("d.18", e, 0.865)  # three units away: a wrong value
    too_short = message("d.18", e, 0.87)               # right at 2 decimals, but 3 are asked
    assert "presque" in too_short and "3" in too_short
    e = entry("d.19", 0.65, decimals=2)                # 2 significant digits: 0.64 may well be another measure
    for wrong in (0.60, 0.64, 0.66):
        assert "presque" not in message("d.19", e, wrong), wrong
    e = entry("d.20", 3.2, decimals=1)
    assert "presque" not in message("d.20", e, 3.3) and "presque" not in message("d.20", e, 3.0)
    e = entry("d.25", 3.25, decimals=2)
    assert "presque" in message("d.25", e, 3.26)
    e = entry("d.26", 0.849, decimals=3)               # too few decimals is said first, even one unit away
    assert "juste à 2 décimale" in message("d.26", e, 0.85)


def test_too_few_decimals_is_recognized_two_decimals_short_or_more():
    """Session 10 (R6, learner): 1.15 for 1.1487 (4 decimals asked) is right at 2 decimals, not « le détail du calcul
    qui cloche » ; -2.74 for -2.7364 too. Only roundings that keep 2 significant digits are claimed."""
    e = entry("d.27", 2 ** (1 / 5), decimals=4)                  # 1.1487
    assert "juste à 2 décimales" in message("d.27", e, 1.15)
    assert "juste à 1 décimale" in message("d.27", e, 1.1)
    assert "juste à" not in message("d.27", e, 1.16) and "juste à" not in message("d.27", e, 1.2)
    e = entry("d.28", -2.7364, decimals=4)
    assert "juste à 2 décimales" in message("d.28", e, -2.74)
    e = entry("d.29", 0.0498, decimals=4)                        # 0.05 is 0.050, right at 3 decimals; 0.0 never
    assert "juste à 3 décimales" in message("d.29", e, 0.05) and "juste à" not in message("d.29", e, 0.0)
    e = entry("d.31", 0.1234, decimals=4)                        # 0.1 keeps one significant digit only
    assert "juste à 2 décimales" in message("d.31", e, 0.12) and "juste à" not in message("d.31", e, 0.1)
    e = entry("d.30", 6.4375, decimals=4)                        # a tie at 2 decimals: 6.44 at school, 6.44 here too
    assert "juste à 2 décimales" in message("d.30", e, 6.44)


def test_fractions_written_as_text_are_numbers_and_percent_signs_get_a_message():
    e = entry("d.21", 41 / 76, decimals=3)
    assert passes("d.21", e, "41/76") and passes("d.21", e, "41 / 76")
    assert not passes("d.21", e, "76/41")
    e = entry("d.22", 3)
    assert passes("d.22", e, "6/2")
    ok, status, text = C.check_entry("d.23", entry("d.23", 0.3, decimals=2), "30 %")
    assert not ok and status == "type" and "sans le signe %" in text and "0.3" not in text
    assert C.check_entry("d.23", entry("d.23", 0.3, decimals=2), "1/0")[1] == "type"


def test_arrays_accept_numbers_written_as_text_and_hint_at_rounding():
    e = entry("d.24", [41 / 48, 13 / 18, 33 / 34], decimals=3)
    assert passes("d.24", e, ["0,854", "0,722", "0,971"])
    assert passes("d.24", e, np.array(["0.854", "0.722", "0.971"]))
    assert passes("d.24", e, ["41/48", "13/18", "33/34"])
    assert "presque" in message("d.24", e, [0.85, 0.72, 0.97])        # too few decimals
    assert "presque" in message("d.24", e, [0.854, 0.723, 0.971])     # one unit away
    far = message("d.24", e, [0.854, 0.65, 0.971])
    assert "presque" not in far and "2 éléments sur 3" in far
    assert "n'est pas un nombre" in message("d.24", e, ["0,854", "abc", "0,971"])


# ---------------------------------------------------------------- session 11 (chapter 3, notebook)
def test_mistake_keys_must_be_messages_not_values():
    """{wrong value: message} (inverted) would store the wrong choice in clear in answers.json."""
    with pytest.raises(ValueError, match="inverted"):
        entry("m.1", "B", mistakes={"A": "compare les precisions parmi 300 alertes"})
    e = entry("m.1", "B", mistakes={"compare les precisions parmi 300 alertes": "A"})
    assert "compare les precisions" in message("m.1", e, "A")
    assert "A" not in e["mistakes"].values()          # the wrong choice itself is never stored in clear


def test_transposed_square_array_is_diagnosed():
    matrix = [[146, 3, 2], [6, 61, 1], [14, 19, 90]]
    e = entry("m.2", matrix)
    assert "transposé" in message("m.2", e, np.array(matrix).T)
    symmetric = [[1, 2], [2, 5]]
    e_sym = entry("m.3", symmetric)
    assert passes("m.3", e_sym, np.array(symmetric).T)   # a symmetric table equals its transpose: right answer


def test_computed_values_get_no_rounding_advice():
    """A value computed by the learner's function is never a rounding slip."""
    e = entry("m.4", 0.9956, decimals=3)
    typed = message("m.4", e, 0.995)
    computed = C.check_entry("m.4", e, 0.995, computed=True)[2]
    assert "presque" in typed.lower()
    assert "trop tôt" not in computed and "décimale" not in computed and "ta fonction" in computed.lower()
    arr_e = entry("m.5", [0.794, 0.0122, 0.9956, 0.9803], decimals=3)
    wrong = [0.794, 0.012, 0.995, 0.980]
    assert "presque" in message("m.5", arr_e, wrong).lower()
    assert "ta fonction" in C.check_entry("m.5", arr_e, wrong, computed=True)[2].lower()


def test_record_warns_when_an_array_element_is_near_a_rounding_boundary(capsys):
    C.record("m.6", [0.8269, 0.914499], decimals=3)
    assert "limite d'arrondi" in capsys.readouterr().out


# ---------------------------------------------------------------- session 12 (chapter 4)
def test_too_few_decimals_is_recognized_on_a_rounding_boundary():
    """0.625 asked with 3 decimals: 0.63 (rounded half up) and 0.62 (Python's rounding) are both 'right at 2'."""
    e = entry("n.1", 0.625, decimals=3)
    for given in (0.63, 0.62):
        assert "juste à 2 décimales" in message("n.1", e, given)
    assert "juste à 2" not in message("n.1", e, 0.61)


def test_too_few_decimals_on_a_tie_stored_under_the_half():
    """Session 77 (B8, solver V1): a tie computed just under the half (1.5 * 1.65 is 2.4749999..., the loss of
    B8.5d is -0.31499999...) gives « presque » for Python's rounding and for the school one (half away from zero); a
    truncation of a tie (0.7 for 0.75, -0.37 for -0.375) stays a wrong value, as 0.6 for 0.65 (d.19)."""
    cases = ((1.5 * (2.4 - 0.75), 3, (2.47, 2.48), None),                 # 2.4749999999999996 (B8.2b)
             (-(2.4 + 0.9 - 0.96 - 1.08) / 4, 3, (-0.31, -0.32), None),     # -0.31499999999999995 (B8.5d)
             (0.75, 2, (0.8,), 0.7), (-0.375, 3, (-0.38,), -0.37))
    for value, decimals, neighbours, truncated in cases:
        e = entry("n.10", value, decimals=decimals)
        for given in neighbours:
            assert f"juste à {decimals - 1} décimale" + ("s" if decimals > 2 else "") in message("n.10", e, given), (value, given)
        if truncated is not None:
            assert "presque" not in message("n.10", e, truncated), (value, truncated)
    e = entry("n.11", 2.4751, decimals=4)                 # not a tie at 3 decimals: only the right rounding
    assert "juste à 3" in message("n.11", e, 2.475) and "juste à 3" not in message("n.11", e, 2.476)


def test_magnitude_messages_for_negative_answers_speak_of_absolute_value():
    """-1000.313 is smaller than -999.687: 'too large' would be wrong without 'in absolute value'."""
    e = entry("n.2", -999.687, decimals=3)
    assert "trop grande en valeur absolue" in message("n.2", e, -1000.313)
    assert "trop petite en valeur absolue" in message("n.2", e, -99.97)
    positive = entry("n.3", 999.687, decimals=3)
    assert "valeur absolue" not in message("n.3", positive, 1000.313)


def test_two_mistakes_with_the_same_value_are_refused():
    """The learner would only ever read one of the two messages (h/n = mean of Beta(h, t) in 4.22 b)."""
    with pytest.raises(ValueError, match="same value"):
        entry("n.4", 0.636, decimals=3, mistakes={"c'est le mode h / n du posterior": 0.65,
                                                  "c'est la moyenne de Beta(h, t)": 13 / 20})


def test_too_few_decimals_is_judged_on_the_true_value_not_on_its_rounding():
    """95.2948 is recorded as 95.295 (3 decimals): at 2 decimals the right value is 95.29, not 95.30."""
    e = entry("n.5", 95.29482, decimals=3)
    assert "juste à 2 décimales" in message("n.5", e, 95.29)
    assert "juste à 2" not in message("n.5", e, 95.30) and "juste à 2" not in message("n.5", e, 95.3)
    e = entry("n.6", 0.034595, decimals=3)
    assert "juste à 2 décimales" in message("n.6", e, 0.03)
    assert "juste à 2" not in message("n.6", e, 0.04)
    for value, good, bad in [(1.2348, 1.23, 1.24), (0.1449, 0.14, 0.15)]:
        e = entry("n.7", value, decimals=3)
        assert "juste à 2" in message("n.7", e, good) and "juste à 2" not in message("n.7", e, bad)


def test_array_elements_with_too_few_decimals_are_judged_on_the_true_values():
    e = entry("n.8", [0.034595, 0.5], decimals=3)
    assert "presque" in message("n.8", e, [0.03, 0.5]).lower()
    assert "presque" not in message("n.8", e, [0.04, 0.5]).lower()
    tie = entry("n.9", [0.625, 0.25], decimals=3)
    for given in ([0.63, 0.25], [0.62, 0.25]):
        assert "presque" in message("n.9", tie, given).lower()


def test_a_decimal_comma_typed_without_quotes_gets_a_message():
    """0,5 typed without quotes is the tuple (0, 5) in Python; [1,5] is a list of two numbers."""
    e = entry("m.20", 0.5, decimals=1)
    text = message("m.20", e, (0, 5))
    assert "virgule décimale" in text and "0.5" in text
    assert passes("m.20", e, "0,5")
    neg = entry("m.21", -0.25, decimals=2)
    assert "virgule décimale" in message("m.21", neg, (-0, 25))   # -0,25 is (0, 25): -0 is 0
    arr_e = entry("m.22", [3.0, 2.0, 1.5], decimals=3)
    assert "virgules décimales" in message("m.22", arr_e, [3, 2, 1, 5])
    assert "virgule" not in message("m.22", arr_e, [3, 2])            # too few elements: no such hint
    assert "virgule" not in message("m.22", arr_e, [3, 2, 1.5, 0.5])  # a non-whole number: no comma split
    assert "virgule" not in C.check_entry("m.22", arr_e, [3, 2, 1, 5], computed=True)[2]  # computed, not typed
    int_e = entry("m.25", [47, 50], decimals=0)
    assert "virgule" not in message("m.25", int_e, [47, 50, 3])       # whole numbers expected: no such hint


def test_computed_values_point_to_the_function_and_its_tests():
    """A wrong value computed by the learner's function gets no hint about units, sums or rounding."""
    e = entry("m.23", 980)
    assert "1 près" in message("m.23", e, 981)
    computed = C.check_entry("m.23", e, 981, computed=True)[2]
    assert "ta fonction" in computed.lower() and "off-by-one" not in computed
    f = entry("m.24", 2.0000003, decimals=4)
    far = C.check_entry("m.24", f, 1.0032, computed=True)[2]
    assert "tests" in far and "ordre de grandeur" not in far.lower() and "unité" not in far
    assert "docstring" in far and "cette cellule" not in far           # not every check cell runs the tests
    assert "ordre de grandeur" in message("m.24", f, 2.5).lower()      # typed values keep the arithmetic hints


def test_fractional_hint_replaces_the_round_to_nearest_advice():
    # a code length is ceil(log2 N): 7.88 must not be told "round to the nearest integer"
    e = entry("f.1", 8, fractional="un code a un nombre entier de chiffres : arrondis log2 N à l'entier supérieur")
    assert passes("f.1", e, 8) and passes("f.1", e, 8.0)
    ok, status, text = C.check_entry("f.1", e, 7.88)
    assert not ok and status == "wrong" and "entier supérieur" in text and "le plus proche" not in text
    assert "entier supérieur" in message("f.1", e, 6.02)      # also when rounding to nearest would be wrong
    assert "entier supérieur" not in message("f.1", e, 7)     # a whole number gets the usual diagnosis
    plain = entry("f.2", 8)
    assert "le plus proche" in message("f.2", plain, 7.88)    # without the option, the generic advice stays


def test_fractional_is_only_for_whole_number_answers_and_must_be_a_sentence():
    with pytest.raises(ValueError, match="whole-number"):
        entry("f.3", 2.5, decimals=1, fractional="arrondis à l'entier supérieur")
    with pytest.raises(ValueError, match="hint sentence"):
        entry("f.4", 3, fractional="ceil")


def test_fractional_hint_survives_the_answers_file(tmp_path):
    e = C.make_entry("f.5", 13, fractional="arrondis à l'entier supérieur")
    path = tmp_path / "answers.json"
    path.write_text(json.dumps({"answers": {"f.5": e}}), encoding="utf-8")
    loaded = C.load_answers(path, reload=True)["f.5"]
    assert "entier supérieur" in C.check_entry("f.5", loaded, 12.93)[2]


def test_zero_is_never_almost_right():
    # 0.01 asked with 2 decimals: 0 is right "with one decimal less" (0.0), but it is not almost right
    e = entry("z.1", 0.01, decimals=2)
    assert "presque" not in message("z.1", e, 0)
    assert "presque" not in message("z.1", e, 0.0)
    near = entry("z.2", 0.123, decimals=3)
    assert "presque" in message("z.2", near, 0.12)                # the usual case is unchanged
    pair = entry("z.3", [0.01, 0.5], decimals=2)                  # the same rule for the elements of an array
    assert "presque" not in message("z.3", pair, [0, 0.5])
    assert "presque" in message("z.4", entry("z.4", [0.123, 0.5], decimals=3), [0.12, 0.5])


def test_choices_ask_for_one_of_the_offered_values():
    e = entry("c.1", 4.0, decimals=1, choices=[3, 4, 4.7, 5],
              mistakes={"c'est le maximum possible : les lettres ne sont pas équiprobables": 4.7})
    assert passes("c.1", e, 4) and passes("c.1", e, 4.0)
    assert "maximum" in message("c.1", e, 4.7)                    # a classic mistake keeps its message
    text = message("c.1", e, 4.2)                                 # an estimate outside the offered values
    assert "valeurs proposées" in text and "3, 4, 4,7 ou 5" in text and "calcul" not in text
    assert "valeurs proposées" not in message("c.1", e, 3)       # another offered value: the usual diagnosis
    small = entry("c.2", 0.2, decimals=2, choices=[0.02, 0.2, 2])
    assert "0,02, 0,2 ou 2" in message("c.2", small, 0.15)


def test_choices_must_contain_the_answer_and_be_numeric():
    with pytest.raises(ValueError, match="not among"):
        entry("c.3", 4.0, decimals=1, choices=[3, 5])
    with pytest.raises(ValueError, match="numeric"):
        entry("c.4", "oui", choices=["oui", "non"])


def test_a_vector_written_with_floats_or_semicolons_is_read_as_its_tuple_text():
    """A position or vector "(4, 3)" computed in Python comes as floats; a French vector uses semicolons (ch. 25)."""
    import numpy as np

    e = entry("g.45", "(4, 3)")
    for v in ("(4.0, 3.0)", (4.0, 3.0), np.array([4.0, 3.0]), np.array([4, 3]), "(4 ; 3)", "(4,0 ; 3,0)", "[4., 3.]"):
        assert passes("g.45", e, v), v
    for v in ("(4.5, 3)", "(3, 4)", (4.5, 3.0), "(4 ; 3,5)"):
        assert not passes("g.45", e, v), v
    for v in ("(2.5, 1.5)", "(3, 4)"):                   # a wrong vector gets the shape/vector hint, not spelling
        text = message("g.45", e, v)
        assert "vecteur" in text and "orthographe" not in text, (v, text)


def test_sets_of_integers_do_not_round_a_decimal_and_read_numbers_in_quotes():
    e = entry("t.5", [-3, 2], ordered=False)
    assert passes("t.5", e, [2, -3]) and passes("t.5", e, ["2", "-3"]) and passes("t.5", e, ["2", "−3"])
    assert not passes("t.5", e, [2.4, -3])
    e = entry("t.6", [4, 5, 5.5], ordered=False, decimals=1)
    assert passes("t.6", e, ["4", "5", "5,5"])


def test_common_wrong_types_are_explained_in_words():
    import sympy as sp
    x, y = sp.symbols("x y")
    e = entry("t.9", [3, 10, -11, 2])
    assert "sp.Poly" in message("t.9", e, 3*x**3 + 10*x**2 - 11*x + 2)
    assert "dictionnaire" in message("t.9", e, {x: 1, y: 2})
    e = entry("t.10", [3, -4], ordered=False)
    assert "« x - 3 »" in message("t.10", e, [x - 3, x + 4])
    assert "crochets" in message("t.10", e, 3)


def test_a_set_reads_a_fraction_typed_between_quotes():
    e = entry("t.8", [-4 / 3, 4 / 3], ordered=False, decimals=6)
    assert passes("t.8", e, ["4/3", "-4/3"]) and passes("t.8", e, [4 / 3, "−4/3"]) and passes("t.8", e, ("4/3", -4 / 3))
    assert not passes("t.8", e, ["4/3", "4/3"]) and not passes("t.8", e, ["1.33", "-1.33"])
    assert not passes("t.8", e, ["4/0", "-4/3"])          # a zero denominator is not read as a number


def test_a_string_order_may_be_written_with_its_signs():
    e = entry("t.7", "ACEDBF")
    assert passes("t.7", e, "A < C < E < D < B < F") and passes("t.7", e, "a,c,e,d,b,f")


# ---------------------------------------------------------------- R3: learner simulation

def test_an_exact_set_rounded_by_the_learner_is_named_as_such():
    """6 decimals or more mean an exact fraction is expected: -0.333 for -1/3 is « arrondie », not a wrong set."""
    e = entry("t3.1", [-1 / 3, 2], ordered=False, decimals=8)
    for rounded in ([-0.33, 2], [2, -0.333], ["-0,3333", 2]):
        assert "arrondie" in message("t3.1", e, rounded)
    assert "arrondie" not in message("t3.1", e, [-0.34, 2])
    assert passes("t3.1", e, ["-1/3", 2]) and passes("t3.1", e, [-1 / 3, 2])


def test_an_exact_list_rounded_by_the_learner_is_named_as_such_but_not_a_list_to_round():
    e = entry("t3.2", [3, -1 / 3, 2], decimals=8)
    assert "arrondie" in message("t3.2", e, [3, -0.33, 2])
    asked = entry("t3.3", [0.123, 0.5], decimals=3)                  # the statement asks for 3 decimals
    assert "arrondie" not in message("t3.3", asked, [0.12, 0.5])


def test_a_decimal_comma_inside_a_set_is_explained_when_it_hides_the_right_answer():
    e = entry("t3.4", [9 / 4], ordered=False, decimals=6)
    assert "virgules décimales" in message("t3.4", e, [2, 25])
    assert "virgules décimales" not in message("t3.4", e, [2, 26])


def test_a_prediction_gets_no_hint_about_its_sign_or_size():
    e = entry("t3.5", 5, prediction=True, mistakes={"on retire 3 d'abord, puis la valeur absolue": -1})
    for wrong in (-5, 50, 6):
        assert message("t3.5", e, wrong).startswith("Prédiction ratée") and "signe" not in message("t3.5", e, wrong)
    assert "on retire 3" in message("t3.5", e, -1)


def test_a_list_of_letters_is_read_as_the_text_of_the_letters():
    e = entry("t3.6", "ACF")
    assert passes("t3.6", e, ["A", "C", "F"]) and passes("t3.6", e, ["f", "a", "c"])
    assert not passes("t3.6", e, ["A", "C"])


def test_an_expression_typed_for_a_list_of_coefficients_gets_the_form_in_words():
    e = entry("t3.7", [2, 0, -3])
    text = message("t3.7", e, "2*x**2 - 3")
    assert "liste de ses coefficients" in text and "tenseur" not in text
    assert "élément en trop" in message("t3.7", e, [2, 0, -3, 0])
    assert "coefficient nul" in message("t3.7", e, [2, -3])


def test_a_value_from_the_learners_function_gets_no_hint_about_its_sign():
    e = entry("t3.8", -13)
    assert "Ta fonction" in C.check_entry("t3.8", e, 26, computed=True)[2]


# ---------------------------------------------------------------- R4: learner simulation

def test_a_truth_table_column_typed_as_letters_is_read():
    e = entry("t4.1", [False, True, True, True])
    assert passes("t4.1", e, "FVVV") and passes("t4.1", e, "f, v, v, v")
    assert "ordre inverse" in message("t4.1", e, "VVVF")


def test_a_wrong_text_of_digits_gets_no_spelling_hint():
    e = entry("g.45", "1001")
    for v in ("0100", "1.01", "10001"):
        text = message("g.45", e, v)
        assert "calcul" in text and "orthographe" not in text, (v, text)
    assert "orthographe" in message("g.45", e, "neuf")             # a word keeps the spelling hint


def test_a_none_inside_a_list_is_named():
    e = entry("t4.2", [85, 0, 1024, 1])
    assert "None" in C.check_entry("t4.2", e, [85, None, 1024, 1], computed=True)[2]
    assert "None" in message("t4.2", e, [85, None, 1024, 1])


def test_a_text_computed_by_the_learners_function_gets_no_spelling_advice():
    e = entry("t4.3", "None", mistakes={"rends None, pas False": "False"})
    text = C.check_entry("t4.3", e, "0", computed=True)[2]
    assert "Ta fonction" in text and "orthographe" not in text


def test_a_prediction_outside_its_choices_is_told_the_choices():
    """A 🔮 answered by a number that is not offered (R5.18c = 4) is told the offered values, not « Prédiction ratée »."""
    import wbm.checker as checker
    entry = checker.make_entry("P.c", 2, None, choices=[1, 2, 3], prediction=True)
    passed, _, message = checker.check_entry("P.c", entry, 4)
    assert not passed and message.startswith("Réponds par le numéro du choix, 1, 2 ou 3"), message
    assert checker.check_entry("P.c", entry, 3)[2].startswith("Prédiction ratée")
    other = checker.make_entry("P.d", 4, None, choices=[3, 4, 5], prediction=True)   # values, not numbers of choices
    assert checker.check_entry("P.d", other, 7)[2].startswith("Choisis l'une des valeurs proposées")


@pytest.mark.parametrize("value", ["plus de 50 %", 0.85, 4])
def test_any_value_outside_the_choices_of_a_prediction_is_told_the_choices(value):
    """Session 13 (R8 learner, C11): a text, a percentage or a decimal for a choice 1, 2 or 3 gets the same message."""
    import wbm.checker as checker
    entry = checker.make_entry("P.d", 3, None, choices=[1, 2, 3], prediction=True)
    passed, _, message = checker.check_entry("P.d", entry, value)
    assert not passed and message.startswith("Réponds par le numéro du choix, 1, 2 ou 3"), message


def test_a_computed_value_right_only_at_zero_decimals_is_not_almost_right():
    """Session 13 (R8 learner, C2): a function that returns 1 for 0.706 (an integer division) is not « tout près »."""
    import wbm.checker as checker
    entry = checker.make_entry("C.z", 0.7063162427, decimals=3)
    message = checker.check_entry("C.z", entry, 1, computed=True)[2]
    assert "Tout près" not in message and "//" in message, message


def test_a_computed_proportion_of_one_names_the_condition_and_the_generator():
    """Session 19 (M02c learner): a coverage of exactly 1.0 (every case passes, or identical simulated samples) gets
    the integer-division hint and the proportion and generator hints; a near value names the seed and the order."""
    import wbm.checker as checker
    entry = checker.make_entry("C.p", 0.9489, decimals=2)
    message = checker.check_entry("C.p", entry, 1.0, computed=True)[2]
    assert "//" in message and "proportion" in message and "générateur" in message, message
    near = checker.check_entry("C.p", checker.make_entry("C.p", 1.994470280, decimals=2), 2.0013, computed=True)[2]
    assert "Tout près" in near and "graine" in near, near


def test_the_right_values_in_another_order_name_no_order():
    """Session 13 (R8 learner, C9): the order asked may be that of the letters A, B, E, not the increasing order."""
    import wbm.checker as checker
    entry = checker.make_entry("O.p", [0.4375, 0.5, 0.0], decimals=4)
    message = checker.check_entry("O.p", entry, [0.5, 0.4375, 0.0])[2]
    assert "pas dans l'ordre demandé" in message and "croissant" not in message, message


def test_infinite_limits_are_written_like_interval_ends():
    """Session 11 (R7): a limit +∞ is typed "+oo" (as in an interval), "∞", float("inf") or "inf"; the other sign
    gets « le signe est inversé », a finite answer for an infinite limit (and the reverse) a plain message."""
    e = entry("d.32", math.inf, decimals=2)
    for v in ("+oo", "oo", "∞", "+∞", math.inf, "inf", " + oo "):
        assert passes("d.32", e, v), v
    assert "signe est inversé" in message("d.32", e, "-oo")
    assert "signe" not in message("d.32", e, 3.0)
    e = entry("d.33", -math.inf, decimals=2)
    assert passes("d.33", e, "-oo") and passes("d.33", e, "−∞") and passes("d.33", e, -math.inf)
    e = entry("d.34", 2.0, decimals=2)
    assert "infinie" in message("d.34", e, "+oo")


# ---------------------------------------------------------------- session 12 (R7, learner simulation)
def test_sympy_numbers_booleans_and_sets_are_read_as_python_values():
    import sympy

    e = entry("s.1", 0.25, decimals=2)
    assert passes("s.1", e, sympy.Float(0.25)) and passes("s.1", e, sympy.Rational(1, 4))
    assert passes("s.2", entry("s.2", [True, True, False]), [sympy.true, sympy.true, sympy.false])
    assert passes("s.3", entry("s.3", math.inf, decimals=2), sympy.oo)
    assert "sorted" in message("s.4", entry("s.4", [0, 2]), sympy.FiniteSet(0, 2))


def test_plus_l_infini_is_read_as_infinity():
    e = entry("s.5", math.inf, decimals=2)
    for text in ("plus l'infini", "plus l’infini", "+oo", "plus infini"):
        assert passes("s.5", e, text), text
    assert passes("s.6", entry("s.6", -math.inf, decimals=2), "moins l'infini")


def test_a_list_typed_in_quotes_is_told_to_drop_them():
    assert "enlève les guillemets" in message("s.7", entry("s.7", [-1, 3]), "[-1, 3]")


def test_a_list_typed_in_quotes_the_french_way_gets_the_python_writing():
    e = entry("s.7b", [0.2, 0.4, 0.4], decimals=2)
    for text in ("[0,2 ; 0,4 ; 0,4]", "[0.2; 0.4; 0.4]"):
        assert "points décimaux et des virgules" in message("s.7b", e, text), text


def test_an_exact_form_where_a_decimal_is_asked():
    e = entry("s.8", math.log(2), decimals=3)
    assert "Ta valeur exacte est la bonne" in message("s.8", e, "ln(2)")
    assert "pas une forme exacte" in message("s.8", e, "ln(3)")
    assert "« e »" in message("s.9", entry("s.9", [math.e, 0.0], decimals=3), ["e", 0])


def test_a_non_integer_mistake_of_an_integer_list_is_not_rounded():
    e = entry("s.10", [-1, 3], mistakes={"le dénominateur, pas le numérateur": [2 / 3, 3]})
    assert "dénominateur" in message("s.10", e, [2 / 3, 3]) and "dénominateur" in message("s.10", e, [0.67, 3])
    assert "dénominateur" not in message("s.10", e, [1, 3])


def test_the_complement_hint_needs_a_value_strictly_between_0_and_1():
    e = entry("s.11", 0.0, decimals=2)
    assert "complément" not in message("s.11", e, 1)


def test_far_too_few_decimals_is_said_without_presque():
    e = entry("s.12", math.log(2), decimals=3)
    text = message("s.12", e, 0.7)
    assert "n'a que 1 décimale" in text and "presque" not in text
    assert "n'a que 0 décimale" in message("s.13", entry("s.13", 60 * math.pi, decimals=2), 188)
    arr = entry("s.14", [4.02, 4.02], decimals=3)
    assert "trop peu de décimales" in message("s.14", arr, [4.0, 4.0])


def test_the_right_values_in_another_order():
    e = entry("s.15", [12, 6, 2])
    assert "pas dans l'ordre" in message("s.15", e, [2, 12, 6])


def test_classic_mistakes_end_with_a_full_stop():
    e = entry("s.16", 5.0, decimals=2, mistakes={"relis la consigne": 2})
    assert message("s.16", e, 2) == "Erreur classique. Piste : relis la consigne."


def test_a_wrong_choice_is_not_a_calculation_slip():
    """A choice 1, 2 or 3 that is not a prediction: 2 for 3 is a wrong choice, never « à 1 près » (session 15, CP0)."""
    e = entry("d.4w", 3, choices=[1, 2, 3])
    text = C.check_entry("d.4w", e, 2)[2]
    assert "bon choix" in text and "1 près" not in text


def test_a_pair_for_a_number_suggests_keeping_one_value():
    entry = C.make_entry("Q.20", 1.772454, decimals=6)
    passed, status, message = C.check_entry("Q.20", entry, (1.7724538509, 1.4e-08))
    assert not passed and status == "type" and "resultat[0]" in message


def test_an_exact_integer_answer_does_not_invite_to_round_a_wrong_value():
    entry = C.make_entry("Q.21", 0)
    passed, _, message = C.check_entry("Q.21", entry, 0.33)
    assert not passed and "Si l'énoncé demande d'arrondir" in message
