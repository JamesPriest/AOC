import numpy as np 



class Grid:

    def __init__(self, width, height):
        self.grid = np.zeros((width, height), dtype=np.int8)


    def fill_in(self):
        for row in range(len(self.grid)):

            started = 0
            seen_a_gap = 0
            
            # if row % 100 == 0:
            #     print(f"Working on row: {row}")


            # print(f"[started {started}] [seen_a_gap {seen_a_gap}] [row {row}] -- Working on row {row} ")
            for col in range(len(self.grid[0])):
                val = self.grid[row, col]
                # if row == 0:
                    # print(self.grid[row, col+1:])
                if val == 1 and not started and self.grid[row, col+1:].sum() > 0: 
                    # if row == 0:
                        # print(f"[val {val}] [started {started}] [seen_a_gap {seen_a_gap}] [row {row}] [col {col}] -- Starting the process should be 1")
                    started = 1
                elif val == 1 and started and seen_a_gap:
                    # if row == 0:
                        # print(f"[val {val}] [started {started}] [seen_a_gap {seen_a_gap}] [row {row}] [col {col}] -- Ending the process should be 1")
                    started = 0
                    seen_a_gap = 0
                elif val == 1 and started and not seen_a_gap and self.grid[row, col+1:].sum() == 0:
                    # if row == 0:
                        # print(f"[val {val}] [started {started}] [seen_a_gap {seen_a_gap}] [row {row}] [col {col}] -- Alternative end on column: ({row}, {col})")  
                    started = 0
                    seen_a_gap = 0
                elif val == 0 and started:
                    # if row == 0:
                        # print(f"[val {val}] [started {started}] [seen_a_gap {seen_a_gap}] [row {row}] [col {col}] -- Allocating 1 to ({row}, {col})")
                    self.grid[row, col] = 1
                    seen_a_gap = 1                   
                else:
                    # if row == 0:
                        # print(f"[val {val}] [started {started}] [seen_a_gap {seen_a_gap}] [row {row}] [col {col}] -- Didn't find anything, going to next col")
                    continue


    def num_dug_out(self):
        return self.grid.sum()


class Digger:

    def __init__(self, width, height):

        self.grid = Grid(width, height)
        self.x = 0
        self.y = 0

        self.grid.grid[self.x, self.y] = 1


    def make_move(self, dirn, steps):
        if dirn == 'R':
            x_step = 0
            y_step = 1
        elif dirn == 'L':
            x_step = 0
            y_step = -1
        elif dirn == 'U':
            x_step = -1
            y_step = 0
        elif dirn == 'D':
            x_step = 1 
            y_step = 0

        for _ in range(steps):
            self.x += x_step
            self.y += y_step
            self.grid.grid[self.x, self.y] = 1


def parse_instruction(instruction_string):
    """Input ike #abcdef to (length, direction)
    
    First 5 digits are hex encoded, last is direction encoded
    """
    instruction_string = instruction_string.replace('#', '')
    dirn_map = {
        '0':'R',
        '1': 'D',
        '2': 'L',
        '3': 'U'
    }
    direction = dirn_map[instruction_string[-1]]

    length = int(instruction_string[:5], 16)   

    return (length, direction)



def parse_corners(instructions):
    corners = []
    for length, direction in instructions:
        if corners:
            x, y = corners[-1]
        else:
            x, y = 0, 0
        if direction == 'R':
            x += 0 * length
            y += 1 * length           
        elif direction == 'L':
            x += 0 * length
            y += -1 * length
        elif direction == 'U':
            x += -1 * length
            y += 0 * length
        elif direction == 'D':
            x += 1 * length 
            y += 0 * length
        corners.append((x, y))
    return corners


def shoelace(corner_list):
    summation = 0
    for i in range(len(corner_list)):
        if i == len(corner_list)-1:
            x1, y1 = corner_list[i]
            x2, y2 = corner_list[0]    
        else: 
            x1, y1 = corner_list[i]
            x2, y2 = corner_list[i+1]
        summation += x1 * y2 - y1 * x2
    summation = abs(summation) / 2
    return summation


def picks(corner_list):
    shoelace_i = shoelace(corner_list=corner_list)
    segment_length = 0
    for i in range(len(corner_list)):
        segment_length += abs(corner_list[i][0] - corner_list[0 if i == len(corner_list)-1 else i+1][0]) + abs(corner_list[i][1] - corner_list[0 if i == len(corner_list)-1 else i+1][1])
    b = segment_length/2
    # print(f"Segment length: {segment_length}")
    return shoelace_i + b + 1



