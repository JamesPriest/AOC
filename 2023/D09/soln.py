def calculate_difference_in_list(input_list):
    first_difference = [input_list[idx+1] - input_list[idx] for idx in range(len(input_list)-1)]
    return first_difference


def calculate_difference_in_list_forward(input_list):
    first_difference = [input_list[idx+1] - input_list[idx] for idx in range(len(input_list)-1)]
    return first_difference


def reduce_list(input_list):
    new_list = calculate_difference_in_list(input_list)
    if all(map(lambda x: x==0, input_list)):
        return 0
    new_val =  reduce_list(new_list)
    return new_list[-1] + new_val


def reduce_list_pt2(input_list):
    new_list = calculate_difference_in_list(input_list)
    if all(map(lambda x: x==0, new_list)):
        return 0
    new_val =  reduce_list_pt2(new_list)
    return new_list[0] - new_val



def reduce_list_with_step_count(input_list, step_count):
    """Debug function to manually cross checking failing calls"""
    new_list = calculate_difference_in_list(input_list)
    # Base statement
    if all(map(lambda x: x==0, new_list)):
        return 0, 1
    new_val, sc =  reduce_list_with_step_count(new_list, step_count)
    return (new_list[-1] + new_val, sc+1)


def convert_string_input_to_int_list(_string):
    result = list(map(lambda x: list(map(int, x)), (map(lambda x: x.split(),  _string.split('\n')))))
    return result

test = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

test = convert_string_input_to_int_list(test)
print(f"TEST value:  {[reduce_list(i)+i[-1] for i in test]}")
assert [reduce_list(i)+i[-1] for i in test] == [18, 28, 68]
assert sum([reduce_list(i)+i[-1] for i in test]) == 114

with open("input.txt", "r") as f:
    data = f.read()
    data = convert_string_input_to_int_list(data)

# Part 1
print(sum([reduce_list(i)+i[-1] for i in data]))

# Part 2
print(sum([i[0]-reduce_list_pt2(i) for i in data]))

# Checking one value
# [Soln: -12, i is 143 and a is -155] Use list: [23, 48, 83, 126, 175, 228, 283, 338, 391, 440, 483, 518, 543, 556, 555, 538, 503, 448, 371, 270, 143]
