from collections import deque


def main(n):
    square_index = find_square_index(n)
    coordinate_sequence = generate_square_sequence(square_index)
    coordinate_position = n - (2 * square_index - 1) * (2 * square_index - 1) - 1
    coordinates = coordinate_sequence[coordinate_position]
    return abs(coordinates[0]) + abs(coordinates[1])


def read(f):
    with open(f) as file:
        d = file.read()

    return int(d)


def output(results):
    print(f"The distance is {results}")


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
