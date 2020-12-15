# December 15th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman

INPUT = [2, 0, 1, 7, 4, 14, 18]


def next_num(data, turn, num):
    tmp = data.get(num, 0)
    data[num] = turn
    if tmp == 0:
        return tmp
    else:
        return turn - tmp


if __name__ == "__main__":
    data = {}
    for i, item in enumerate(INPUT):
        data[item] = i+1
    turn = i+1
    num = INPUT[-1]
    while turn <= 30000000:  # Part 1 2020tn number, Part 2 30000000th number
        num = next_num(data, turn, num)
        turn += 1
    for key, val in data.items():
        if val == 30000000:
            print("result", key)
