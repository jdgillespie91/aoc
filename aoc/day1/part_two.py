from functools import reduce


def part_two(n):
    l = int(len(str(n)) / 2)
    integer_list = list(int(x) for x in str(n) + str(n)[:l])
    consecutive_pairs = zip(integer_list, integer_list[l:])
    matching_consecutive_pairs = filter(lambda x: x[0] == x[1], consecutive_pairs)
    return reduce(lambda x, y: x + y[0], matching_consecutive_pairs, 0)