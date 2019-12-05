
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_move(self, direction):
        if direction == "U":
            self.move_up()
        elif direction == "D":
            self.move_down()
        elif direction == "R":
            self.move_right()
        elif direction == "L":
            self.move_left()
        else:
            print('???')

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

def calculate_paths(wires):
    possible_paths = []
    for wire in wires:
        wire_path = Point(0,0)
        traversed_points = []
        for move in wire.split(','):
            distance = int(move[1:])
            for i in range(distance):
                wire_path.make_move(move[0])
                traversed_points.append((wire_path.x, wire_path.y))
        possible_paths.append(traversed_points)

    return possible_paths


def calculate_shortest_wire_crossover(wires): 
    possible_paths = calculate_paths(wires)
    wire1, wire2 = possible_paths
    wire1 = set(wire1)
    wire2 = set(wire2)
    #print(possible_paths[1] & possible_paths[0])
    #print([sum(i) for i in possible_paths[1] & possible_paths[0]])
    shortest_path = min([sum(map(abs, i)) for i in wire1 & wire2])

    return shortest_path


test_1 = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
test_2 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
test_3 = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

assert calculate_shortest_wire_crossover(test_1) == 6
print( calculate_shortest_wire_crossover(test_2)) 
assert calculate_shortest_wire_crossover(test_2) == 159
assert calculate_shortest_wire_crossover(test_3) == 135

def main():
    with open('input') as f:
        wires = f.read().strip().split('\n')

    print(f"Part 1 is {calculate_shortest_wire_crossover(wires)}")

    p1, p2 = calculate_paths(wires)
    intersections = list(set(p1) & set(p2))
    least_energy = min([p1.index(i) + p2.index(i) + 2 for i in intersections])

    print(f"Part 2 is {least_energy}")


if __name__ == "__main__":
    main()
