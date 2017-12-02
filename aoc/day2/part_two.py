from itertools import product


def part_two(n):
    quotients = list(map(find_integer_quotient, n))
    return 'N/A' if -1 in quotients else sum(quotients)


def is_integer_quotient(pair):
    q = pair[0] / pair[1]

    if q == int(q):
        return True, q

    if 1 / q == int(1 / q):
        return True, 1 / q

    return False, 0


def generate_pairs(row):
    count = 0
    length = len(row)
    all_pairs = product(row, row)

    while count < length * length:
        count += 1
        pair = next(all_pairs)

        if count % (length + 1) == 1:
            continue

        yield pair


def find_integer_quotient(row):
    pairs = generate_pairs(row)

    for pair in pairs:
        is_integer, quotient = is_integer_quotient(pair)
        if is_integer:
            return int(quotient)

    return -1