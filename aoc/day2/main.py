def main(n):
    return first_half(n), second_half(n)


def read(f):
    with open(f) as file:
        d = file.read()

    return [list(map(int, x.split('\t'))) for x in d.split('\n') if x]


def output(results):
    print(f'The checksum is {results[0]}')
    print(f'The other sum is {results[1]}')


def first_half(n):
    return sum([max(row) - min(row) for row in n])


def second_half(n):
    total = 0

    for row in n:
        for index, a in enumerate(row):
            found = 0

            for b in row[index + 1:]:
                if a % b == 0:
                    quotient = a / b
                elif b % a == 0:
                    quotient = b / a
                else:
                    quotient = 0

                if quotient:
                    found = 1
                    total += quotient
                    break

            if found:
                break

        if not found:
            # print(f'The following row has no two integers for which one evenly divides the other: {row}')
            return 'N/A'

    return int(total)
