from aoc.day3 import main
from aoc.day3.main import generate_square_sequence, find_square_index


def test_generate_square_sequence():
    assert generate_square_sequence(0) == [(0, 0)]
    assert generate_square_sequence(1) == [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    assert generate_square_sequence(2) == [
        (2, -1), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (-1, 2), (-2, 2), (-2, 1),
        (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2)
    ]


def test_find_square_index():
    assert 0 == find_square_index(1)
    assert 1 == find_square_index(4)
    assert 2 == find_square_index(12)
    assert 2 == find_square_index(18)


def test_examples():
    assert 0 == main(1)
    assert 3 == main(12)
    assert 2 == main(23)
    assert 31 == main(1024)


def test_puzzle():
    assert 438 == main(265149)
