import re 

with open("input.txt", "r") as f:
    data = f.read()


class Game:

    def __init__(self, game_str):

        self.game_id = int(re.match(r'(?:Game ([0-9]+):)', game_str)[1])

        self.pulls = []
        

        for i in game_str.split(':')[1].split(';'):
            single_pull = i.strip().split(' ')

            game_result = {color.replace(',', ''):int(nbr) for nbr, color in zip(single_pull[::2], single_pull[1::2])}

            for i in ['red', 'green', 'blue']:
                if i not in game_result:
                    game_result[i] = 0

            self.pulls.append(game_result)

        #Game 32: 8 green, 17 red, 17 blue; 11 red, 6 green, 13 blue; 14 red, 1 green, 1 blue; 1 green, 17 red, 4 blue; 5 green, 
        #14 red, 15 blue; 15 blue, 8 green


    def __str__(self):
        return f"Game {self.id}: {self.pulls}\n"


    def is_game_valid(self, red_cap, green_cap, blue_cap):
        is_valid = 1
        for i in self.pulls:
            is_valid = is_valid and i['red'] <= red_cap and i['green'] <= green_cap and i['blue'] <= blue_cap

        return is_valid

    def get_minimum_cube_counts(self):
        max_cubes = {'green':0, 'red':0, 'blue':0}
        for i in self.pulls:
            for k, v in i.items():
                max_cubes[k] = max(v, max_cubes[k])
        
        return max_cubes

    
    def calculate_minimum_cube_power(self):
        cubes_required = self.get_minimum_cube_counts()
        cube_power = 1
        for v in cubes_required.values():
            cube_power *= v

        return cube_power


red_cap = 12
green_cap = 13
blue_cap = 14

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

test = test.split('\n')
games = [Game(i) for i in test]
valid_game_ids = [i.game_id for i in games if i.is_game_valid(red_cap=red_cap, blue_cap=blue_cap, green_cap=green_cap)]

assert sum(valid_game_ids) == 8

# Parse Game
game_lines = [line for line in data.split('\n')]


# Part 1
games = [Game(i) for i in game_lines]
valid_game_ids = [i.game_id for i in games if i.is_game_valid(red_cap=red_cap, blue_cap=blue_cap, green_cap=green_cap)]

print(sum(valid_game_ids))

# Part 2
cube_power = [i.calculate_minimum_cube_power() for i in games]
print(sum(cube_power))