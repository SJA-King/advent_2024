import pytest

from day4 import part1, part2


def test_part1():
    coords = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"]

    assert part1(coords) == 18

    # answer
    # ....XXMAS.
    # .SAMXMS...
    # ...S..A...
    # ..A.A.MS.X
    # XMASAMX.MM
    # X.....XA.A
    # S.S.S.S.SS
    # .A.A.A.A.A
    # ..M.M.M.MM
    # .X.X.XMASX


def test_part2():
    coords = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"]

    assert part2(coords) == 9

    # answer
    # .M.S......
    # ..A..MSMS.
    # .M.S.MAA..
    # ..A.ASMSM.
    # .M.S.M....
    # ..........
    # S.S.S.S.S.
    # .A.A.A.A..
    # M.M.M.M.M.
    # ..........

