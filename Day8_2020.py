# December 8th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman
from copy import deepcopy


def operation(data):
    # Executes the code, if it reach the infity loop returns False, if it execute complete return True
    i = 0
    acc = 0
    while i < len(data):
        if data[i][2] == False:
            if data[i][0] == "jmp":
                data[i][2] = True
                i = eval(str(i)+data[i][1])
            elif data[i][0] == "acc":
                data[i][2] = True
                acc = eval(str(acc)+data[i][1])
                i += 1
            elif data[i][0] == "nop":
                data[i][2] = True
                i += 1
        else:
            return acc, False
    return acc, True


if __name__ == "__main__":
    with open("InputDay8_2020.txt", "r") as file:
        code = file.read().split("\n")
    list_code = []
    for instruction in code:
        # Add a flag for vitited
        list_code.append(instruction.split() + [False])
    # copy to have the original list of instructions for the part 2
    original_code = deepcopy(list_code)
    acc, complete = operation(list_code)
    print("Accumulator before looping is:", acc)
    # 2nd part, searching for the corrupted instruction
    n = 0
    while complete == False:
        data = deepcopy(original_code)
        if data[n][0] == "nop" and data[n][1] != "+0":  # Border condition.
            data[n][0] = "jmp"
        elif data[n][0] == "jmp":
            data[n][0] = "nop"
        n += 1
        acc, complete = operation(data)
    print("Accumulator after executing the program correctly:", acc)
