from evalkit.report import markdown_table
from evalkit.runner import EvalResult


def test_markdown_table_has_header_and_row():
    table = markdown_table([EvalResult(model="baseline", task="arith", n=10, accuracy=0.5, ci=(0.2, 0.8))])
    lines = table.splitlines()
    assert lines[0].startswith("| model")
    assert "0.500" in lines[2]
    assert "[0.200, 0.800]" in lines[2]
