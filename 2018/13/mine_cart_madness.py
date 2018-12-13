def parse_map():
    # Thing about the representation of the cart in memory.
    pass

class cart:

    def __init__(self):
        self.turn = "left"

    def get_intersection_turn(self):
        last_direction = self.turn
        turn_mapping = {"left":"straight", "straight":"right", "right":"left"}
        self.turn = turn_mapping[last_direction]
        return self.turn
