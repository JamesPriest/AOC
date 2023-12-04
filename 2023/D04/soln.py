with open("input.txt", "r") as f:
    data = f.read()

class Game:

    def __init__(self, game_str):
        
        id_str, game_info = game_str.split(":")
        self.game_id = int(id_str.replace("Card", "").strip())

        winning_numbers, picked_numbers = game_info.split('|')

        self.winning_numbers = self.parse_number_string(winning_numbers[1:-1])
        self.picked_numbers = self.parse_number_string(picked_numbers[1:])

        self.count = 1

    def number_winners(self):
        wins = 0
        for i in self.picked_numbers:
            if i in self.winning_numbers:
                wins += 1
        
        return wins

    def calculate_ticket_score(self):
        wins = self.number_winners()

        ticket_score = 2**(wins-1) if wins > 0 else 0 
        return ticket_score

    @staticmethod
    def parse_number_string(number_string):
        retlist = []
        for i, j in zip(number_string[0::3], number_string[1::3]):
            retlist.append(int(i+j))      

        return retlist



assert Game.parse_number_string("47 97 83 82 43  7 61 73 57  2") == [47, 97, 83, 82, 43, 7, 61, 73, 57, 2]

test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# Part 1
test_cases = [Game(i) for i in test.split('\n')]

assert sum([i.calculate_ticket_score() for i in test_cases]) == 13

cards_str = data.split('\n')

cards = [Game(i) for i in cards_str]

print(sum([i.calculate_ticket_score() for i in cards]))


# Part 2 - Total number of scratchcards you end up with

for idx, card in enumerate(test_cases):
    wins = card.number_winners()
    if wins > 0:
        for i in range(idx+1, wins+idx+1):
            test_cases[i].count += card.count

print([i.count for i in test_cases])
assert sum([i.count for i in test_cases]) == 30

# The number of copies of Card N is a function of {Card N-1, Card N-2, etc}
# Hence Card 2 can only be impacted by Card 1, so all we need to know about Card 1 is 
# 1. How many copies of Card 1 exist and 
for idx, card in enumerate(cards):
    wins = card.number_winners()
    if wins > 0:
        for i in range(idx+1, wins+idx+1):
            cards[i].count += card.count



print(sum([i.count for i in cards]))