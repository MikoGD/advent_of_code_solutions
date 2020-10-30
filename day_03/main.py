from types import GetSetDescriptorType


def main():
    with open('day_03/data.txt', 'r', encoding='utf-8') as file:
        wires = [line.strip().split(',') for line in file]
        wire_1, wire_2 = wires
    # END WITH

    points_1 = get_points(wire_1)
    points_2 = get_points(wire_2)

    set_1 = set([point[:2] for point in points_1])
    set_2 = set([point[:2] for point in points_2])

    intersections = sorted(list(set_1.intersection(set_2)))

    intersections_steps = get_steps_to_intersection(
        points_1, points_2, intersections)

    intersections_steps = sorted(intersections_steps)
    print(intersections_steps)
    print(intersections_steps[1])
# END main()


def get_points(wire):
    points = [(0, 0, 0)]

    last_point = points[0]
    for path in wire:
        direction, steps = path[:1], int(path[1:])

        for i in range(0, steps):
            if direction == "R":
                new_point = (last_point[0] + 1,
                             last_point[1], last_point[2] + 1)
            elif direction == "L":
                new_point = (last_point[0] - 1,
                             last_point[1], last_point[2] + 1)
            elif direction == "U":
                new_point = (
                    last_point[0], last_point[1] + 1, last_point[2] + 1)
            elif direction == "D":
                new_point = (
                    last_point[0], last_point[1] - 1, last_point[2] + 1)
            else:
                print("ERROR: invalid direction: " + direction)
                exit()
            # END IF

            points.append(new_point)
            last_point = new_point
        # END FOR
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


def get_steps_to_intersection(points_1, points_2, intersections):
    steps_1 = []
    steps_2 = []
    for intersection in intersections:
        for point in points_1:
            if point[:2] == intersection:
                steps_1.append(point[2])
            # END IF
        # END FOR

        for point in points_2:
            if point[:2] == intersection:
                steps_2.append(point[2])
            # END IF
        # END FOR
    # END FOR

    print(steps_1)
    print(steps_2)
    intersections_steps = []
    for i in range(0, len(steps_1)):
        intersections_steps.append(steps_1[i] + steps_2[i])
    # END FOR

    return intersections_steps
# END get_steps_to_intersection()


if __name__ == "__main__":
    main()
# END IF
