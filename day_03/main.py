import math

X = 0
Y = 1


class Grid:
    def __init__(self):
        self.layout = [[0]]
        self.center = [0, 0]
        self.x_max = 0
        self.y_max = 0
    # END __init__()

    def check_space(self, path, curr_pos):
        direction, steps = path[0], int(''.join(path[1:]))

        if direction in 'UD':
            if direction == 'U':
                diff = curr_pos[Y] - steps
            elif direction == 'D':
                diff = self.y_max - (curr_pos[Y] + steps)
            else:
                print(f'ERROR: direction {direction} is invalid')
                exit()
            # END IF

            if diff < 0:
                diff = abs(diff)

                if self.x_max == 0:
                    self.x_max = 1
                # END IF

                for i in range(0, len(self.layout)):
                    self.layout[i] = ([0] * diff) + self.layout[i]
                    self.layout[i] += ([0] * diff)
                # END FOR
                self.y_max += diff * 2
                self.check_grid_odd()
                self.center[Y] = math.ceil(self.y_max / 2)
                curr_pos[Y] += math.ceil(self.y_max / 2)
            # END IF
        elif direction in 'RL':
            if direction == 'R':
                diff = self.x_max - (curr_pos[X] + steps)
            elif direction == 'L':
                diff = curr_pos[X] - steps
            else:
                print(f'ERROR: direction {direction} is invalid')
                exit()
            # END IF

            if diff < 0:
                diff = abs(diff)

                if self.y_max == 0:
                    self.y_max = 1
                # END IF
                for i in range(0, abs(diff)):
                    self.layout.append([0] * self.y_max)
                    self.layout.insert(0, [0] * self.y_max)
                # END FOR
                self.x_max += diff * 2
                self.check_grid_odd()
                self.center[X] = math.ceil(self.x_max / 2)
                curr_pos[X] += math.ceil(self.x_max / 2)
            # END IF
        else:
            print(f'ERROR: invalid path - {path}')
            print(f'direction {direction} == \'R\'? {direction == "R"}')
            exit()
        # END IF

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

    def add_wire(self, path, curr_pos, wire_no):
        direction, steps = path[0], int(''.join(path[1:]))

        if direction in 'RL':
            if direction == 'R':
                mode = 1
            elif direction == 'L':
                mode = -1
            else:
                print(f'ERROR: invalid direction {direction}')
                exit()
            # END IF

            for i in range(0, steps):
                next_pos = curr_pos[X] + ((1 + i) * mode)
                print(self.x_max, self.center, curr_pos, steps)
                print(f'i = {i}')
                print(next_pos)
                print(self.layout[next_pos])
                print(len(self.layout))
                print('~~~~~~~~~~~~~~~~~')
                if self.layout[next_pos][curr_pos[Y]] == 0:
                    self.layout[next_pos][curr_pos[Y]] = wire_no
                else:
                    self.layout[next_pos][curr_pos[Y]] = 3
                # END IF
            # END FOR
            curr_pos[X] += steps * mode
        # END IF

        if direction in 'UD':
            if direction == 'D':
                mode = 1
            elif direction == 'U':
                mode = -1
            else:
                print(f'ERROR: invalid direction {direction}')
                exit()
            # END IF

            for i in range(0, steps):
                next_pos = curr_pos[Y] + ((1 + i) * mode)
                print(self.y_max, self.center, curr_pos, steps)
                print(f'i = {i}')
                print(f'next_pos = {next_pos}')
                print(len(self.layout[i]))
                print('~~~~~~~~~~~~~~~~~')
                if self.layout[curr_pos[X]][next_pos] == 0:
                    self.layout[curr_pos[X]][next_pos] == wire_no
                else:
                    self.layout[curr_pos[X]][next_pos] = 3
                # END IF
            # END FOR
            curr_pos[Y] += steps * mode
        # END IF

        return curr_pos
    # END add_wire()
# END CLASS


def main():
    with open('data.txt', 'r', encoding='utf-8') as file:
        wires = [line.strip().split(',') for line in file]
        wire_1, wire_2 = wires
    # END WITH

    grid = Grid()
    draw_wire(wire_1, 1, grid)
    print(grid)
# END main()


def draw_wire(wire, wire_no, grid):
    curr_pos = list(grid.center)
    for i, path in enumerate(wire):
        print(f'drawing wire {i}')
        if i > 2:
            print(curr_pos)
            exit()
        path = list(path)
        if path[0] == 'U':
            curr_pos = grid.check_space(path, curr_pos)
            curr_pos = grid.add_wire(path, curr_pos, wire_no)
        elif path[0] == 'R':
            curr_pos = grid.check_space(path, curr_pos)
            curr_pos = grid.add_wire(path, curr_pos, wire_no)
        elif path[0] == 'D':
            curr_pos = grid.check_space(path, curr_pos)
            curr_pos = grid.add_wire(path, curr_pos, wire_no)
        elif path[0] == 'L':
            curr_pos = grid.check_space(path, curr_pos)
            curr_pos = grid.add_wire(path, curr_pos, wire_no)
        else:
            print(f'ERROR: invalid direction - {path[0]}')
            exit()
        # END IF

    # END IF
# END draw_wire()


if __name__ == "__main__":
    main()
# END IF
