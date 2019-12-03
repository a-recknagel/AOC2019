from typing import Callable


def get_input(loc, func: Callable = str, strip=True):
    with open(loc) as data:
        return [func(line.strip() if strip else line) for line in data]


def intcode(data):
    for idx in range(0, len(data), 4):
        opcode, source_1, source_2, target = data[idx:idx+4]
        if opcode == 99:
            break
        elif opcode == 1:
            data[target] = data[source_1] + data[source_2]
        elif opcode == 2:
            data[target] = data[source_1] * data[source_2]
        else:
            raise RuntimeError(f'Bad data, invalid {opcode=}.')


def part_1(data):
    local_data = data.copy()
    local_data[1], local_data[2] = 12, 2
    intcode(local_data)
    return local_data[0]


def part_2(data):
    for noun in range(100):
        for verb in range(100):
            local_data = data.copy()
            local_data[1], local_data[2] = noun, verb
            intcode(local_data)
            if local_data[0] == 19690720:
                return 100 * noun + verb
    else:
        raise RuntimeError('Found no valid noun/verb combination.')


if __name__ == "__main__":
    data_ = [int(x) for x in get_input("data/day2")[0].split(',')]

    res_1 = part_1(data_)
    print(f"{res_1=}")

    res_2 = part_2(data_)
    print(f"{res_2=}")
