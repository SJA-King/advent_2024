

import pathlib

HERE = pathlib.Path(__file__).parent


def get_name(name):
    file_name = pathlib.Path(name).stem
    print(f"Im {file_name}")
    return file_name


def get_puzzle_input(file_name: str) -> list:
    with open(file_name, "r") as fn:
        return fn.readlines()
