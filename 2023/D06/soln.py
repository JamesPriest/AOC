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
    winning_prods = reduce(lambda x, y: x*y, \
        [sum([1 for i in range(t) if -i**2 + i*t - d>0]) for t, d in zip(times, distances)]
    )

    return winning_prods


assert calculate_winnings(*parse_data(test_case)) == 288


with open("input.txt", "r") as f:
    data = f.read()

# Part 1
print(calculate_winnings(*parse_data(data)))


# Part 2
print(calculate_winnings(*parse_data_pt_2(data)))