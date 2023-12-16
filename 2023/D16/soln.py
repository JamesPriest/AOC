from enum import Enum
from collections import namedtuple


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
        return f'({self.x}, {self.y})'

    def is_terminated(self):
        return self.terminated

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


class Beam:
    
    def __init__(self, loc, dirn):

        self.loc = loc # BeamLocation
        self.dirn = dirn # > < ^ V

        self.beam_key = (self.loc.initial_x, self.loc.initial_y, self.dirn)

    def get_location(self):
        return self.loc.get_location()

    def propagate(self, symbol):
        if self.loc.is_terminated():
            return None
        
        new_beam = None
        if symbol == '-':
            if self.dirn == '>':
                self.loc.move_right()
            elif self.dirn == '<':
                self.loc.move_left()
            elif self.dirn == '^' or self.dirn == 'V':
                new_beam = Beam(self.loc.duplicate(), '<')
                new_beam.loc.move_left()
                self.dirn = '>'
                self.loc.move_right()
                # print(f"New Beam Propagated to: {new_beam.get_location()} - [DIRN = {new_beam.dirn}]")
                # print(f"Old Beam Propagated to: {self.get_location()} - [DIRN = {self.dirn}]")                
        elif symbol == '|':
            if self.dirn == '>' or '<':
                # print(f"Found a | entering from {self.dirn} ({self.get_location()})=> going to create a new beam")
                new_beam = Beam(self.loc.duplicate(), '^')
                new_beam.loc.move_up()
                self.dirn = 'V'
                self.loc.move_down()
                # print(f"New Beam Propagated to: {new_beam.get_location()} - [DIRN = {new_beam.dirn}]")
                # print(f"Old Beam Propagated to: {self.get_location()} - [DIRN = {self.dirn}]")
            elif self.dirn == '^':
                self.loc.move_up()            
            elif self.dirn == 'V':
                self.loc.move_down()
        elif symbol == '\\':
            if self.dirn == '>':
                self.loc.move_down()
                self.dirn = 'V'
            elif self.dirn == '<':
                self.loc.move_up()
                self.dirn = '^'
            elif self.dirn == '^':
                self.loc.move_left()
                self.dirn = '<'         
            elif self.dirn == 'V':
                self.loc.move_right()
                self.dirn = '>'  
        elif symbol == '/':
            if self.dirn == '>':
                self.loc.move_up()
                self.dirn = '^'
            elif self.dirn == '<':
                self.loc.move_down()
                self.dirn = 'V'
            elif self.dirn == '^':
                self.loc.move_right()
                self.dirn = '>'         
            elif self.dirn == 'V':
                self.loc.move_left()
                self.dirn = '<'          
        elif symbol == '.':
            if self.dirn == '>':
                self.loc.move_right()
            elif self.dirn == '<':
                self.loc.move_left()
            elif self.dirn == '^':
                self.loc.move_up()            
            elif self.dirn == 'V':
                self.loc.move_down()

        if (self.loc.x, self.loc.y, self.dirn) == self.beam_key:
            # Reach a cycle
            # print(f"Reached a cycle - terminating the beam F [beam key = {self.beam_key}] [test case = {(self.loc.x, self.loc.y, self.dirn)}]")
            self.loc.terminated = True

        return new_beam


def parse_input(data):
    data = data.split('\n')
    data = list(map(list, data))
    if len(data[-1]) == 0:
        data = data[:-1]
    return data

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

def print_matrix(inp, coordinates):
    td2 = parse_input(inp)
    for i in coordinates:
        td2[i[0]][i[1]] = '#'
    
    print('\n'.join(''.join([i if i in ('#', '.') else '.' for i in row]) for row in td2))


def test_fns(beam_list):
    existing_beams = {beam_list[0].beam_key}
    for _ in range(30):
        new_beams = []

        for i in beam_list:
            symbol = td[i.loc.x][i.loc.y]
            new_beam = i.propagate(symbol)
            if new_beam:
                print("Received a new beam")
                print(existing_beams)
                print(new_beam.beam_key)
            if new_beam and not new_beam.beam_key in existing_beams:
                print("Should be unique, appending...")
                new_beams.append(new_beam)
                energised.add_location(new_beam.loc)
            energised.add_location(i.loc)
        
        for i in new_beams:
            print(i.beam_key)
            print(f"Now adding {len(new_beams)} beams")
            beam_list.append(i)
            existing_beams.add(i.beam_key)

        for idx, i in enumerate(beam_list):
            print(f"Beam: {idx} => {i.get_location()} [DIRN = {i.dirn}] [STATUS = {'Terminated' if i.loc.is_terminated() else 'Active'}]")
        print()
        print_matrix(test, energised.energised_coordinates)
        print()


