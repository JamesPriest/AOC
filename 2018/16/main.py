import opcodes as ops


def calculate(before, code, after, show=False):
    count = 0
    for i in filter(lambda x: "__" not in x, dir(ops)):
        if show:
            print(
                f"{i} - " \
                f"{getattr(ops, i)(before, *code)==after} - " \
                f"{getattr(ops, i)(before, *code)}"
            )
        if (getattr(ops, i)(before, *code) == after) == True:
            count += 1

    return count

def convert_to_int_list(inp):
    inp = list(map(int, inp.strip(']').split('[')[1].split(',')))
    return inp

def convert_code_input(inp):
    inp = list(map(int, inp.split(' ')))
    return inp

if __name__ == "__main__":
    data = open("input").read().split('\n')
    before = [convert_to_int_list(i) for i in data[::4][:-1]]
    code = [convert_code_input(i)[1:] for i in data[1::4]]
    after = [convert_to_int_list(i) for i in data[2::4]]

    total_count = 0
    for bef, cod, aft in zip(before, code, after):
        possible_choices = calculate(bef, cod, aft)
        if possible_choices > 2:
            total_count += 1
        elif possible_choices == 1:
            calculate(bef, cod, aft, show=True)
    
    print(f"Problem 1: {total_count}")

