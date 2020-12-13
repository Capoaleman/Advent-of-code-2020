# December 12th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman


def arrive_time(timestamp, bus):
    return (timestamp//bus)*bus + bus


if __name__ == "__main__":
    with open("InputDay13_2020.txt", "r") as file:
        timestamp = int(file.readline())
        bus_id = file.readline().split(",")
    minim = timestamp + 100000
    minbus = 0
    for bus in bus_id:
        if bus != "x":
            time = arrive_time(timestamp, int(bus))
            if time < minim:
                minim = time
                minbus = int(bus)
    print("Part1 result:", minbus*(minim-timestamp))
    # Part 2
    bus_wID = {bus: bus_id.index(bus) for bus in bus_id if bus != "x"}
    t = 1
    a = 1
    for bus, offset in bus_wID.items():
        while True:
            if (t+offset) % int(bus) == 0:
                break
            t += a
        a *= int(bus)
    print(f"Part2 result: {t}")
