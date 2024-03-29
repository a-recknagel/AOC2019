from util import get_input


def part_1(data):
    return sum(val // 3 - 2 for val in data)


def part_2(data):
    acc = 0
    for val in data:
        while (val := val // 3 - 2) > 0:
            acc += val
    return acc


if __name__ == "__main__":
    data_ = get_input("data/day1", func=int)

    res_1 = part_1(data_)
    print(f"{res_1=}")

    res_2 = part_2(data_)
    print(f"{res_2=}")
