# December 3rd, Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman

# 2nd part slopes:
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def tree_counter(terrain, right, down):
    # Counts the tree in the way
    end = len(terrain)
    pos = [0, 0]
    trees = 0
    while pos[1] < end:
        if terrain[pos[1]][pos[0]] == "#":
            trees += 1
        pos[0] += right
        pos[1] += down
        if pos[0] >= len(terrain[0]):
            pos[0] = pos[0] % len(terrain[0])
    return trees


if __name__ == "__main__":
    f = open("InputDay3_2020.txt", "r")
    input_arr = list(f.read().split("\n"))
    trees = tree_counter(input_arr, 3, 1)
    print("You would encounter: ", trees, " trees")
    # 2nd part
    mult_trees = 1
    for right, down in slopes:
        mult_trees *= tree_counter(input_arr, right, down)
    print("the multiplication of all the trees found is: ", mult_trees)
