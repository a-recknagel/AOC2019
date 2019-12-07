from itertools import permutations

from util import get_input
from day5 import IntCode


def run_amplifiers(program, phases):
    out = 0
    for phase in phases:
        out = IntCode(program, [phase, out]).run()[0]
    return out


def part_1(data):
    results = []
    for phases in permutations([0, 1, 2, 3, 4]):
        results.append((run_amplifiers(data, phases), phases))
    return max(results, key=lambda x: x[0])[0]


def part_2(data):
    ...


test_1 = [
    [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
    [4, 3, 2, 1, 0]
]
test_2 = [
    [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
    [0, 1, 2, 3, 4]
]
test_3 = [
    [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31,
     4, 31, 99, 0, 0, 0],
    [1, 0, 4, 3, 2]
]

if __name__ == "__main__":
    data_ = [*map(int, get_input("data/day7")[0].split(','))]

    print(f"got {run_amplifiers(*test_1)}, should be 4321")
    print(f"got {run_amplifiers(*test_2)}, should be 54321")
    print(f"got {run_amplifiers(*test_3)}, should be 65210")

    res_1 = part_1(data_, )
    print(f"{res_1=}")
