from .checks import contains_unique_elements, contains_no_anagrams


def part_two(n):
    return sum(map(is_valid, n))


def is_valid(l):
    return contains_unique_elements(l) and contains_no_anagrams(l)
