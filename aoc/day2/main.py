from .part_one import part_one
from .part_two import part_two


def main(n):
    return part_one(n), part_two(n)


def read(f):
    with open(f) as file:
        d = file.read()

    return [list(map(int, x.split('\t'))) for x in d.split('\n') if x]


def output(results):
    print(f'The checksum is {results[0]}')
    print(f'The other sum is {results[1]}')
