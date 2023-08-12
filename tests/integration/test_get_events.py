import pytest

from receiver import argument_parser


@pytest.mark.parametrize("param", [("today"), ("week"), ("month"), ("year")])
def test_get_event_today(param, capfd):
    argument_parser(["-df", param])

    out = capfd.readouterr()[0]
    assert "Schedule" in out or "No events sceduled for" in out
