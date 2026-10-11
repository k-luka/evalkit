from evalkit.metrics import accuracy, bootstrap_ci, exact_match


def test_exact_match_ignores_case_whitespace_and_trailing_period():
    assert exact_match("  Paris. ", "paris")
    assert not exact_match("Lyon", "Paris")


def test_accuracy():
    assert accuracy([True, False, True, True]) == 0.75
    assert accuracy([]) == 0.0


def test_bootstrap_ci_contains_point_estimate():
    correct = [True] * 60 + [False] * 40
    lo, hi = bootstrap_ci(correct)
    assert lo <= 0.6 <= hi
    assert bootstrap_ci(correct) == bootstrap_ci(correct)
