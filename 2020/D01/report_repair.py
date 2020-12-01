
def part_one(filename):

    with open(filename) as f:
        data = f.read().split('\n')
        data = list(filter(lambda x: len(x)>0, data))
        data = list(map(int, data))

    for item in data:
        try:
            pair_point = 2020 - item
            data.index(pair_point)
            return item * pair_point
        except:
            continue

    print("failed to find a pair")
    return None

def part_two(filename):
    with open(filename) as f:
        data = f.read().split('\n')
        data = list(filter(lambda x: len(x)>0, data))
        data = list(map(int, data))

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            duo_sum = data[i]+data[j]
            for k in range(j+1, len(data)):
                if duo_sum + data[k] == 2020:
                    return data[i] * data[j] * data[k]


if __name__ == "__main__":
    soln = part_one("input_01")
    print(f"Solution to part one is {soln}")

    soln2 = part_two("input_01")
    print(f"Solution to part one is {soln2}")

