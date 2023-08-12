import pytest

from receiver import argument_parser


@pytest.mark.parametrize("param", [("today"), ("month"), ("year")])
def test_get_diagnostics(param, capfd):
    argument_parser(["-diagnostics", param])

    out = capfd.readouterr()[0]
    assert "No endpoints hit yet" in out or "Endpoints Hit Count" in out
