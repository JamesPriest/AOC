import copy 


def get_empty_rows(space):
    empty_row_idx = [idx for idx, row in enumerate(space) if all(map(lambda x : x=='.', row))]
    return empty_row_idx


def get_empty_columns(space):
    empty_col_idx = [col_num for col_num in range(len(space[0])) if all(map(lambda x: x=='.', [i[col_num] for i in space]))]
    return empty_col_idx


def expand_space(_data, factor=1):
    # Example
    """
    #.........
    .......... <== **
    ......#...

    ** This is empty on the horizontal and so is row is double, so instead of 
    counting for 1 row, it'll count for two rows.

    Note: This only works for part 1
    """
    data = copy.deepcopy(_data)

    # Identify which rows and columns to expand
    # Row first
    rows_to_transform = get_empty_rows(data)

    # Column next
    columns_to_transform = get_empty_columns(data)

    # Perform the expansion
    # Row level expansion
    new_row = ['.' for _ in range(len(data[0]))]
    for row in rows_to_transform[::-1]:
        for _ in range(factor):
            data.insert(row, copy.copy(new_row))
    
    # Column level expansion
    # Run the addition columns in reverse as if we add 
    # a new column to column 2 then if we need to add on
    # to column 5, it's now column 6
    for col in columns_to_transform[::-1]:
        for i in data:
            for _ in range(factor):
                i.insert(col+1, '.')
    
    # Return the new data
    return data


def calculate_distance(galaxy_1, galaxy_2, empty_rows, empty_columns, factor = 1):
    """
    galaxy_1: (x, y)

    galaxy_2: (x, y)

    empty_rows: List[Int]

    empty_columns: List[Int]

    factor: Int
    """
    g1_x, g1_y = galaxy_1
    g2_x, g2_y = galaxy_2
    dist_1 = abs(g1_x - g2_x) + (factor-1) * sum([1 for i in empty_rows if i > min(g1_x, g2_x) and i < max(g1_x, g2_x)])
    dist_2 = abs(g1_y - g2_y) + (factor-1) * sum([1 for i in empty_columns if i > min(g1_y, g2_y) and i < max(g1_y, g2_y)])
    return dist_1 + dist_2


def parse_input(data):
    data = data.split('\n')
    data = list(map(list, data))
    return data


def get_galaxies(data):
    galaxies = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j]=='#']
    galaxy_hashmap = {idx: i for idx, i in enumerate(galaxies)}
    return galaxy_hashmap


def tuple_abs_difference_sum(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])


###############################
#                             #
# Test data                   #
#                             #
###############################
test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


test_parsed = parse_input(test_data)
test_expansion = expand_space(test_parsed)
test_expansion_repr = '\n'.join([''.join(i) for i in test_expansion])

outcome = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""

# 
assert test_expansion_repr == outcome

test_galax = get_galaxies(test_expansion)
analysis_pairs = [tuple_abs_difference_sum(test_galax[i], test_galax[j]) for i in test_galax.keys() for j in range(i)]
assert sum(analysis_pairs) == 374


###############################
#                             #
# Part 1                      #
#                             #
###############################
with open("input.txt", "r") as f:
    data = f.read()
    data = parse_input(data)

expansion = expand_space(data)
galax = get_galaxies(expansion)
analysis_pairs = [tuple_abs_difference_sum(galax[i], galax[j]) for i in galax.keys() for j in range(i)]


# Part 2
test_expansion_pt2 = expand_space(test_parsed, factor=(100-1))
test_expansion_pt2_repr = '\n'.join([''.join(i) for i in test_expansion_pt2])
test_galax_pt2 = get_galaxies(test_expansion_pt2)
analysis_pairs_pt2 = [tuple_abs_difference_sum(test_galax_pt2[i], test_galax_pt2[j]) for i in test_galax_pt2.keys() for j in range(i)]
print(f"\nPart 2 - result: {sum(analysis_pairs_pt2)}")

## Okay do not do this, it will not run
# expansion = expand_space(data, factor = (1_000_000 - 1))
# galax = get_galaxies(expansion)
# analysis_pairs = [tuple_abs_difference_sum(galax[i], galax[j]) for i in galax.keys() for j in range(i)]
# print(sum(analysis_pairs))

###############################
#                             #
# Part 2                      #
#                             #
###############################
tg = get_galaxies(test_parsed)
tc = get_empty_columns(test_parsed)
tr = get_empty_rows(test_parsed)
test_1 = [calculate_distance(tg[i], tg[j], empty_rows=tr, empty_columns=tc, factor=10) for i in test_galax_pt2.keys() for j in range(i)]
assert sum(test_1) == 1030

test_2 = [calculate_distance(tg[i], tg[j], empty_rows=tr, empty_columns=tc, factor=100) for i in test_galax_pt2.keys() for j in range(i)]
assert sum(test_2) == 8410

galax = get_galaxies(data)
tc = get_empty_columns(data)
tr = get_empty_rows(data)
part_2 =  [calculate_distance(galax[i], galax[j], empty_rows=tr, empty_columns=tc, factor=1_000_000) for i in galax.keys() for j in range(i)]
print(f"Part 2 result: {sum(part_2)}")