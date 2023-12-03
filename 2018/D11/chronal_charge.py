serial_number = 8979

def calculate_power_level(row, column, serial_number):
    rack_id = row + 10
    power = column * rack_id
    power += serial_number
    power *= rack_id
    power = power//100 % 10
    power -= 5
    return power

# Check this works on tests
assert calculate_power_level(3, 5, 8) == 4
assert calculate_power_level(122, 79, 57) == -5
assert calculate_power_level(217, 196, 39) == 0
assert calculate_power_level(101, 153, 71) == 4
print("All assertions passed - calculate function is working")

power_matrix = [[calculate_power_level(i+1, j+1, serial_number) for i in range(300)] for j in range(300)]

largest = 0
for i in range(300):
   for j in range(300):
        total = sum(sum(ll[j:j+3]) for ll in power_matrix[i:i+3])
        if total>largest:
            largest = total
            idx_y, idx_x = i+1, j+1

print(f"Part #1 - {idx_x},{idx_y}")


largest = 0
for size in range(15, 30):
    if (size%30)==0:
        print(f"Now passed {size}")
    for i in range(300):
        if i+size > 300:
            continue
        for j in range(300):
            if j+size > 300:
                continue
 
            total = sum(sum(ll[j:j+size]) for ll in power_matrix[i:i+size])
            if total>largest:
                largest = total
                try:
                    print(f"change size to {size} from {idx_size}")
                except:
                    print(f"Now setting size to {size}")
                idx_y, idx_x, idx_size = i+1, j+1, size

print(f"Part #1 - {idx_x},{idx_y},{idx_size}")


