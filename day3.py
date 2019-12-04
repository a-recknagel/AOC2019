from itertools import zip_longest

from util import get_input


def map_path(wire):
    x, y, tick = 0, 0, 1
    for instruction in wire:
        loc, amount = instruction[0], int(instruction[1:])
        ticks = range(tick, tick := tick + abs(amount))
        if loc == "U":
            path = zip_longest((), range(y + 1, (y := y + amount) + 1), ticks, fillvalue=x)
        elif loc == "R":
            path = zip_longest(range(x + 1, (x := x + amount) + 1), (), ticks, fillvalue=y)
        elif loc == "D":
            path = zip_longest((), range(y - 1, (y := y - amount) - 1, -1), ticks, fillvalue=x)
        elif loc == "L":
            path = zip_longest(range(x - 1, (x := x - amount) - 1, -1), (), ticks, fillvalue=y)
        else:
            raise ValueError(f"Got wrong {loc=}.")
        yield from path


def part_1(first, second):
    wire_path = {(x, y) for x, y, _ in map_path(first)}
    distances = [abs(x) + abs(y) for x, y, _ in map_path(second) if (x, y) in wire_path]
    return min(distances)


def part_2(first, second):
    wire_path = {(x, y): tick for x, y, tick in map_path(first)}
    durations = [
        tick + wire_path[(x, y)]
        for x, y, tick in map_path(second)
        if (x, y) in wire_path
    ]
    return min(durations)


test_1 = (
    ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
    ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
)
test_2 = (
    ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
    ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
)

if __name__ == "__main__":
    wire_1, wire_2 = [wire.split(",") for wire in get_input("data/day3")]

    test_1_1 = part_1(*test_1)
    print(f"{test_1_1=}")

    test_1_2 = part_1(*test_2)
    print(f"{test_1_2=}")

    res_1 = part_1(wire_1, wire_2)
    print(f"{res_1=}")

    test_2_1 = part_2(*test_1)
    print(f"{test_2_1=}")

    test_2_2 = part_2(*test_2)
    print(f"{test_2_2=}")

    res_2 = part_2(wire_1, wire_2)
    print(f"{res_2=}")
