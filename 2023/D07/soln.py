from collections import Counter
from itertools import product, repeat


def convert_card_to_int(card, twisted = False):
    if card.isdigit():
        card = int(card)
    else:
        if twisted:
            # Joker mode
            card = {'T':10,'Q':12,'K':13,'A':14,'J': 1}[card]
        else:
            card = {'T':10,'J':11,'Q':12,'K':13,'A':14}[card]
    return card


def calculate_hand_strength(vals):
    """
    Step up by multiples of 100 due to the fact that multiples of 10 could create collisions 
    with hands with Tends, Jacks, Queens or Kings
    """
    hand_strength = 0
    if vals[5] == 1:
        # Five of a Kind
        hand_strength = 1000000000000
    elif vals[4] == 1:
        # Four of a kind
        hand_strength = 10000000000
    elif vals[3] == 1 and vals[2] == 1:
        # Full house
        hand_strength = 100000000
    elif vals[3] == 1 and vals[1] == 2:
        # 3 of a kind
        hand_strength = 1000000
    elif vals[2] == 2:
        # Two Pair
        hand_strength = 10000
    elif vals[2] == 1:
        # One Pair
        hand_strength = 100
    else:
        # High card
        hand_strength = 1

    return hand_strength


def replace_jokers(hand_str, replacement_str):
    """
    So basically it's a string substitution however the replacement
    keys aren't uniform and the locations aren't uniform. It creates a
    new string by scanning across the string and replacing what the 
    current index of replacement is.

    It's cursed and if I can be smarter about this, I all ears.
    """
    idx = 0
    out_str = ""
    for i in hand_str:
        if i == "J":
            out_str += replacement_str[idx]
            idx += 1
        else:
            out_str += i
    return out_str


def convert_hand_to_strength_calculator(hand):
    formatted = Counter(Counter(hand).values())
    return formatted


def parse_hand(hand, twisted=False):
    # Get the int values of the cards themselves in the hand
    card_repr = list(map(lambda x: convert_card_to_int(x, twisted=twisted), hand))

    # Hacky but basically we generate EVERY possible hand the joker
    # could be and then subsequently pick the best one
    # Note: 223JJ
    if twisted and hand.count('J') > 0:
        # Here we ONLY care about how strong the hand could ever possibly be
        if hand.count('J') == 5 or hand.count('J') == 4:
            # Short circuit the obvious examples
            hand_strength = calculate_hand_strength(convert_hand_to_strength_calculator('KKKKK'))
        else:
            # I don't think python should be written like this...
            hand_strength = max(
                calculate_hand_strength(convert_hand_to_strength_calculator(replace_jokers(hand, instance)))   \
                for instance in product(*repeat('AKQT98765432', hand.count('J')))
            )
    else:
        # Original method
        hand_strength = calculate_hand_strength(convert_hand_to_strength_calculator(hand))     

    # This effectively gives us a representation that we can sort over
    card_repr = [i*hand_strength for i in card_repr]

    return card_repr


def compare_hands(hand_list):
    # Assign an id to each hand
    hand_id_map = {i:j for i, j in enumerate(hand_list)}
    # Get sort each id by ranking
    sorted_hand_winnings = [i[0] for i in sorted(hand_id_map.items(), key = lambda x: (x[1][0], x[1][1], x[1][2], x[1][3], x[1][4]), reverse=False)]
    # Hand ID : Ranking
    hand_ranks = {j:i+1 for i, j in enumerate(sorted_hand_winnings)}
    # Abuse the fact that this is ordering has been preserved
    total_winnings = [i * hand_ranks[j] for i, j in zip(wagers, sorted(hand_ranks.keys()))]
    return total_winnings


def parse_input(input_str, twisted=False):
    pre_map = list(map(lambda x: x.split(' '), input_str.split('\n')))
    wagers = [int(i[1]) for i in pre_map]
    hand_list = [parse_hand(i[0], twisted=twisted) for i in pre_map]
    return wagers, hand_list


# Tests
assert convert_card_to_int('A') == 14
assert convert_card_to_int('2') == 2
assert convert_card_to_int('3') == 3
assert convert_card_to_int('J') == 11


# Test case
test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# Hand to an int based repr
wagers, hand_list = parse_input(test)
hand_val = compare_hands(hand_list)
total_winnings = sum(hand_val)

assert total_winnings == 6440

# Part 1
with open("input.txt", "r") as f:
    data = f.read()

# Hand to an int based repr
wagers, hand_list = parse_input(data)
hand_val = compare_hands(hand_list)
total_winnings = sum(hand_val)

print(f"Part 1: {total_winnings}")

# Test case for Part 2
# Hand to an int based repr
twisted = True
wagers, hand_list = parse_input(test, twisted=twisted)
hand_val = compare_hands(hand_list)
total_winnings = sum(hand_val)
assert total_winnings == 5905

# Part 2
# Another joker reference, ha get it, I'm so funny
wagers, hand_list = parse_input(data, twisted=twisted)
hand_val = compare_hands(hand_list)
total_winnings = sum(hand_val)
assert total_winnings == 250577259
print(f"Part 2: {total_winnings}")