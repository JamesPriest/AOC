def run_intcodes(command_list):
    idx = 0

    while True:
        if command_list[idx] == 99:
            return command_list[0]
        elif command_list[idx] == 1:
            # Addition command
            sums = command_list[command_list[idx+1]] + command_list[command_list[idx+2]]
            save_to = command_list[idx+3]
            command_list[save_to] = sums
            idx += 4
        elif command_list[idx] == 2:
            # Addition command
            mult = command_list[command_list[idx+1]] * command_list[command_list[idx+2]]
            save_to = command_list[idx+3]
            command_list[save_to] = mult
            idx += 4


test_program =  [1,9,10,3,2,3,11,0,99,30,40,50]
assert run_intcodes(test_program) == 3500
test_program =  [1,0,0,0,99]
assert run_intcodes(test_program) == 2
test_program =  [2,3,0,3,99]
assert run_intcodes(test_program) == 2
test_program =  [1,1,1,4,99,5,6,0,99]
assert run_intcodes(test_program) == 30

from itertools import product

def main():
    with open('input') as f:
        code_list = list(map(int, f.read().strip().split(',')))

    original_list = code_list.copy()
    # Set to 1202 program alarm
    code_list[1] = 12
    code_list[2] = 2

    print(f"Q1: {run_intcodes(code_list)}")


    for i, j in product(range(100), range(100)):
        code_list = original_list.copy()
        code_list[1] = i
        code_list[2] = j
        result = run_intcodes(code_list)
    
        if result == 19690720:
            print("Combination found")
            break

    print(f"Q2: {100*i + j}")

if __name__ == "__main__":
    main()
