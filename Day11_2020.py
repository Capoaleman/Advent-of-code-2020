# December 11th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman

from copy import deepcopy


def simulation_2(current, next_state):
    # 2nd part simulation
    going = False
    for i, line in enumerate(current):
        for j, seat in enumerate(line):
            change = True
            if seat == ".":
                continue
            elif seat == "#":
                count = 0
                for row, col in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    n = 1
                    while True:
                        if i+n*row >= 0 and j+n*col >= 0 and i+n*row < len(current) and j+n*col < len(line):
                            if current[i+n*row][j+n*col] == "#":
                                count += 1
                                break
                            elif current[i+n*row][j+n*col] == "L":
                                break
                            else:
                                n += 1
                        else:
                            break
                if count < 5 and seat == "#":
                    change = False
            elif seat == "L":
                for row, col in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    n = 1
                    while True:
                        if i+n*row >= 0 and j+n*col >= 0 and i+n*row < len(current) and j+n*col < len(line):
                            if current[i+n*row][j+n*col] == "#":
                                change = False
                                break
                            elif current[i+n*row][j+n*col] == "L":
                                break
                            else:
                                n += 1
                        else:
                            break
                    if not change:
                        break
            if change:
                going = True
                if seat == "#":
                    next_state[i][j] = "L"
                elif seat == "L":
                    next_state[i][j] = "#"
    return going, next_state


def simulation(current, next_state):
    # 1st Part simulation
    going = False
    for i, line in enumerate(current):
        for j, seat in enumerate(line):
            change = True
            if seat == ".":
                continue
            else:
                count = 0
                for row in [-1, 0, 1]:
                    for col in [-1, 0, 1]:
                        try:
                            if i+row >= 0 and j+col >= 0 and current[i+row][j+col] == "#":
                                count += 1
                        except:
                            continue
                if (count < 5 and seat == "#") or (count != 0 and seat == "L"):  # It is counting itself
                    change = False
            if change:
                going = True
                if seat == "#":
                    next_state[i][j] = "L"
                elif seat == "L":
                    next_state[i][j] = "#"
    return going, next_state


if __name__ == "__main__":
    with open("InputDay11_2020.txt", "r") as file:
        data = file.read().splitlines()
    seat_data = []
    for i, line in enumerate(data):
        seat_data.append([])
        for j, word in enumerate(line):
            seat_data[i].append(word)
    going = True
    sec_part_seat = deepcopy(seat_data)
    while going:
        next_step = deepcopy(seat_data)
        going, seat_data = simulation(seat_data, next_step)
    n = sum(1 for line in seat_data for seat in line if seat == "#")
    print(f"There are {n} seats occupied")
    going = True
    while going:
        next_step = deepcopy(sec_part_seat)
        going, sec_part_seat = simulation_2(sec_part_seat, next_step)
    n = sum(1 for line in sec_part_seat for seat in line if seat == "#")
    print(f"There are {n} seats occupied for part 2")
