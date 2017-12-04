from .checks import contains_unique_elements


def part_one(n):
    return sum(map(is_valid, n))


def is_valid(l):
    return contains_unique_elements(l)
