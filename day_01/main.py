def main():
    with open('data.txt', 'r', encoding='utf-8') as file:
        modules = [int(line) for line in file]
    # END OPEN

    result, fuels = 0, list(map(lambda n: get_fuel(n//3 - 2), modules))

    for fuel in fuels:
        result += fuel

    print(result)
# END main()


def get_fuel(mass):
    return 0 if mass < 0 else mass + get_fuel((mass//3) - 2)
# END get_fuel


if __name__ == "__main__":
    main()
# END IF
