import pytest

from day2 import part1, part2


def test_part1():
    the_list = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"]

    assert part1(the_list) == 2


@pytest.mark.parametrize("a_list, safe", [
    [["9 12 14 16 17 18 15"], 1],
    [["86 88 91 94 95 95"], 1],
    [["15 18 20 21 23 25 28 32"], 1],
    [["70 72 74 77 78 83"], 1],
    [["57 60 62 64 63 64 65"], 1],
    [["44 45 44 47 46"], 0],
    [["33 35 32 33 36 36"], 0],
    [["83 86 88 89 87 88 90 94"], 0],
    [["56 59 62 65 68 65 68 75"], 0],
    [["36 39 40 40 43"], 1],
    [["87 90 93 95 95 97 94"], 0]])
def test_part2(a_list: list[str], safe: int):

    assert part2(a_list) == safe

