from collections import Counter

def count(inp):
    total = Counter(inp)
    up = total['(']
    down = total[')']
    return up - down

def negative_floor(inp):
    floor_count = 0

    for idx, char in enumerate(inp):
        if char == '(':
            floor_count += 1
        elif char == ')':
            floor_count -= 1
        if floor_count < 0:
            return idx + 1

def test_input():
    with open('tests.txt') as file:
        for line in file:
            inp, target = line.strip('\n').split('=')
            target = int(target)
            print(f"Result is: {count(inp)==target}")


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read().strip()
        print(f"Solution 1: {count(data)}")
        print(f"Solution 2: {negative_floor(data)}")
