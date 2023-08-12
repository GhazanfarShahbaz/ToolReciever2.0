import pytest

from receiver import argument_parser


@pytest.fixture
def codechef_argument_fixture(request):
    arguments = ["-cf"]

    if request.param[0]:
        arguments.append("-cf_d")
        arguments.append(request.param[0])

    yield arguments


@pytest.mark.parametrize(
    "codechef_argument_fixture",
    [[None], ["beginner"], ["easy"], ["beginner"], ["medium"], ["hard"], ["challenge"]],
    indirect=True,
)
def test_process_random_codechef_request(codechef_argument_fixture, capfd):
    argument_parser(codechef_argument_fixture)

    out = capfd.readouterr()[0]
    assert "Codechef Question Link:" in out
