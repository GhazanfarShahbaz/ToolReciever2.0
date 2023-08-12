from receiver import argument_parser


def test_get_event_today(capfd):
    argument_parser(["-euler"])

    out = capfd.readouterr()[0]
    assert "Euler Question Link:" in out
