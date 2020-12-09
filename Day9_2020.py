# December 9th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman


def validator(num, preamble):
    # Validates the number as the sum of two numbers in the preamble
    sort_preamble = sorted(preamble)
    for i, h in enumerate(sort_preamble):
        for j in sort_preamble[i:]:
            if num == h+j:
                return True
    return False


def encryption_weakness(num, ind, data):
    # Detects the encryption weakness
    i = 0
    while i < ind:
        add = 0
        num_list = []
        for n in data[i:ind]:
            add += n
            num_list.append(n)
            if add == num:
                return min(num_list) + max(num_list)
            elif add > num:
                i += 1
                break
    return 0


if __name__ == "__main__":
    with open("InputDay9_2020.txt", "r") as file:
        xmas_data = list(map(int, file.read().split("\n")))
    for i, num in enumerate(xmas_data[25:]):
        preamble = xmas_data[i:i+25]
        if not validator(num, preamble):
            break
    print("The first number that does not have the property is:", num)
# Part 2
    result = encryption_weakness(num, i+25, xmas_data)
    print("The encryption weakness is:", result)
