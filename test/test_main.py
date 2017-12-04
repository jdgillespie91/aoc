from aoc.main import main


def test_puzzles():
    assert (1119, 1420) == main(1, 'data/day1.txt')
    assert (44887, 242) == main(2, 'data/day2.txt')
    assert 438 == main(3, 'data/day3.txt')
    assert (466, 251) == main(4, 'data/day4.txt')