def parse_input(data):
    data = data.split("\n")
    if len(data[-1]) == 0:
        data = data[:-1]
    data = [i.split(' ') for i in data]
    return data


def format_grid(grid):
    grid_fmt = '\n'.join([''.join(i) for i in grid.astype(int).astype(str)])
    return grid_fmt


if __name__ == '__main__':
    test = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

    td = parse_input(test)

    dig = Digger(10, 8)
    
    for i in td:
        dirn = i[0]
        steps = int(i[1])

        # print(f"Movement: {dirn} + {steps}")

        dig.make_move(dirn, steps)

    dig.grid.fill_in()
    
    print()
    print(format_grid(dig.grid.grid))
    print(dig.grid.num_dug_out())

    with open("input.txt", "r") as f:
        data = f.read()

    data = parse_input(data)
    
    dig = Digger(400, 1500)
    
    for i in data:
        dirn = i[0]
        steps = int(i[1])

        print(f"Movement: {dirn} + {steps}")

        dig.make_move(dirn, steps)

    # Okay here to solve:
    tmp_grid = dig.grid.grid
    # 1. Pivot vertical on an empty column
    empty_cols = np.where(tmp_grid.sum(axis=0)==0)
    pivot = empty_cols[0][-1]+1
    tmp_grid = np.concatenate((tmp_grid[:, pivot:], tmp_grid[:, :pivot]), axis=1)
    # new_grid = np.concatenate()
    # 2. Pivot horizontal on an empty row
    empty_rows = np.where(tmp_grid.sum(axis=1)==0)
    pivot = empty_rows[0][-1]+1
    tmp_grid = np.concatenate((tmp_grid[pivot:, :], tmp_grid[:pivot, :]), axis=0)

    # Reduce - leave some empty room for the next step in the cursed flood fill
    empty_cols = np.where(tmp_grid.sum(axis=0)==0)
    pivot = empty_cols[0][0]
    tmp_grid = tmp_grid[:, :pivot+2]
    empty_rows = np.where(tmp_grid.sum(axis=1)==0)
    pivot = empty_rows[0][0]
    tmp_grid = tmp_grid[:pivot+2, :]

    # Add back an empty row/column to make the flood fill work
    tmp_grid = np.concatenate((np.zeros((tmp_grid.shape[0], 1), dtype=int,), tmp_grid), axis=1) 
    tmp_grid = np.concatenate((np.zeros((1, tmp_grid.shape[1]), dtype=int,), tmp_grid), axis=0) 

    with open("test_grid.txt", "w") as f:
        f.write(format_grid(tmp_grid))

    # Now the interior/exterior are completely within the borders
        # 3. Pick a point and flood fill - as long as it's not already a 1 it's either the interior
        # or the exterior, if it's the exterior then interior points = total_points_on_grid - exterior + boundary
    boundary_size = tmp_grid.sum()
    n_points = tmp_grid.shape[0] * tmp_grid.shape[1]

    x = np.random.randint(0, tmp_grid.shape[0]-1) 
    y = np.random.randint(0, tmp_grid.shape[1]-1) 

    while tmp_grid[x, y] != 0:
        x = np.random.randint(0, tmp_grid.shape[0]-1) 
        y = np.random.randint(0, tmp_grid.shape[1]-1)        
        
    print(f"Initial x, y is {x, y}")
    ng3 = tmp_grid.copy()
    visited = {(x, y)}
    while visited:
        x, y = visited.pop()
        if ng3[x, y] == 1:
            continue
        else:
            ng3[x, y] = 1
            if x > 0:
                visited.add((x-1, y))
            if x < ng3.shape[0]-1:
                visited.add((x+1, y))
            if y > 0:
                visited.add((x, y-1))
            if y < ng3.shape[1]-1:
                visited.add((x, y+1))

    print(f"Total size (if interior point was hit): {ng3.sum()}")
    print(f"Total size (if exterior point was hit): {n_points - ng3.sum() + boundary_size}")

    # Now this works as long as my initial grid size is large enough to not overlap
    # This is cursed.

    # Part 2 - oh no my brilliant plan foiled by a number larger than 10,000
    instructs = [parse_instruction(i[-1].replace('(', '').replace(')', '')) for i in data]
    corners = parse_corners(instructs)
    print(f"Part 2: {picks(corners)}")



    # Example taken from wikipedia
    c = [(1,6), (3,1), (7, 2), (4, 4), (8, 5)]
    assert shoelace(c) == 16.5

    pt1 = [(int(i[1]), i[0]) for i in td]
    c = parse_corners(pt1)
