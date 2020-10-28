def main():
    with open('day_03/data_medium.txt', 'r', encoding='utf-8') as file:
        wires = [line.strip().split(',') for line in file]
        wire_1, wire_2 = wires
    # END WITH

    points_1 = get_points(wire_1)
    points_2 = get_points(wire_2)

    set_1 = set(points_1)
    set_2 = set(points_2)

    intersections = set_1.intersection(set_2)
    manhattan_distances = get_manhattan_distances(intersections)

    print(manhattan_distances[1])
# END main()


def get_points(wire):
    points = [(0, 0)]

    last_point = points[0]
    for path in wire:
        direction, steps = path[:1], int(path[1:])

        for i in range(0, steps):
            if direction == "R":
                new_point = (last_point[0] + 1, last_point[1])
            elif direction == "L":
                new_point = (last_point[0] - 1, last_point[1])
            elif direction == "U":
                new_point = (last_point[0], last_point[1] + 1)
            elif direction == "D":
                new_point = (last_point[0], last_point[1] - 1)
            else:
                print("ERROR: invalid direction: " + direction)
                exit()
            # END IF

            points.append(new_point)
            last_point = new_point

            print(f"Point {i} added: {new_point}")
        # END FOR

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # END FOR

    return points
# END get_pontis()


def get_manhattan_distances(intersections):
    manhattan_distances = []

    for intersection in intersections:
        manhattan_distances.append(
            abs(0 - intersection[0]) + abs(0 - intersection[1]))
    # END FOR

    return sorted(manhattan_distances)
# END get_manhattan_distances()


if __name__ == "__main__":
    main()
# END IF
