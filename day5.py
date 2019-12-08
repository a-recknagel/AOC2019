import typing as ty
from collections import deque
from itertools import islice


from util import get_input


class Finished(Exception):
    pass


class NoInput(Exception):
    pass


class IntCode:
    def __init__(self, program: ty.List[int], input: ty.Iterable[int]):
        self.program = program.copy()
        self.input = deque(input)
        self.idx = 0
        self.output = deque()
        self.op_code_map = {
            1: self.add,
            2: self.mul,
            3: self.mov,
            4: self.out,
            5: self.jit,
            6: self.jif,
            7: self.lt,
            8: self.eq,
            99: self.die,
        }

    def resolve_idx(self, offset, mode):
        if mode[offset - 1]:  # instructions progress one further than modes
            ret = self.idx + offset
        else:
            ret = self.program[self.idx + offset]
        return ret

    def add(self, modes):
        noun = self.program[self.resolve_idx(1, modes)]
        verb = self.program[self.resolve_idx(2, modes)]
        self.program[self.resolve_idx(3, modes)] = noun + verb
        self.idx += 4

    def mul(self, modes):
        noun = self.program[self.resolve_idx(1, modes)]
        verb = self.program[self.resolve_idx(2, modes)]
        self.program[self.resolve_idx(3, modes)] = noun * verb
        self.idx += 4

    def mov(self, modes):
        if not self.input:
            raise NoInput
        self.program[self.resolve_idx(1, modes)] = self.input.popleft()
        self.idx += 2

    def out(self, modes):
        self.output.append(self.program[self.resolve_idx(1, modes)])
        self.idx += 2

    def jit(self, modes):
        cond = self.program[self.resolve_idx(1, modes)]
        loc = self.program[self.resolve_idx(2, modes)]
        if cond:
            self.idx = loc
        else:
            self.idx += 3

    def jif(self, modes):
        cond = not self.program[self.resolve_idx(1, modes)]
        loc = self.program[self.resolve_idx(2, modes)]
        if cond:
            self.idx = loc
        else:
            self.idx += 3

    def lt(self, modes):
        noun = self.program[self.resolve_idx(1, modes)]
        verb = self.program[self.resolve_idx(2, modes)]
        self.program[self.resolve_idx(3, modes)] = int(noun < verb)
        self.idx += 4

    def eq(self, modes):
        noun = self.program[self.resolve_idx(1, modes)]
        verb = self.program[self.resolve_idx(2, modes)]
        self.program[self.resolve_idx(3, modes)] = int(noun == verb)
        self.idx += 4

    def die(self, _):
        raise Finished

    def parse_instructions(self):
        instruction = str(self.program[self.idx])
        if len(instruction) == 1:  # pad
            instruction = f"0{instruction}"
        yield int(instruction[-2:])
        yield from map(int, reversed(instruction[:-2]))
        while True:
            yield 0

    def step(self):
        op_code, *modes = islice(self.parse_instructions(), 6)  # there can't be too many modes
        self.op_code_map[op_code](modes)

    def run(self):
        while True:
            try:
                self.step()
            except Finished:
                return self.output


def part_1():
    test_1_1 = IntCode([1002, 4, 3, 4, 33], [1]).run()
    print(f"{test_1_1=}")
    test_1_2 = IntCode([3, 0, 4, 0, 99], [1]).run()
    print(f"{test_1_2=}")

    data = list(map(int, get_input("data/day5")[0].split(',')))
    res_1 = IntCode(data, [1]).run()
    print(f"{res_1=}")


def part_2():
    test_2_1 = IntCode([
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [7]).run()[0]
    print(f"{test_2_1=}")
    test_2_2 = IntCode([
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [8]).run()[0]
    print(f"{test_2_2=}")
    test_2_3 = IntCode([
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [9]).run()[0]
    print(f"{test_2_3=}")

    data = list(map(int, get_input("data/day5")[0].split(',')))
    res_2 = IntCode(data, [5]).run()[0]
    print(f"{res_2=}")


if __name__ == "__main__":
    part_1()
    part_2()
