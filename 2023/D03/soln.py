with open("input.txt", "r") as f:
    data = f.read()

data = [[j for j in i] for i in data.split('\n')]


def process_data(data):
    i, j = 0, 0

    final_sum = 0

    while i < len(data):
        while j < len(data[0]):
            # print(f"Checking cell: {i} - {j}")
            if data[i][j].isdigit():
                # Found a digit, so grab the digit and then look around it
                emp_digit = data[i][j]
                start_loc = (i, j)
                j += 1
                while data[i][j].isdigit():
                    emp_digit += data[i][j]
                    j += 1
                    if j >= len(data[0]):
                        break
                end_loc = (i, j-1)

                for x in range(i-1, i+2):
                    for y in range(start_loc[1]-1, end_loc[1]+2):
                        # Check if outside boundary
                        if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
                            continue
                        if data[x][y] != '.' and not data[x][y].isdigit():
                            final_sum += int(emp_digit)
                            print(f"Found digit: {int(emp_digit)}")
                            # Only sum once
                            break
                


                
                # Step back an index as we increment in outer case
                j -= 1

                

            j += 1

        j = 0
        i += 1

    return final_sum


test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test = [[j for j in i] for i in test.split('\n')]



assert process_data(test) == 4361


print(process_data(data))