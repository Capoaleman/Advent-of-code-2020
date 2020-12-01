# December 1st Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman


def doble_mult(series, n):
    # First part of the puzze, look 2 numbers that they sum is equal to 2020 and then multiply them for the result.
    for i, num1 in enumerate(series):
        for j in range(i+1, n-1):
            if num1 + series[j] == 2020:
                return num1*series[j]


def triple_mult(series, n):
    # Second part of the puzzle, look 3 numbers that they sum is equal to 2020 and the multiply them for the result.
    for i, num1 in enumerate(series):
        for j in range(i+1, n-1):
            for h in range(j+1, n-1):
                if num1+series[j]+series[h] == 2020:
                    return num1*series[j]*series[h]
                elif num1+series[j]+series[h] > 2020:
                    break


if __name__ == "__main__":
    f = open("InputDay1_2020.txt", "r")
    input_arr = list(map(int, f.read().split("\n")))
    result1 = doble_mult(input_arr, len(input_arr))
    result2 = triple_mult(sorted(input_arr), len(input_arr))
    print("1st part answer:", result1)
    print("2nd part answer:", result2)
