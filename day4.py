from util import get_input


def part_1(start, end):
    ret = []
    for pw in map(str, range(start, end+1)):
        if any(pw[idx] > pw[idx+1] for idx in range(5)):
            continue
        if max(pw.count(x) for x in pw) < 2:
            continue
        ret.append(pw)
    return len(ret)


def part_2(start, end):
    ret = []
    for pw in map(str, range(start, end+1)):
        if any(pw[idx] > pw[idx+1] for idx in range(5)):
            continue
        if 2 not in [pw.count(x) for x in pw]:
            continue
        ret.append(pw)
    return len(ret)


if __name__ == "__main__":
    data = list(map(int, get_input("data/day4")[0].split('-')))

    res_1 = part_1(*data)
    print(f"{res_1=}")

    res_2 = part_2(*data)
    print(f"{res_2=}")
