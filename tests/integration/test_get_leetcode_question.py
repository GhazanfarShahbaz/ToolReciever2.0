import pytest

from receiver import argument_parser


@pytest.fixture
def leetcode_argument_fixture(request):
    arguments = ["-lc"]

    if request.param[0]:
        arguments.append("-lc_d")
        arguments.append(request.param[0])

    if request.param[1]:
        arguments.append("-lc_t")
        arguments.append(request.param[1])

    yield arguments


@pytest.mark.parametrize(
    "leetcode_argument_fixture",
    [
        [None, None],
        ["easy", None],
        ["medium", None],
        ["hard", None],
        [None, "array"],
        [None, "array"],
        ["easy", "array"],
    ],
    indirect=True,
)
def test_process_random_leetcode_request(leetcode_argument_fixture, capfd):
    argument_parser(leetcode_argument_fixture)

    out = capfd.readouterr()[0]
    assert "Leetcode Question Link:" in out
