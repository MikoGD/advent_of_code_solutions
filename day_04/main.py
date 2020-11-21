def main():
    with open('day_04/data.txt', 'r', encoding='utf-8') as file:
        ranges = [line.strip().split('-') for line in file]
        begin, end = ranges[0]
    # END WITH

    count = 0
    for i in range(int(begin), int(end) + 1):
        adjacent = False
        ascending = False
        curr_num = [int(c) for c in str(i)]

        for j, digit in enumerate(curr_num):
            if j < len(curr_num) - 1 and digit ^ curr_num[j + 1] == 0:
                if j < len(curr_num) - 2 and digit ^ curr_num[j + 2] != 0:
                    adjacent = True
                # END IF
                break
            # END IF
        # END FOR

        if curr_num == sorted(curr_num):
            ascending = True
        # END IF

        if adjacent == True and ascending == True:
            print(i)
            count += 1
        # END IF
    # END FOR

    print(count)
# END main()


if __name__ == "__main__":
    main()
# END IF
