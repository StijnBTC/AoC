def day2_1():
    hpos = 0
    depth = 0
    for line in read_file():
        line = line.split()
        number = int(line[1])
        if line[0] == 'forward':
            hpos += number
        if line[0] == 'down':
            depth += number
        if line[0] == 'up':
            depth -= number
    print(hpos * depth)


def day2_2():
    hpos = 0
    depth = 0
    aim = 0
    for line in read_file():
        line = line.split()
        number = int(line[1])
        if line[0] == 'forward':
            hpos += number
            depth += aim * number
        if line[0] == 'down':
            aim += number
        if line[0] == 'up':
            aim -= number
    print(hpos * depth)


def read_file():
    return open('input.txt', 'r').readlines()


if __name__ == "__main__":
    day2_1()
    day2_2()
