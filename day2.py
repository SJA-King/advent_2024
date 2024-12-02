import pathlib
import os
print(os.getcwd())
from common import get_name, get_puzzle_input, HERE


def part1(the_list) -> int:
    # Answer was 510
    print("Original List...")
    print(the_list)

    safe = 0
    safe_lines = []
    not_safe_lines = []
    for line in the_list:
        is_safe = True
        levels = line.split(" ")
        print(levels)

        last_level = int(levels[0])
        diff_list = []
        for level in levels[1:]:

            diff = last_level - int(level)
            diff_list.append(diff)

            print(f"Diff = {diff}")
            if abs(diff) < 1 or abs(diff) > 3:
                print("Not Safe")
                is_safe = False
                break

            last_level = int(level)

        if is_safe:
            ascending = True
            if not all(0 <= i for i in diff_list):
                print("Not All Ascending!")
                ascending = False
            # if diff_list[0] < 0:
            descending = True
            if not all(i < 0 for i in diff_list):
                print("Not ALL Descending!")
                descending = False

            if not descending and not ascending:
                print("Not All Ascending OR Descending! - Not Safe")
                is_safe = False

        if is_safe:
            print(f"'{line}' IS Safe!")
            safe += 1
            safe_lines.append(line)
        else:
            not_safe_lines.append(line)

    with open(HERE / "day2_safe.txt", "w") as ds:
        ds.write("\n".join(safe_lines))

    with open(HERE / "day2_notsafe.txt", "w") as ds:
        ds.write("\n".join(not_safe_lines))

    return safe


def part2(the_list) -> int:
    # Answer is 553 (with 510 from previous ofc)
    safe = 0
    for line in the_list:

        orig_levels = line.split(" ")

        # bad_level = 0
        for idx in range(len(orig_levels)):
            is_safe = True
            print(f"Before - {orig_levels}")
            levels = orig_levels.copy()
            del levels[idx]
            print(f"After - {levels}")

            # if bad_level > 1:
            #     print("Totally Unsafe!")
            #     break

            last_level = int(levels[0])
            diff_list = []
            for level in levels[1:]:

                diff = last_level - int(level)
                diff_list.append(diff)

                print(f"Diff = {diff}")
                if abs(diff) < 1 or abs(diff) > 3:
                    print("Not Safe")
                    is_safe = False
                    break

                last_level = int(level)

            if is_safe:
                ascending = True
                if not all(0 <= i for i in diff_list):
                    print("Not All Ascending!")
                    ascending = False
                # if diff_list[0] < 0:
                descending = True
                if not all(i < 0 for i in diff_list):
                    print("Not ALL Descending!")
                    descending = False

                if not descending and not ascending:
                    print("Not All Ascending OR Descending! - Not Safe")
                    is_safe = False

            if is_safe:
                print(f"'{line}' IS 'Dampened' Safe!")
                safe += 1
                break

    return safe


def main():
    name = get_name(__file__)
    puzzle_input = f"{name}.txt"
    data = get_puzzle_input(f"{HERE}/{puzzle_input}")
    a_list = []
    for line in data:
        line = line.rstrip()
        a_list.append(line)

    answer = part1(a_list)
    print(answer)

    data = get_puzzle_input(f"{HERE}/{name}_notsafe.txt")
    a_list = []
    for line in data:
        line = line.rstrip()
        a_list.append(line)
    pt2_answer = part2(a_list)
    print(pt2_answer + answer)


if __name__ == "__main__":
    main()
