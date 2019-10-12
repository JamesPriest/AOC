def calculate_face_areas(dimensions):
    l, b, w = dimensions
    face_areas = [l * w, w * b, l * b]
    smallest_face = min(face_areas)
    return 2 * sum(face_areas) + smallest_face


from functools import reduce


def calculate_ribbon_distance(dimensions):
    l, b, w = dimensions
    face_areas = [l * w, w * b, l * b]
    face_dims = [(l, w), (w, b), (l, b)]
    smallest_face = face_dims[face_areas.index(min(face_areas))]
    smallest_distance = reduce(lambda x, y: x * y, dimensions)
    return smallest_distance + 2*sum(smallest_face)


def main():
    with open("input.txt") as file:
        data = file.read().split("\n")
    data = [list(map(int, i.split("x"))) for i in data if len(i) > 0]

    face_areas = [calculate_face_areas(i) for i in data]

    print(f"Total is: {sum(face_areas)}")

    ribbon_distance = [calculate_ribbon_distance(i) for i in data]

    print(f"Total is {sum(ribbon_distance)}")

if __name__ == "__main__":
    main()
