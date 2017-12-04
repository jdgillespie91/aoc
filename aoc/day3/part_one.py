from collections import deque


def part_one(n):
    return distance(find_coordinates(n))


def find_coordinates(n):
    i = find_square_index(n)
    seq = generate_square_sequence(i)
    return seq[n - (2 * i - 1) ** 2 - 1]


def distance(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])


def find_square_index(n):
    i = 0
    root = 2 * i + 1

    while n > root * root:
        i += 1
        root = 2 * i + 1

    return i


def generate_square_sequence(i):
    if i == 0:
        return [(0, 0)]

    seq = deque([i] * (2 * i - 1) + list(range(i, -i - 1, -1)) + [-i] * (2 * i - 1) + list(range(-i, i + 1)))

    x = seq.copy()
    y = seq.copy()
    y.rotate(2 * i)

    return list(zip(x, y))
