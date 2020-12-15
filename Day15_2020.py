# December 15th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman

INPUT = [2, 0, 1, 7, 4, 14, 18]


def next_num(turn, num):
    tmp = data.get(num, 0)
    data[num] = turn
    if tmp == 0:
        return tmp
    else:
        return turn - tmp


def play(top):
    turn = len(INPUT)
    num = INPUT[-1]
    while turn <= top:  # 30000000th number
        num = next_num(turn, num)
        turn += 1
    for key, val in data.items():
        if val == top:
            return key


if __name__ == "__main__":
    # Part 1
    data = dict([(item, i+1) for i, item in enumerate(INPUT)])
    print("The 2020th number is:", play(2020))
    # Part 2
    data = dict([(item, i+1) for i, item in enumerate(INPUT)])
    print("The 30000000th number is:", play(30000000))
