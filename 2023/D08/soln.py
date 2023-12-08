import math

def parse_input(data):
    data = data.split('\n')

    if data[-1] == "":
        data = data[:-1]

    instruction_set = data[0]

    mappings = data[2:]

    return instruction_set, mappings


class Node:
    
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.end = name[-1]

    def add_left_node(self, left):
        self.left = left

    def add_right_node(self, right):
        self.right = right


def parse_mappings(mappings):
    nodes = [Node(i.split(' = ')[0]) for i in mappings]
    node_lookup = {i.name: i for i in nodes}

    for line in mappings:
        name, next_options = line.split(' = ')
        left, right = next_options.replace('(', '').replace(')','').split(', ')
        _node = node_lookup[name]
        _node.add_left_node(node_lookup[left])
        _node.add_right_node(node_lookup[right])

    return nodes


def get_steps(nodes, instructions):
    current_pointer = [i for i in nodes if i.name == 'AAA'].pop()

    instruction_idx = 0
    steps = 0
    while current_pointer.name != 'ZZZ':
        if instructions[instruction_idx] == 'L':
            current_pointer = current_pointer.left
        elif instructions[instruction_idx] == 'R':
            current_pointer = current_pointer.right
        else:
            print("Failuire")
        steps += 1
        instruction_idx = (instruction_idx + 1) % len(instructions)

    return steps


def get_steps_pt2(nodes, instructions):
    node_ptr = [i for i in nodes if i.end == 'A']

    instruction_idx = 0
    steps = 0
    while not all([i.end == 'Z' for i in node_ptr]):
        if instructions[instruction_idx] == 'L':
            node_ptr = [i.left for i in node_ptr]
        elif instructions[instruction_idx] == 'R':
            node_ptr = [i.right for i in node_ptr]
        else:
            print("Failuire")
        steps += 1
        instruction_idx = (instruction_idx + 1) % len(instructions)
    return steps


def calculate_ghost_cycle(ghost, instructions):
    times_hit_Z = 0
    instruction_idx = 0
    ghost_name = ghost.name
    cycle_length = 0
    cycle_begin = 0
    steps = 0
    while times_hit_Z < 2:
        ghost = ghost
        if instructions[instruction_idx] == 'L':
            ghost = ghost.left
        elif instructions[instruction_idx] == 'R':
            ghost = ghost.right
        instruction_idx = (instruction_idx + 1) % len(instructions)
        steps += 1
        if cycle_begin:
            # print(f"Ghost cycle is ongoing counting length of: {cycle_length}")
            cycle_length += 1
        if ghost.end == 'Z':
            # print(f"Ghost cycle has begun: {ghost_name} => at step {steps}")
            cycle_begin = 1
            times_hit_Z += 1
    return cycle_length, ghost_name

test_case = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""


test_case_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

test_case_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

instructions, mappings = parse_input(test_case)
nodes = parse_mappings(mappings)
steps = get_steps(nodes, instructions)
assert steps == 2


instructions, mappings = parse_input(test_case_2)
nodes = parse_mappings(mappings)
steps = get_steps(nodes, instructions)
assert steps == 6


with open("input.txt", "r") as f:
    data = f.read()

instructions, mappings = parse_input(data)
nodes = parse_mappings(mappings)
steps = get_steps(nodes, instructions)
print(steps)



instructions, mappings = parse_input(test_case_3)
nodes = parse_mappings(mappings)
steps = get_steps_pt2(nodes, instructions)
# print(steps)

# Do not do this, it's been over 10 mins and hasn't concluded
instructions, mappings = parse_input(data)
nodes = parse_mappings(mappings)
# steps = get_steps_pt2(nodes, instructions)
# print(steps)



# Approach via cycle length and LCM
instructions, mappings = parse_input(data)
nodes = parse_mappings(mappings)
ghosts = [i for i in nodes if i.end == 'A']
# steps = get_steps_pt2(nodes, instructions)

cycles = [calculate_ghost_cycle(i, instructions) for i in ghosts]
print(math.lcm(*[i[0] for i in cycles]))