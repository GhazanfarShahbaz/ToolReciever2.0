from receiver import argument_parser


def test_get_event_today(capfd):
    argument_parser(["-dgm"])

    out = capfd.readouterr()[0]
    assert "Emails" in out
