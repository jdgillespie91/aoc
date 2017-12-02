from functools import reduce


def main(n):
    return first_half(n), second_half(n)


def read(f):
    with open(f) as file:
        d = file.read()

    return int(d)


def output(results):
    print(f'Summing equal consecutive integers gives: {results[0]}')
    print(f'Summing equal halfway integers gives: {results[1]}')


def first_half(n):
    integer_list = list(int(x) for x in str(n) + str(n)[0])
    consecutive_pairs = zip(integer_list, integer_list[1:])
    matching_consecutive_pairs = filter(lambda x: x[0] == x[1], consecutive_pairs)
    return reduce(lambda x, y: x + y[0], matching_consecutive_pairs, 0)


def second_half(n):
    l = int(len(str(n)) / 2)
    integer_list = list(int(x) for x in str(n) + str(n)[:l])
    consecutive_pairs = zip(integer_list, integer_list[l:])
    matching_consecutive_pairs = filter(lambda x: x[0] == x[1], consecutive_pairs)
    return reduce(lambda x, y: x + y[0], matching_consecutive_pairs, 0)
