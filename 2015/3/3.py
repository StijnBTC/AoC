def read_file():
    return open('input.txt', 'r').readline()


def day3_2():
    sx = 0
    sy = 0
    rx = 0
    ry = 0
    line = read_file()
    santa_route = [(sx, sy)]
    robot_route = [(rx, ry)]
    turn = True
    for direction in line:
        if turn:
            sx, sy = step(sx, sy, direction)
            santa_route.append((sx, sy))
        else:
            rx, ry = step(rx, ry, direction)
            robot_route.append((rx, ry))
        turn = not turn
    print("p2 = " + str(len(set(santa_route).union(set(robot_route)))))


def day3_1():
    x = 0
    y = 0
    line = read_file()
    santa_route = [(x, y)]
    for direction in line:
        x, y = step(x, y, direction)
        santa_route.append((x, y))
    print("p1 = " + str(len(set(santa_route))))


def step(x, y, direction):
    if direction == '<':
        x -= 1
    if direction == '>':
        x += 1
    if direction == 'v':
        y -= 1
    if direction == '^':
        y += 1
    return x, y


if __name__ == "__main__":
    day3_1()
    day3_2()
