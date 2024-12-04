import pathlib
import os
import re
print(os.getcwd())
from common import get_name, get_puzzle_input, HERE


def part1(coords) -> int:
    # answer is 2569
    xmases = 0
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            strings_to_check = []

            if i > 2:
                print("Checking UP")
                a_string_to_check = "".join([coords[i][j], coords[i-1][j], coords[i-2][j], coords[i-3][j]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            if i > 2 and j < (len(coords[i]) - 3):
                print("Checking UP/RIGHT")
                a_string_to_check = "".join([coords[i][j], coords[i-1][j+1], coords[i-2][j+2], coords[i-3][j+3]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            if j < (len(coords[i]) - 3):
                print("Checking RIGHT")
                a_string_to_check = "".join([coords[i][j], coords[i][j+1], coords[i][j+2], coords[i][j+3]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            if i < (len(coords) - 3) and j < (len(coords[i]) - 3):
                print("Checking DOWN/RIGHT")
                a_string_to_check = "".join([coords[i][j], coords[i+1][j+1], coords[i+2][j+2], coords[i+3][j+3]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            if i < (len(coords) - 3):
                print("Checking DOWN")
                a_string_to_check = "".join([coords[i][j], coords[i+1][j], coords[i+2][j], coords[i+3][j]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            if i < (len(coords) - 3) and j > 2:
                print("Checking DOWN/LEFT")
                a_string_to_check = "".join([coords[i][j], coords[i+1][j-1], coords[i+2][j-2], coords[i+3][j-3]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            if j > 2:
                print("Checking LEFT")
                a_string_to_check = "".join([coords[i][j], coords[i][j-1], coords[i][j-2], coords[i][j-3]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            if i > 2 and j > 2:
                print("Checking LEFT/UP")
                a_string_to_check = "".join([coords[i][j], coords[i-1][j-1], coords[i-2][j-2], coords[i-3][j-3]])
                print(i, j, a_string_to_check)
                strings_to_check.append(a_string_to_check)

            for a_string in strings_to_check:
                if a_string == "XMAS":
                    xmases += 1

    return xmases


def part2(coords) -> int:
    # answer is 1998
    xmases = 0
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            if coords[i][j] != "A":
                continue

            # Out of bounds check
            if i < 1:
                continue
            if j < 1:
                continue
            if j >= len(coords[i]) - 1:
                continue
            if i >= len(coords) - 1:
                continue

            print("Checking MM / A / SS")
            if coords[i-1][j-1] == "M" and coords[i-1][j+1] == "M" and coords[i+1][j-1] == "S" and coords[i+1][j+1] == "S":
                print("Found!")
                xmases += 1

            print("Checking SM / A / MS")
            if coords[i-1][j-1] == "S" and coords[i-1][j+1] == "M" and coords[i+1][j-1] == "S" and coords[i+1][j+1] == "M":
                print("Found!")
                xmases += 1

            print("Checking SS / A / MM")
            if coords[i-1][j-1] == "S" and coords[i-1][j+1] == "S" and coords[i+1][j-1] == "M" and coords[i+1][j+1] == "M":
                print("Found!")
                xmases += 1

            print("Checking MS / A / SM")
            if coords[i-1][j-1] == "M" and coords[i-1][j+1] == "S" and coords[i+1][j-1] == "M" and coords[i+1][j+1] == "S":
                print("Found!")
                xmases += 1

    return xmases


def main():
    name = get_name(__file__)
    puzzle_input = f"{name}.txt"
    data = get_puzzle_input(f"{HERE}/{puzzle_input}")
    a_list = []
    for line in data:
        line = line.rstrip()
        a_list.append(line)

    # answer = part1(a_list)
    # print(answer)
    #
    pt2_answer = part2(a_list)
    print(pt2_answer)


if __name__ == "__main__":
    main()
