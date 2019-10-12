def main():
    with open('input.txt') as file:
        data = file.read()

    visited_houses = []
    xpos, ypos = 0, 0

    visited_houses.append((xpos, ypos))

    for direction in data:
        if direction == "^":
            xpos += 1
        elif direction == ">":
            ypos += 1
        elif direction == "<":
            ypos -= 1
        elif direction == "v":
            xpos -= 1
        else:
            pass

        if (xpos, ypos) not in visited_houses:
            visited_houses.append((xpos, ypos))

    print(len(visited_houses))



if __name__ == '__main__':
    main()
