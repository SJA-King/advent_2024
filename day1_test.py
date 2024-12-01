# import sys
# # sys.path.append("..")
from day1 import part1, part2
# from


def test_part1():
    list1 = [3,4,2,1,3,3]
    list2 = [4,3,5,3,9,3]

    assert part1(list1, list2) == 11


def test_part2():
    list1 = [3,4,2,1,3,3]
    list2 = [4,3,5,3,9,3]

    assert part2(list1, list2) == 31