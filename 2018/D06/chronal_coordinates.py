import numpy as np

from string import ascii_letters

data = [
    [int(j) for j in i.split(", ")] for i in open("input.txt").read().split("\n")[:-1]
]

key_points = {}
for key, val in zip(ascii_letters, data):
    key_points[key] = val


def manhatten_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def calculate_nearest_point(point):
    lowest_val, lowest_key = 1_000_000, 0
    mhd_list = []
    for key, val in key_points.items():
        mhd = manhatten_distance(point, val)
        # Handle collisions
        if mhd < lowest_val:
            lowest_val, lowest_key = mhd, key

        mhd_list.append(mhd)

    if mhd_list.count(lowest_val) > 1:
        lowest_key = "."

    return lowest_key


def calculate_total_size_point(point):
    mhd_list = []
    for key, val in key_points.items():
        mhd = manhatten_distance(point, val)
        mhd_list.append(mhd)

    return sum(mhd_list)


largest_x = max(data, key=lambda x: x[0])[0] + 10
largest_y = max(data, key=lambda x: x[1])[1] + 10

grid = [
    [calculate_nearest_point([i, j]) for i in range(largest_y)]
    for j in range(largest_x)
]
to_exclude = (
    [i for i in grid[0]]
    + [i for i in grid[-1]]
    + [i for j in grid for i in j[0]]
    + [i for j in grid for i in j[-1]]
)
to_exclude = set(to_exclude)

grid_flat = [i for j in grid for i in j]
counts = {}
for i in set(grid_flat):
    if not i in to_exclude:
        counts[i] = grid_flat.count(i)

print(f"Part 1#) {counts[max(counts, key=counts.get)]}")


# see the grid
import matplotlib.pyplot as plt

repr_map = dict(zip(set(grid_flat), range(len(set(grid_flat)))))
num = np.vectorize(repr_map.get)(grid)
# plt.imshow(num)
# plt.show(num)

## Part 2
grid = [
    [calculate_total_size_point([i, j]) for i in range(largest_y)]
    for j in range(largest_x)
]

region_size = sum(1 if j < 10000 else 0 for i in grid for j in i)
print(f"region size is {region_size}")
