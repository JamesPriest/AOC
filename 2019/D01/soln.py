def calculate_fuel_requirements(value):
    return value//3 - 2

def calculate_fuel_requirements_with_fuel(value):
    fuel_reqs = []
    while value > 6:
        new_value = calculate_fuel_requirements(value)
        fuel_reqs.append(new_value)
        value = new_value
    return sum(fuel_reqs)

def calculate_fuel_req_p2(value):
    output = [value]
    while output[-1] > 6:
        output.append(calculate_fuel_requirements(output[-1]))
    return sum(output[1:])

# Test known examples from Q
assert calculate_fuel_requirements(12) == 2
assert calculate_fuel_requirements(14) == 2
assert calculate_fuel_requirements(1969) == 654
assert calculate_fuel_requirements(100756) == 33583

assert calculate_fuel_requirements_with_fuel(14) == 2
assert calculate_fuel_requirements_with_fuel(1969) == 966
assert calculate_fuel_requirements_with_fuel(100756) == 50346

assert calculate_fuel_req_p2(14) == 2
assert calculate_fuel_req_p2(1969) == 966
assert calculate_fuel_req_p2(100756) == 50346


if __name__ == "__main__":
    
    with open('input1') as f:
        p1 =  list(map(int, f.read().strip().split('\n')))

    print(f"Q1 answer is: {sum(map(calculate_fuel_requirements, p1))}")

    print(f"Q2 answer is: {sum(map(calculate_fuel_requirements_with_fuel, p1))}")
