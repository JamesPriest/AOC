# Part 1
with open("input.txt", "r") as f:
    data = f.read()

def get_first_and_last_digit_list(data):
    outlist = []
    for item in data.split("\n"):
        if len(item) < 1: 
            continue
        ints = [i for i in item if i in "123456789"]
        outlist.append(int(ints[0] + ints[-1]))

    return outlist

print("Part 1")
print(sum(get_first_and_last_digit_list(data)))


# Part 2
digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# Reformat data list mapping all instances of numbers to their digits
pt_2_data = data

# Can't do this, edge case twonethree is 2ne3 not tw13
# for k, v in digit_map.items():
#     pt_2_data = pt_2_data.replace(k, str(v))

# Re-attempt - scanning across the string and replace once one of the keys of digit map is satisfied
first_digit_of_mapper = set(map(lambda x: x[0], digit_map.keys()))

new_str = []
for item in pt_2_data.split('\n'):
    if len(item) < 2:
        continue

    minor_str = []

    idx = 0
    str_list = list(item)
    while idx < len(str_list):
        letter = str_list[idx]
        if letter in "123456789":
            minor_str.append(letter)
            idx += 1
            continue


        if letter in first_digit_of_mapper:
            for lengths in set(map(len, digit_map.keys())):
                if idx + lengths > len(str_list):
                    continue
                word = ''.join(str_list[idx:idx+lengths])

                if word in digit_map.keys():
                    result = str(digit_map[word])

                    # Don't need to replace, so just get the digits and the word digits
                    # for _ in range(lengths):
                    #     str_list.pop(idx)
                    # str_list.insert(idx, result)
                    minor_str.append(result)
        idx += 1
    
    
    
    new_str.append(''.join(minor_str))

print()
print("Part 2")
print(sum(get_first_and_last_digit_list('\n'.join(new_str))))


