
def counter(string):
    k = {}
    for letter in string:
        if letter in k:
            k[letter] += 1
        else:
            k[letter] = 1

    return k

def count_twos_and_threes(string):
    counts = counter(string)
    values = [i for i in counts.values()]
    return (2 in values)*1, (3 in values)*1

def compare_IDs(string1, string2):
    difference_observed = 0
    for i, j in zip(string1, string2):
        if i != j:
            if not difference_observed:
                difference_observed = 1
            else:
                return -1
    return difference_observed

data = open('input.txt').read().strip().split('\n')
twos, threes = list(zip(*[count_twos_and_threes(i) for i in data]))
print(f"Part #1: {sum(twos)*sum(threes)}")

for i in range(len(data)):
    for j in range(i):
        if compare_IDs(data[i], data[j]) == 1:
            final = ""
            for str1, str2 in zip(data[i], data[j]):
                if str1==str2:
                    final+=str1
            break

print(f"Part #2: {final}")
