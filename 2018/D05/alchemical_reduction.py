import time


def react_string(data):
    stack = []
    for letter in data:

        if len(stack) == 0:
            stack.append(letter)
            continue
        if (
            (chr(ord(letter) + 32))
            if ord(letter) <= ord("Z")
            else chr(ord(letter) - 32)
        ) == stack[-1]:
            stack = stack[:-1]
        else:
            stack.append(letter)

    return len(stack)


def react_string2(data, return_raw=False):
    i=0
    while i != len(data) - 1:
        if  ((chr(ord(data[i]) + 32))
            if ord(data[i]) <= ord("Z")
            else chr(ord(data[i]) - 32)) == data[i+1]:
                data = data[:i] + data[i+2:]
                i -= 2
        i+=1

    return len(data) if not return_raw else data


if __name__ == "__main__":
    data = open("input.txt").read().strip()
    
    st = time.time()
    print(f"Part 1: {react_string(data)}")
    print(f"Elapsed time - {time.time() - st:.4f}s")


    st = time.time()
    print(f"Part 1: {react_string2(data)}")
    print(f"Elapsed time - {time.time() - st:.4f}s")

    missing_letters = {}
    letters = set(data.lower())
    
    st = time.time()
    for letter in letters:
        missing_letters[letter] = react_string(
            data.replace(letter, "").replace(letter.upper(), "")
        )
    print("")
    smallest_result = sorted(missing_letters.items(), key=lambda x: x[1])[0]
    print(f"Part 2: {smallest_result[0]} ({smallest_result[1]})")
    print(f"Elapsed time - {time.time() - st:.4f}s")

    st = time.time()
    for letter in letters:
        missing_letters[letter] = react_string2(
            data.replace(letter, "").replace(letter.upper(), "")
        )
    print("")
    smallest_result = sorted(missing_letters.items(), key=lambda x: x[1])[0]
    print(f"Part 2: {smallest_result[0]} ({smallest_result[1]})")
    print(f"Elapsed time - {time.time() - st:.4f}s")

    st = time.time()
    reduced = react_string2(data, return_raw=True)
    for letter in letters:
        missing_letters[letter] = react_string2(
            reduced.replace(letter, "").replace(letter.upper(), "")
        )
    print("")
    smallest_result = sorted(missing_letters.items(), key=lambda x: x[1])[0]
    print(f"Part 2: {smallest_result[0]} ({smallest_result[1]})")
    print(f"Elapsed time - {time.time() - st:.4f}s")
