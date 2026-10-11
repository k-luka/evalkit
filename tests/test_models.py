from evalkit.models import BaselineModel, get_model


def test_baseline_adds_and_subtracts():
    m = BaselineModel()
    assert m.generate("What is 12 + 30?") == "42"
    assert m.generate("What is 12 - 30?") == "-18"


def test_get_model_unknown_name():
    try:
        get_model("gpt-17")
    except ValueError as e:
        assert "baseline" in str(e)
    else:
        raise AssertionError("expected ValueError")
