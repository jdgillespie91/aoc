from .part_one import steps_to_leave
from .part_two import steps_to_leave_part_two


def main(n):
    return steps_to_leave([x for x in n]), steps_to_leave_part_two([x for x in n])


def read(f):
    with open(f) as file:
        d = file.read()

    return [int(x) for x in d.split('\n') if x]


def output(results):
    print(f"The number of steps required is {results}")
