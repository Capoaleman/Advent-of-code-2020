# December 14th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman

from copy import deepcopy


def update_mask(mask, num):
    h = str()
    for i, n in enumerate(num):
        if mask[i] == "X":
            h += n
        else:
            h += mask[i]
    return int(h, 2)


def apply_mask(mask, num):
    h = []
    for i, n in enumerate(mask):
        if n == "0":
            h.append(num[i])
        else:
            h.append(n)
    return h


if __name__ == "__main__":
    memory = {}
    memory_v2 = {}
    with open("InputDay14_2020.txt", "r") as file:
        data = file.read().splitlines()
    for line in data:
        if "mask" in line:
            mask = line.replace("mask = ", "")
            x = mask.count("X")
        else:
            tmp = line.split(" = ")
            memory[tmp[0].strip("me[]")] = update_mask(
                mask, bin(int(tmp[1]))[2:].zfill(36))
            # Part 2
            addres = bin(int(tmp[0].strip("me[]")))[2:].zfill(36)
            with_mask = apply_mask(mask, addres)
            for i in range(int(pow(2, x))):
                temp_address = deepcopy(with_mask)
                change = bin(i)[2:].zfill(x)
                for a in change:
                    ind = temp_address.index("X")
                    temp_address[ind] = a
                memory_v2["".join(temp_address)] = int(tmp[1])
    print(sum(memory.values()))
    print(sum(memory_v2.values()))
