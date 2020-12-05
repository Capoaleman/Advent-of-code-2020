# December 5th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman


def binary_partition(li, code):
    # Parts the list and returns the desired half
    if code == "F" or code == "L":
        return li[:len(li)//2]
    else:
        return li[len(li)//2:]


def get_seat_id(seat):
    # Calculates the seat ID after decoding the seat code
    row = [n for n in range(128)]
    column = [n for n in range(8)]
    for code in seat:
        if code == "F" or code == "B":
            row = binary_partition(row, code)
        else:
            column = binary_partition(column, code)
    return row[0]*8+column[0]


if __name__ == "__main__":
    with open("InputDay5_2020.txt", "r") as file:
        seat_data = list(file.read().split("\n"))
    all_seat_id = []
    for seat in seat_data:
        all_seat_id.append(get_seat_id(seat))
    max_id = max(all_seat_id)
    print("The highest id is:", max_id)
    # 2nd part, with sets, we can find the missing seat by join the all_seat_id with a set with all the id that should be in the aircraft
    min_id = min(all_seat_id)
    all_seats = set([n for n in range(min_id, max_id+1)])
    my_seat = all_seats.difference(all_seat_id)
    print("My id seat is:", my_seat)