if __name__ == '__main__':
    ### TEST
    # td = parse_input(test)
    # initial_location = BeamLocation(0, 0, len(td), len(td[0]))
    # beams = [Beam(initial_location, '>')]
    # energised = EnergisedLocations()
    # energised.add_location(initial_location)

    # existing_beams = {beams[0].beam_key}
    # while not all([i.loc.is_terminated() for i in beams]):
    #     new_beams = []

    #     for i in beams:
    #         symbol = td[i.loc.x][i.loc.y]
    #         new_beam = i.propagate(symbol)
    #         if new_beam:
    #             print("Received a new beam")
    #             print(existing_beams)
    #             print(new_beam.beam_key)
    #         if new_beam and not new_beam.beam_key in existing_beams:
    #             print("Should be unique, appending...")
    #             new_beams.append(new_beam)
    #             energised.add_location(new_beam.loc)
    #         energised.add_location(i.loc)
        
    #     for i in new_beams:
    #         print(i.beam_key)
    #         print(f"Now adding {len(new_beams)} beams")
    #         beams.append(i)
    #         existing_beams.add(i.beam_key)

    #     for idx, i in enumerate(beams):
    #         print(f"Beam: {idx} => {i.get_location()} [DIRN = {i.dirn}] [STATUS = {'Terminated' if i.loc.is_terminated() else 'Active'}]")
    #     print()
    #     print_matrix(test, energised.energised_coordinates)
    #     print()
    # with open("input.txt", "r") as f:
    #     data = f.read()


    #### PART 1
    # td = parse_input(data)
    # initial_location = BeamLocation(0, 0, len(td), len(td[0]))
    # beams = [Beam(initial_location, '>')]
    # energised = EnergisedLocations()
    # energised.add_location(initial_location)

    # existing_beams = {beams[0].beam_key}
    # while not all([i.loc.is_terminated() for i in beams]):
    #     new_beams = []

    #     for i in beams:
    #         symbol = td[i.loc.x][i.loc.y]
    #         new_beam = i.propagate(symbol)
    #         # if new_beam:
    #         #     print("Received a new beam")
    #         #     print(existing_beams)
    #         #     print(new_beam.beam_key)
    #         if new_beam and not new_beam.beam_key in existing_beams:
    #             # print("Should be unique, appending...")
    #             new_beams.append(new_beam)
    #             energised.add_location(new_beam.loc)
    #         energised.add_location(i.loc)
        
    #     for i in new_beams:
    #         # print(i.beam_key)
    #         # print(f"Now adding {len(new_beams)} beams")
    #         beams.append(i)
    #         existing_beams.add(i.beam_key)

    #     # for idx, i in enumerate(beams):
    #     #     print(f"Beam: {idx} => {i.get_location()} [DIRN = {i.dirn}] [STATUS = {'Terminated' if i.loc.is_terminated() else 'Active'}]")

    #     print(f"Active beams: {sum(0 if i.loc.is_terminated() else 1 for i in beams)} - Terminated: {sum(1 if i.loc.is_terminated() else 1 for i in beams)}")
        # print(f"Active beams: {sum(0 if i.loc.is_terminated() else 1 for i in beams)} - Terminated: {sum(1 if i.loc.is_terminated() else 1 for i in beams)} [CNT = {cnt}] [Stability = {cnt > len(td[0])*1.1}]")   
        # # print_matrix(data, energised.energised_coordinates)
        # if sum(0 if i.loc.is_terminated() else 1 for i in beams) == prev_active_beams and cnt > len(td[0])*1.1:
        #     # Stability
        #     print("Stable")
        #     break
        # elif sum(0 if i.loc.is_terminated() else 1 for i in beams) == prev_active_beams:
        #     cnt += 1
        # else:
        #     cnt = 0

    #     # print_matrix(data, energised.energised_coordinates)


    # print(f"Pt 1: {energised.number_energised_locations()}")

    ### PART 2
    with open("input.txt", "r") as f:
        data = f.read()

    td = parse_input(data)
    # td = parse_input(test)

    highest_energisation = 0
    starting_points = [(i, 0, '>') for i in range(len(td))] \
        + [(i, len(td)-1, '<') for i in range(len(td))] \
            + [(len(td)-1, i, '^') for i in range(len(td))] \
                +  [(0, i, 'V') for i in range(len(td))]
    # starting_points = [(0,0), (0, len(td)-1), (len(td)-1, 0), (len(td)-1, len(td)-1)]
    # starting_points = [ (0, 0, '>'), (3, 0, 'V')]
    for i in starting_points:
        print(f"Working on {i}")
        x, y, dirn = i
        initial_location = BeamLocation(x, y, len(td), len(td[0]))
        beams = [Beam(initial_location, dirn)]
        energised = EnergisedLocations()
        energised.add_location(initial_location)

        existing_beams = {beams[0].beam_key}

        cnt = 0
        prev_active_beams = 0

        while not all([i.loc.is_terminated() for i in beams]):
            new_beams = []

            for i in beams:
                symbol = td[i.loc.x][i.loc.y]
                new_beam = i.propagate(symbol)
                # if new_beam:
                #     print("Received a new beam")
                #     print(existing_beams)
                #     print(new_beam.beam_key)
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

            # for idx, i in enumerate(beams):
            #     print(f"Beam: {idx} => {i.get_location()} [DIRN = {i.dirn}] [STATUS = {'Terminated' if i.loc.is_terminated() else 'Active'}]")

            # print(f"Active beams: {sum(0 if i.loc.is_terminated() else 1 for i in beams)} - Terminated: {sum(1 if i.loc.is_terminated() else 1 for i in beams)} [CNT = {cnt}] [Stability = {cnt > len(td[0])*1.1}]")   
            # print_matrix(test, energised.energised_coordinates)
            # print()
            if sum(0 if i.loc.is_terminated() else 1 for i in beams) == prev_active_beams and cnt > len(td[0])*1.1:
                # Stability
                # print("Stable")
                break
            elif sum(0 if i.loc.is_terminated() else 1 for i in beams) == prev_active_beams:
                cnt += 1
            else:
                cnt = 0


            prev_active_beams = sum(0 if i.loc.is_terminated() else 1 for i in beams) 
    
        highest_energisation = max(highest_energisation, energised.number_energised_locations())
        print(f"CURRENT MAX: {highest_energisation} [CURRENT = {energised.number_energised_locations()}]")
    print(f"Pt 2: {highest_energisation}")