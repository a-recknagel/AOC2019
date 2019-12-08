from itertools import permutations

from util import get_input
from day5 import IntCode, NoInput, Finished


def amplifier_chain(program, phases):
    out = 0
    for phase in phases:
        out = IntCode(program, [phase, out]).run()[0]
    return out


def amplifier_loop(program, phases):
    # set up amplifier feedback loop
    phases = iter(phases)
    amplifiers = [IntCode(program, [next(phases), 0])]
    for phase in phases:
        amplifiers.append(IntCode(program, [phase]))
        amplifiers[-2].output = amplifiers[-1].input
    amplifiers[-1].output = amplifiers[0].input

    # run their loop by hand to handle i/o
    current = 0
    # count = 0
    while True:
        # if not(count % 100000):
        #     print(count)
        #     for amplifier in amplifiers:
        #         print(amplifier.program)
        # count += 1
        try:
            amplifiers[current].step()
        except NoInput:
            current = (current + 1) % len(amplifiers)
        except Finished:
            if current == len(amplifiers):
                return amplifiers[current].output


def part_1(data):
    return max(amplifier_chain(data, phase) for phase in permutations([0, 1, 2, 3, 4]))


def part_2(data):
    return max(amplifier_chain(data, phase) for phase in permutations([5, 6, 7, 8, 9]))


test_1_1 = [
    [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
    [4, 3, 2, 1, 0]
]
test_1_2 = [
    [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
    [0, 1, 2, 3, 4]
]
test_1_3 = [
    [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31,
     4, 31, 99, 0, 0, 0],
    [1, 0, 4, 3, 2]
]
test_2_1 = [
    [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
     27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5],
    [9, 8, 7, 6, 5]
]
test_2_2 = [
    [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
     -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
     53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10],
    [9, 7, 8, 5, 6]
]

if __name__ == "__main__":
    data_ = [*map(int, get_input("data/day7")[0].split(','))]

    print(f"got {amplifier_chain(*test_1_1)}, should be 4321")
    print(f"got {amplifier_chain(*test_1_2)}, should be 54321")
    print(f"got {amplifier_chain(*test_1_3)}, should be 65210")

    res_1 = part_1(data_, )
    print(f"{res_1=}")

    # TODO: get the stuff below this line to work

    print(f"got {amplifier_loop(*test_2_1)}, should be 139629729")
    print(f"got {amplifier_loop(*test_2_2)}, should be 18216")

    res_2 = part_2(data_, )
    print(f"{res_2=}")
