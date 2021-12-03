from collections import Counter


def read_file() -> []:
    return [x for x in open('input.txt').read().strip().split('\n')]


def day3_p1():
    gamma = ''
    epsilon = ''
    file = read_file()
    for i in range(len(file[0])):
        common = Counter([x[i] for x in file])
        if common['0'] > common['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    # print(int(gamma, 2) * int(switch(gamma), 2))
    print(int(gamma, 2) * int(epsilon, 2))


def switch(string):
    result = [(int(x) + 1) % 2 for x in string]
    return str(''.join(str(x) for x in result))


def o2():
    lines = read_file()

    result = ''
    for i in range(len(lines[0])):
        common = Counter([x[i] for x in lines])
        if common['0'] > common['1']:
            lines = [x for x in lines if x[i] == '0']
        else:
            lines = [x for x in lines if x[i] == '1']
        result = lines[0]
    return result


def co2():
    lines = read_file()
    result = ''
    for i in range(len(lines[0])):
        common = Counter([x[i] for x in lines])
        if common['0'] > common['1']:
            lines = [x for x in lines if x[i] == '1']
        else:
            lines = [x for x in lines if x[i] == '0']
        if lines:
            result = lines[0]
    return result


def day3_p2():
    print(int(o2(), 2) * int(co2(), 2))


def most(one, zero):
    if one == zero:
        return 1
    elif one > zero:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # print(switch(list("01010")))
    day3_p1()
    day3_p2()
