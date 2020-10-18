def main():
    with open('data.txt', 'r', encoding='utf-8') as file:
        intcode_string = [line.strip().split(',') for line in file]
        intcode = [int(code) for code in intcode_string[0]]
    # END open()

    for noun in range(0, 100):
        for verb in range(0, 100):
            result = run_program(noun, verb, list(intcode))
            if result == 19690720:
                print(100 * noun + verb)
                exit()
            # END IF
        # END FOR
    # END FOR
# END main()


def run_program(noun, verb, intcode):
    intcode[1] = noun
    intcode[2] = verb

    pointer = 0
    while (intcode[pointer] != 99):
        opcode = intcode[pointer]
        param_1 = intcode[pointer + 1]
        param_2 = intcode[pointer + 2]
        result_address = intcode[pointer + 3]

        if opcode == 1:
            intcode[result_address] = intcode[param_1] + intcode[param_2]
        elif opcode == 2:
            intcode[result_address] = intcode[param_1] * intcode[param_2]
        else:
            print('ERROR: invalid opcode')
            print(f'noun: {noun}, verb: {verb}')
            print(f'pointer: {pointer}, opcode:{opcode}')
            print(intcode)
            exit()
        # END IF

        pointer += 4
    # END WHILE

    return intcode[0]
# END run_program()


if __name__ == "__main__":
    main()
# END IF
