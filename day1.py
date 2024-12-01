import pathlib
import os
print(os.getcwd())
from common import get_name, get_puzzle_input, HERE


def part1(list_one: list[int], list_two: list[int]) -> int:
    assert len(list_one) == len(list_two)
    print("Original Lists...")
    print(list_one)
    print(list_two)
    print("Lists sorted")
    sorted_list_one = sorted(list_one)
    sorted_list_two = sorted(list_two)
    print(sorted_list_one)
    print(sorted_list_two)

    distance = 0
    for index in range(len(list_one)):
        l1_val = sorted_list_one[index]
        l2_val = sorted_list_two[index]
        difference = abs(int(l1_val) - int(l2_val))
        print(f"L1 = {l1_val}, L2 = {l2_val} : {difference}")
        distance += difference
        print(f"Distance = {distance}")

    return distance


def part2(list_one: list[int], list_two: list[int]) -> int:
    lookup = {}
    score = 0
    for l1_val in list_one:
        if l1_val in lookup:
            print(f"Already Counted {l1_val}")
            score += int(l1_val) * lookup[l1_val]
            print(f"Score = {score}")
            continue

        occurence = list_two.count(l1_val)
        score += int(l1_val) * occurence
        print(f"Score = {score}")
        lookup[l1_val] = occurence

    print(f"Final Score = {score}")
    return score


def main():
    name = get_name(__file__)
    puzzle_input = f"{name}.txt"
    data = get_puzzle_input(f"{HERE}/{puzzle_input}")
    list1 = []
    list2 = []
    for line in data:
        line = line.rstrip()
        one, two = line.split("   ")
        list1.append(one)
        list2.append(two)

    part1(list1, list2)
    part2(list1, list2)


if __name__ == "__main__":
    main()
