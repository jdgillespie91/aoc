from aoc.day1.part_one import part_one
from aoc.day1.part_two import part_two


def main(n):
    return part_one(n), part_two(n)


def read(f):
    with open(f) as file:
        d = file.read()

    return int(d)


def output(results):
    print(f'Summing equal consecutive integers gives: {results[0]}')
    print(f'Summing equal halfway integers gives: {results[1]}')
