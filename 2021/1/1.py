def day1(window_size=1):
    lines = read_file()
    count = 0
    prev_sum = None

    for i in range(len(lines) - window_size + 1):
        next_sum = sum(lines[i:i + window_size])
        if prev_sum and next_sum > prev_sum:
            count += 1
        prev_sum = next_sum
    print(f'Answer: {count}')


def read_file():
    return [*map(int, open('input.txt', 'r'))]


if __name__ == "__main__":
    day1()
    day1(3)
