def day2_1():
    hpos = 0
    depth = 0
    for line in read_file():
        trimmed_line = line.rstrip()
        number = int(line[len(trimmed_line) - 1])
        if trimmed_line[0] == 'f':
            hpos += number
        if trimmed_line[0] == 'd':
            depth += number
        if trimmed_line[0] == 'u':
            depth -= number
    print(hpos * depth)


def day2_2():
    hpos = 0
    depth = 0
    aim = 0
    for line in read_file():
        trimmed_line = line.rstrip()
        number = int(line[len(trimmed_line) - 1])
        if trimmed_line[0] == 'f':
            hpos += number
            depth += aim * number
        if trimmed_line[0] == 'd':
            aim += number
        if trimmed_line[0] == 'u':
            aim -= number
    print(hpos * depth)


def read_file():
    return open('input.txt', 'r').readlines()


if __name__ == "__main__":
    # day2_1()
    day2_2()
