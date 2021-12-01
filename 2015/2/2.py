def read_file():
    return open('input.txt', 'r').readlines()


def day2():
    paper = 0
    ribbon = 0
    for line in read_file():
        length, width, height = [int(x) for x in line.split('x')]
        paper += calculate_sf(length, width, height)
        ribbon += calculate_ribbon(length, width, height)
    print(paper)
    print(ribbon)


def calculate_sf(length, width, height):
    sides = [2 * length * width, 2 * width * height, 2 * height * length]
    sides.sort()
    return int(sum(sides + [sides[0] / 2]))


def calculate_ribbon(length, width, height):
    sides = [length, width, height]
    sides.sort()
    return int(sides[0]*2 + sides[1]*2)+calculate_bow(length, width, height)


def calculate_bow(length, width, height):
    return int(length * width * height)


if __name__ == "__main__":
    day2()
