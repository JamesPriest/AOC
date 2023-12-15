from functools import cache

def parse_input(data):
    data = data.split('\n')
    data = list(map(list, data))
    if len(data[-1]) == 0:
        data = data[:-1]
    return data

def calculate_rocks(data):
    val = sum([i.count('O')*(len(i)-idx) for idx, i in enumerate(data)])
    return val


def print_rocks(data):
    print('\n'.join([''.join(i) for i in data]))


def rotate_data(data):
    rotated_data = list(zip(*data[::-1]))
    return rotated_data


def matrix_to_str(inp):
    str_repr = '\n'.join(''.join(i) for i in inp)
    return str_repr


def str_to_matrix(inp):
    matrix = list(map(list, inp.split('\n')))
    return matrix


@cache
def perform_cycle(d2):
    d2 = str_to_matrix(d2)
    for _ in range(4):
        d2 = rotate_data(rotate(d2))
    d2 = matrix_to_str(d2)
    return d2


def rotate(data):
    i, j = 1, 0
    rotated_data = [[item for item in data[0]]]
    while i < len(data):
        # print(f"i: {i}, j:{j}")
        rotated_data.append([item for item in data[i]])
        # print(rotated_data)
        while j < len(data[0]):
            # print(f"i: {i}, j:{j}")
            symbol = data[i][j]
            if symbol == 'O':
                # print(f"Working on slot ({i}, {j})")
                for k in range(0, i+1)[::-1]:
                    # print(f"k: {k}")
                    # print(f"Found symbol ({rotated_data[i][j]}) at ({i}, {j})")
                    if k==0 and rotated_data[k][j] == '.':
                        # print(f"Found an empty slot at the top of at ({k}, {j}) ==> Pushing Boulder Up and replace ({i}, {j}) with a '.' symbol")
                        # Top row, so if I can place it I will
                        rotated_data[k][j] = symbol
                        rotated_data[i][j] = '.'
                        break
                    elif rotated_data[k-1][j] == '#' or rotated_data[k-1][j] == 'O':
                        # print('\n'.join([''.join(pp) for pp in rotated_data]))
                        # print()
                        # print(f"found a block above at ({k-1}, {j}) =>  {rotated_data[k-1][j]} ==> Found a block or another placing it at ({k}, {j})")
                        # Cell above me has a block so place it
                        rotated_data[k][j] = 'O'
                        if k != i:
                            rotated_data[i][j] = '.'
                        # print()
                        break
                    elif rotated_data[k-1][j] == '.':
                        # Can go one higher! Go the next k!
                        # print("Found a slot - so we check a higher value\n")
                        continue
            j+=1
        # print('\n'.join([''.join(pp) for pp in rotated_data]))
        # print()
        j = 0
        i+=1
    return rotated_data


if __name__ == '__main__':
    test = """O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#...."""

    outcome = """OOOO.#.O..
    OO..#....#
    OO..O##..O
    O..#.OO...
    ........#.
    ..#....#.#
    ..O..#.O.O
    ..O.......
    #....###..
    #....#...."""

    test_data = parse_input(test)
    rotated_data = rotate(test_data)
    assert outcome == rotated_test

    with open("input.txt", "r") as f:
        data = f.read()

    data = parse_input(data)
    rotated_data = rotate(data)
    print(f"Part 1: {calculate_rocks(rotated_data)}")

    # c = matrix_to_str(b)
    # examples = [perform_cycle(c)]
    # for _ in range(1_000_000_000):
    #     examples.append(perform_cycle(examples[-1]))

    outcome = [perform_cycle(matrix_to_str(data))]
    # for _ in range(1_000_00):
    while len(outcome) < 1_000_000_000:
        outcome.append(perform_cycle(outcome[-1]))

    print(f"Part 2: {calculate_rocks(str_to_matrix(outcome[-1]))}")