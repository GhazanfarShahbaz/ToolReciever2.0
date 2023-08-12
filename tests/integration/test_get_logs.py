from receiver import argument_parser


def test_get_event_today(capfd):
    argument_parser(["-gl"])

    out = capfd.readouterr()[0]
    assert "Successfully saved logs." in out
