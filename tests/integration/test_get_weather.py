from receiver import argument_parser


def test_get_weather(capfd):
    argument_parser(["-w"])

    out = capfd.readouterr()[0]
    assert "Current Weather" in out
