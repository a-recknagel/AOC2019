import typing as ty

from util import get_input


class Node:
    nodes: ty.Dict[str, 'Node'] = {}

    def __init__(self, name: str):
        self.name = name
        self.parent: ty.Optional['Node'] = None

    def __repr__(self):
        return self.name

    def ancestors(self) -> ty.Iterator['Node']:
        while (self := self.parent) is not None:
            yield self

    @classmethod
    def parse(cls, orbits: ty.Iterable[ty.Tuple[str, str]]):
        cls.nodes = {}
        for parent, child in orbits:
            if parent not in cls.nodes:
                cls.nodes[parent] = cls(parent)
            if child not in cls.nodes:
                cls.nodes[child] = cls(child)
        for parent, child in orbits:
            cls.nodes[child].parent = cls.nodes[parent]


def part_1(data):
    orbits = [tuple(line.split(")")) for line in data]
    Node.parse(orbits)
    return sum([len([*n.ancestors()]) for n in Node.nodes.values()])


def part_2(data):
    orbits = [tuple(line.split(")")) for line in data]
    Node.parse(orbits)
    for count_you, n_you in enumerate(Node.nodes["YOU"].ancestors()):
        for count_san, n_san in enumerate(Node.nodes["SAN"].ancestors()):
            if n_you == n_san:
                return count_you + count_san


test_data_1 = """\
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split('\n')

test_data_2 = """\
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".split('\n')


if __name__ == "__main__":
    data_ = get_input("data/day6")

    test_1_1 = part_1(test_data_1)
    print(f"{test_1_1=}")

    test_2_1 = part_2(test_data_2)
    print(f"{test_2_1=}")

    res_1 = part_1(data_)
    print(f"{res_1=}")

    res_2 = part_2(data_)
    print(f"{res_2=}")
