from functools import reduce

test_case = """Time:      7  15   30
Distance:  9  40  200"""

def parse_data(data):
    t, d = data.split('\n')
    t = list(map(int, t.replace("Time:", "").strip().split()))
    d = list(map(int, d.replace("Distance:", "").strip().split()))
    return t, d

def parse_data_pt_2(data):
    t, d = data.split('\n')
    t = list(map(int, t.replace("Time:", "").replace(' ', '').strip().split()))
    d = list(map(int, d.replace("Distance:", "").replace(' ', '').strip().split()))
    return t, d


def calculate_winnings(times, distances):
    race_winnings = []
    for time, distance in zip(times, distances):
        races = [1 for i in range(time+1) if i*(time - i) > distance]
        race_winnings.append(sum(races))

    winning_prods = reduce(lambda x, y: x*y, race_winnings)
    return winning_prods


assert calculate_winnings(*parse_data(test_case)) == 288


with open("input.txt", "r") as f:
    data = f.read()

# Part 1
print(calculate_winnings(*parse_data(data)))


# Part 2
print(calculate_winnings(*parse_data_pt_2(data)))