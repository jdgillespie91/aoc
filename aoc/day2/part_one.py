def part_one(n):
    return sum(map(find_difference, n))


def find_difference(row):
    return max(row) - min(row)