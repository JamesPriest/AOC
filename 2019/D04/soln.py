
from collections import Counter

def is_valid_codeword(number):
    if len(str(number)) != 6:
        return False

    two_adjacent = 0
    increasing = 1
    past_number = int(str(number)[0])
    for i in str(number)[1:]:
        if past_number == int(i):
            two_adjacent = 1
        elif past_number > int(i):
            increasing = 0
        past_number = int(i)

    return two_adjacent & increasing

def is_valid_codeward_p2(number):
    if len(str(number)) != 6:
        return False

    two_adjacent = 0
    increasing = 1
    past_number = int(str(number)[0])
    for i in str(number)[1:]:
        if past_number == int(i):
            two_adjacent = 1
        elif past_number > int(i):
            increasing = 0
        past_number = int(i)

    has_a_double = 2 in Counter(str(number)).values()

    return two_adjacent & increasing & has_a_double


     

assert is_valid_codeword(111111) == True
assert is_valid_codeword(223450) == False
assert is_valid_codeword(123789) == False


if __name__ == "__main__":
    
    start, end = 240298, 784956

    part1 = sum([is_valid_codeword(i) for i in range(start, end+1)])

    print(f"Part 1: {part1}")

    part2 = sum([is_valid_codeward_p2(i) for i in range(start, end+1)])
    print(f"Part 2: {part2}")
