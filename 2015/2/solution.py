def calculate_face_areas(dimensions):
    l, b, w = dimensions
    face_areas = [l * w, w * b, l * b]
    smallest_face = min(face_areas)
    return 2 * sum(face_areas) + smallest_face


def main():
    with open("input.txt") as file:
        data = file.read().split("\n")
    data = [
        list(map(int, i.split("x")))
        for i in data
        if len(i) > 0
    ]

    data = [ calculate_face_areas(i) for i in data]

    print(f"Total is: {sum(data)}")


if __name__ == "__main__":
    main()
