from .part_one import part_one


def main(n):
    return part_one(n)


def read(f):
    with open(f) as file:
        d = file.read()

    return int(d)


def output(results):
    print(f"The distance is {results}")
