import copy


def main(n):
    return cycle_with_set(n)


def read(f):
    with open(f) as file:
        d = file.read()

    return [int(x) for x in d.split('\t') if x]


def output(results):
    print(f"The number of cycles is: {results[0]}")
    print(f"The length of the cycle is: {results[1]}")


def cycle_with_set(banks):
    b = copy.copy(banks)
    seen_states = {','.join([str(x) for x in b])}
    state_position = {','.join([str(x) for x in b]): 0}

    while True:
        b = reallocate(b)

        if ','.join([str(x) for x in b]) in seen_states:
            return len(seen_states), len(seen_states) - state_position[','.join([str(x) for x in b])]

        state_position[','.join([str(x) for x in b])] = len(seen_states)
        seen_states.add(','.join([str(x) for x in b]))


def reallocate(banks):
    banks_copy = copy.copy(banks)

    blocks, index = max(banks), banks.index(max(banks))
    banks_copy[index] = 0

    while blocks:
        banks_copy[(index + 1) % len(banks)] += 1
        index += 1
        blocks -= 1

    return banks_copy
