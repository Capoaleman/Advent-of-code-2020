# December 10th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman


def jolt_dif(data):
    one_dif = 0
    three_dif = 0
    prev = 0
    for adap in data:
        if adap - prev > 3:
            break
        elif adap - prev == 1:
            one_dif += 1
        elif adap - prev == 3:
            three_dif += 1
        prev = adap
    return one_dif, three_dif


if __name__ == "__main__":
    with open("InputDay10_2020.txt", "r") as file:
        adapters = sorted(list(map(int, file.read().splitlines()))+[0])
    adapters.append(max(adapters)+3)
    one, three = jolt_dif(adapters)
    print(f"Part 1: {one*three}")
    # part 2
    # Calculates the way to get to every jolt, the last one have the answer
    ways = [1] * (adapters[-1] + 1)
    for d in adapters[1:]:
        ways[d] = sum(ways[n] for n in range(d - 3, d) if n in adapters)
    print(f"Part 2: {ways[-1]}")
