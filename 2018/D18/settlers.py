from pathlib import Path


def process_ground(raw):
    """

    raw : 3x3 grid (list)
    """
    tree_count = 0
    for row in raw:
        for col in row:
            if col == "|":
                tree_count += 1
    return "." if tree_count < 3 else "|"


def process_trees(raw):
    lumberyard_count = 0
    for row in raw:
        for col in row:
            if col == "#":
                lumberyard_count += 1
    return "|" if lumberyard_count < 3 else "#"


def print_matrix(data):
    for row in data:
        print(''.join(row))

def process_lumberyard(raw):
    lumberyard_count, tree_count = 0, 0
    for row in raw:
        for col in row:
            if col == "|":
                tree_count += 1
            elif col == "#":
                lumberyard_count += 1
    #print_matrix(raw)
    #print(f"Lumberyard count: {lumberyard_count}, tree_count: {tree_count}")
    #print(f"Process to get {'#' if (lumberyard_count > 0 and tree_count > 0) else '.'}\n")
    # Note counting its own lumberyard, so we need more than 1
    return "#" if (lumberyard_count > 1 and tree_count > 0) else "."


process_mapper = {".": process_ground, "|": process_trees, "#": process_lumberyard}


def step_state(current_state):
    new_state = []
    # Assume input will be a square
    rows, cols = len(current_state), len(current_state[0])
    for row in range(rows):
        new_row = []
        for col in range(cols):

            subset = list(
                map(
                    lambda x: x[(col - 1 if col > 0 else 0) : col + 2],
                    current_state[row - 1 if row > 0 else 0 : row + 2],
                )
            )
            # print(f"Row: {row}, col: {col}")
            new_value = process_mapper[current_state[row][col]](subset)

            new_row.append(new_value)
        new_state.append(new_row)

    return new_state


# def process_input(data):

if __name__ == "__main__":
    filename = "input.txt"
    filepath = Path(filename)

    if filepath.exists():
        initial_state = [
            [j for j in i] for i in open(filepath).read().split("\n") if len(i) > 0
        ]

    TEN_MINUTES = 10

    state = initial_state
    for minute in range(TEN_MINUTES):
        print(f"Minute: {minute}")
        for row in state:
            print("".join(row))
        state = step_state(state)

    trees, lumberyards = 0, 0
    for row in state:
        for col in row:
            if col == "|":
                trees += 1
            elif col == "#":
                lumberyards += 1

    print(f"Part 1: {trees*lumberyards}")


"""
Note for borders, pad the edges...actually no

"""
