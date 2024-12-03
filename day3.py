import pathlib
import os
import re
print(os.getcwd())
from common import get_name, get_puzzle_input, HERE


def part1(instructions) -> int:
    # answer is 163931492
    total = 0
    for instruction_line in instructions:
        ins_values = re.findall("mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)", instruction_line)
        for a_value_pair in ins_values:
            val_1, val_2 = a_value_pair
            val_1 = int(val_1)
            val_2 = int(val_2)
            multi = val_1 * val_2
            total += multi
            print(val_1, val_2, multi, f"New Total = {total}")

    return total


def part2(instructions) -> int:
    total = 0
    for line_idx in range(len(instructions)):
        donts = instructions[line_idx].count("don't")
        print(f"Line: {line_idx} there are {donts} don't")

        line_without_dont = instructions[line_idx].split("don't")
        print(f"Line 'Without' don;t = {line_without_dont}")
        print(line_without_dont[0])
        total += part1([line_without_dont[0]])

        for a_part in line_without_dont:
            if "do()" in a_part:
                dos = a_part.split("do()")
                print(f"Dos = {dos}")
                for a_do in dos[1:]:
                    print(f"A Do = {a_do}")
                    total += part1([a_do])

    return total


def main():
    name = get_name(__file__)
    puzzle_input = f"{name}.txt"
    # data = get_puzzle_input(f"{HERE}/{puzzle_input}")
    # a_list = []
    # for line in data:
    #     line = line.rstrip()
    #     a_list.append(line)
    #
    # answer = part1(a_list)
    # print(answer)
    #
    # pt2_answer = part2(a_list)
    # print(pt2_answer)
    import re

    with open(f"{HERE}/{puzzle_input}") as f:
        memory = f.read()

    def my_func(raw):
        inp = re.findall("mul\(\d+,\d+\)", raw)
        f_result = 0
        for i in inp:
            a = i.split(',')
            first = a[0][4:]
            second = a[1][:-1]
            f_result += int(first) * int(second)
        return f_result

    result = my_func(memory)
    print(result)

    new_result = 0
    while True:
        no = memory.find("don't()")
        if no == -1:
            break
        chunk = memory[:no]
        rest = memory[no:]
        new_result += my_func(chunk)
        yes = rest.find("do()")
        if yes == -1:
            break
        memory = rest[yes:]

    print(new_result)


if __name__ == "__main__":
    main()
