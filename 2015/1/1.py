def read_file():
    return open('input.txt', 'r').read()


def day1():
    floor = 0
    for i, val in enumerate(read_file()):
        if val == '(':
            floor += 1
        elif val == ')':
            floor -= 1
        if floor == -1:
            print(i + 1)
    print(floor)


if __name__ == "__main__":
    day1()
