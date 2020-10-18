import math

X = 0
Y = 1


class Grid:
    def __init__(self):
        self.layout = []
        self.center = [0, 0]
        self.x_max = 0
        self.y_max = 0
    # END __init__()

    def check_space(self, path, curr_pos):
        direction, steps = path[0], int(''.join(path[1:]))
        print(f'cur_pos: {curr_pos}, path: {"".join(path)}')
        print(
            f'center: {self.center}, x_max: {self.x_max}, y_max {self.y_max}')

        if direction == 'U':
            diff = curr_pos[Y] - steps
            print(diff)
            if diff < 0:
                diff = abs(diff)
                """
                for i, col in enumerate(self.layout):
                    col = ([0] * diff) + col
                    col += ([0] * diff)
                # END FOR
                """
                for i in range(0, len(self.layout)):
                    self.layout[i] = ([0] * diff) + self.layout[i]
                    self.layout[i] += ([0] * diff)
                # END FOR
                self.y_max += diff * 2
                self.check_grid_odd()
                self.center[Y] = math.ceil(self.y_max / 2)
                curr_pos[Y] += math.ceil(self.y_max / 2)
            # END IF
            curr_pos[Y] = (curr_pos[Y] - steps) + \
                math.ceil(self.y_max / 2)
        elif direction == 'R':
            diff = self.x_max - (curr_pos[X] + steps)
            print(diff)
            if diff < 0:
                diff = abs(diff)
                for i in range(0, abs(diff)):
                    self.layout.append([0] * self.y_max)
                    self.layout.insert(0, [0] * self.y_max)
                # END FOR
                self.x_max += diff * 2
                self.check_grid_odd()
                self.center[X] = math.ceil(self.x_max / 2)
                curr_pos[X] += math.ceil(self.x_max / 2)
            # END IF
        elif direction == 'D':
            diff = self.y_max - (curr_pos[Y] + steps)
            if diff < 0:
                diff = abs(diff)
                for col in self.layout:
                    col = ([0] * diff) + col
                    col += ([0] * diff)
                # END FOR
                self.y_max += diff
                self.check_grid_odd()
                self.center[Y] = math.ceil(self.y_max / 2)
                curr_pos[Y] = (curr_pos[Y] + steps) - diff
            # END IF
        elif direction == 'L':
            diff = curr_pos[X] - steps
            if diff < 0:
                diff = abs(diff)
                for i in range(0, abs(diff)):
                    self.layout.append([0] * self.y_max)
                    self.layout.insert(0, [0] * self.y_max)
                # END FOR
                self.x_max += diff
                self.check_grid_odd()
                self.center[X] = math.ceil(self.x_max / 2)
            # END IF
            curr_pos = (curr_pos[X] - steps) - steps
        else:
            print(f'ERROR: invalid path - {path}')
            print(f'direction {direction} == \'R\'? {direction == "R"}')
            exit()
        # END IF

        print('~~~ after adding path ~~~')
        print(f'cur_pos: {curr_pos}, path: {"".join(path)}')
        print(
            f'center: {self.center}, x_max: {self.x_max}, y_max {self.y_max}')
        print('----------------------------\n')
        return curr_pos
    # END check_space()

    def check_grid_odd(self):
        if self.x_max % 2 == 0:
            self.layout.append([0] * self.y_max)
            self.x_max += 1
        # END IF

        if self.y_max % 2 == 0 and self.y_max != 0:
            for col in self.layout:
                col += [0]
            # END FOR

            self.y_max += 1
        # END IF
    # END chech_grid_odd()
# END CLASS


def main():
    with open('data.txt', 'r', encoding='utf-8') as file:
        wires = [line.strip().split(',') for line in file]
        wire_1, wire_2 = wires
    # END WITH

    grid = Grid()
    draw_wire(wire_1, grid)
    print(grid)
# END main()


def draw_wire(wire, grid):
    curr_pos = list(grid.center)
    for i, path in enumerate(wire):
        print(f'drawing wire {i}')
        if i > 2:
            exit()
        path = list(path)
        if path[0] == 'U':
            cur_pos = grid.check_space(path, curr_pos)
        elif path[0] == 'R':
            cur_pos = grid.check_space(path, curr_pos)
        elif path[0] == 'D':
            cur_pos = grid.check_space(path, curr_pos)
        elif path[0] == 'L':
            cur_pos = grid.check_space(path, curr_pos)
        else:
            print(f'ERROR: invalid direction - {path[0]}')
            exit()
        # END IF

    # END IF
# END draw_wire()


if __name__ == "__main__":
    main()
# END IF
