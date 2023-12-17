from collections import namedtuple

import numpy as np

from functools import wraps
from time import time


def timing(f):
    """Taken from https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator"""

    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print("func:%r args:[%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te - ts))
        return result

    return wrap


class BeamLocation:
    def __init__(self, x, y, max_length, max_height):
        self.x = x
        self.y = y
        self.max_length = max_length
        self.max_height = max_height
        self.terminated = False

        self.initial_x = x
        self.initial_y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_location(self):
        return (self.x, self.y)

    def move_up(self):
        if not self.terminated and self.x > 0:
            self.x -= 1
        else:
            self.terminated = True

    def move_down(self):
        if not self.terminated and self.x < self.max_height - 1:
            self.x += 1
        else:
            self.terminated = True

    def move_left(self):
        if not self.terminated and self.y > 0:
            self.y -= 1
        else:
            self.terminated = True

    def move_right(self):
        if not self.terminated and self.y < self.max_length - 1:
            self.y += 1
        else:
            self.terminated = True

    def duplicate(self):
        return BeamLocation(self.x, self.y, self.max_height, self.max_length)


class EnergisedLocations:
    def __init__(self):
        self.energised_coordinates = []

    def number_energised_locations(self):
        return len(self.energised_coordinates)

    def add_location(self, beam_location):
        location = beam_location.get_location()
        if location not in self.energised_coordinates:
            self.energised_coordinates.append(location)


class FastEnergisedLocations:
    """Re-implemntation of EnergisedLocation by @BradLewis

    Leverages 2 major changes
    1. List appens are horrendously slow relative to numpy arrays
    2. We know the size of the 2D matrix which is immutable, so we can
        tick the same box to the same effect
    """

    def __init__(self, width, height):
        self.energised_coordinates = np.zeros((width, height), dtype="?")

    def number_energised_locations(self):
        return np.sum(self.energised_coordinates)

    def add_location(self, beam_location):
        location = beam_location.get_location()
        self.energised_coordinates[location[0]][location[1]] = 1


class Beam:
    def __init__(self, loc, dirn):
        self.loc = loc  # BeamLocation
        self.dirn = dirn  # > < ^ V

        self.beam_key = (self.loc.initial_x, self.loc.initial_y, self.dirn)

        self.actions = {
            (".", ">"): self.loc.move_right,
            (".", "<"): self.loc.move_left,
            (".", "^"): self.loc.move_up,
            (".", "V"): self.loc.move_down,
            ("-", ">"): self.loc.move_right,
            ("-", "<"): self.loc.move_left,
            ("|", "^"): self.loc.move_up,
            ("|", "V"): self.loc.move_down,
        }

    def get_location(self):
        return self.loc.get_location()

    def propagate(self, symbol):
        if self.loc.terminated:
            return None

        new_beam = None

        if symbol == ".":
            self.actions[(symbol, self.dirn)]()
        elif symbol == "-":
            if self.dirn == ">" or self.dirn == "<":
                self.actions[(symbol, self.dirn)]()
            elif self.dirn == "^" or self.dirn == "V":
                new_beam = Beam(self.loc.duplicate(), "<")
                new_beam.loc.move_left()
                self.dirn = ">"
                self.loc.move_right()
                # print(f"New Beam Propagated to: {new_beam.get_location()} - [DIRN = {new_beam.dirn}]")
                # print(f"Old Beam Propagated to: {self.get_location()} - [DIRN = {self.dirn}]")
        elif symbol == "|":
            if self.dirn == ">" or "<":
                # print(f"Found a | entering from {self.dirn} ({self.get_location()})=> going to create a new beam")
                new_beam = Beam(self.loc.duplicate(), "^")
                new_beam.loc.move_up()
                self.dirn = "V"
                self.loc.move_down()
                # print(f"New Beam Propagated to: {new_beam.get_location()} - [DIRN = {new_beam.dirn}]")
                # print(f"Old Beam Propagated to: {self.get_location()} - [DIRN = {self.dirn}]")
            elif self.dirn == "^":
                self.loc.move_up()
            elif self.dirn == "V":
                self.loc.move_down()
        elif symbol == "\\":
            if self.dirn == ">":
                self.loc.move_down()
                self.dirn = "V"
            elif self.dirn == "<":
                self.loc.move_up()
                self.dirn = "^"
            elif self.dirn == "^":
                self.loc.move_left()
                self.dirn = "<"
            elif self.dirn == "V":
                self.loc.move_right()
                self.dirn = ">"
        elif symbol == "/":
            if self.dirn == ">":
                self.loc.move_up()
                self.dirn = "^"
            elif self.dirn == "<":
                self.loc.move_down()
                self.dirn = "V"
            elif self.dirn == "^":
                self.loc.move_right()
                self.dirn = ">"
            elif self.dirn == "V":
                self.loc.move_left()
                self.dirn = "<"

        if (self.loc.x, self.loc.y, self.dirn) == self.beam_key:
            # Reach a cycle
            # print(f"Reached a cycle - terminating the beam F [beam key = {self.beam_key}] [test case = {(self.loc.x, self.loc.y, self.dirn)}]")
            self.loc.terminated = True

        return new_beam


def parse_input(data):
    data = data.split("\n")
    data = list(map(list, data))
    if len(data[-1]) == 0:
        data = data[:-1]
    return data


def print_matrix(inp, coordinates):
    td2 = parse_input(inp)
    for i in coordinates:
        td2[i[0]][i[1]] = "#"

    print(
        "\n".join("".join([i if i in ("#", ".") else "." for i in row]) for row in td2)
    )


test = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""


def print_beam_activity(beams):
    for idx, i in enumerate(beams):
        print(
            f"Beam: {idx} => {i.get_location()} [DIRN = {i.dirn}] [STATUS = {'Terminated' if i.loc.terminated else 'Active'}]"
        )


def print_beam_activity_summary(beams):
    print(
        f"Active beams: {sum(0 if i.loc.terminated else 1 for i in beams)} - Terminated: {sum(1 if i.loc.terminated else 1 for i in beams)}"
    )


@timing
def energised_locations(starting_points, show_max=False):
    highest_energisation = 0
    for i in starting_points:
        # Initialisation
        x, y, dirn = i
        initial_location = BeamLocation(x, y, len(td), len(td[0]))
        beams = [Beam(initial_location, dirn)]

        # Replacement
        # energised = EnergisedLocations()
        energised = FastEnergisedLocations(len(td[0]), len(td))
        energised.add_location(initial_location)

        existing_beams = {beams[0].beam_key}
        visited = set()

        # Don't need to instatiate this iterator, creating the list
        # due the [i.loc.terminated for i in beams] is really expensive
        while not all(i.loc.terminated for i in beams):
            new_beams = []

            for i in beams:
                # Early short if we've visited this location
                visited.add((i.loc.x, i.loc.y, i.dirn))
                symbol = td[i.loc.x][i.loc.y]
                new_beam = i.propagate(symbol)

                if (
                    new_beam
                    and (new_beam.loc.x, new_beam.loc.y, new_beam.dirn) in visited
                ):
                    # print("Cycle detected")
                    new_beam.loc.terminated = True
                    continue
                if (i.loc.x, i.loc.y, i.dirn) in visited:
                    # print("Cycle detected 2")
                    i.loc.terminated = True
                    # Don't need a history of the old beams
                    beams.remove(i)
                    continue
                if new_beam and not new_beam.beam_key in existing_beams:
                    # print("Should be unique, appending...")
                    new_beams.append(new_beam)
                    energised.add_location(new_beam.loc)

                energised.add_location(i.loc)

            for i in new_beams:
                # print(i.beam_key)
                # print(f"Now adding {len(new_beams)} beams")
                beams.append(i)
                existing_beams.add(i.beam_key)

            #
            # print_matrix(test, energised.energised_coordinates)
            # print()

        highest_energisation = max(
            highest_energisation, energised.number_energised_locations()
        )

        if show_max:
            print(
                f"CURRENT MAX: {highest_energisation} [CURRENT = {energised.number_energised_locations()}]"
            )

    return highest_energisation


if __name__ == "__main__":
    ### PART 2
    with open("input.txt", "r") as f:
        data = f.read()

    td = parse_input(data)
    # td = parse_input(test)

    starting_points = ((0, 0, ">"),)
    highest_energisation = energised_locations(starting_points=starting_points)
    print(f"Pt 1: {highest_energisation}")

    starting_points = (
        [(i, 0, ">") for i in range(len(td))]
        + [(i, len(td) - 1, "<") for i in range(len(td))]
        + [(len(td) - 1, i, "^") for i in range(len(td))]
        + [(0, i, "V") for i in range(len(td))]
    )
    highest_energisation = energised_locations(
        starting_points=starting_points, show_max=False
    )
    print(f"Pt 2: {highest_energisation}")
