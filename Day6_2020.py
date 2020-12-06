# December 6th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman


def count_answers(form):
    # Returns the total of yes answer, 1 per question
    return len(set(form))


def every_yes(form):
    # Returns the total of yes answer, 1 per question per group
    new_group = set(form.pop(0))
    for person in form:
        new_group = new_group.intersection(set(person))
    return len(new_group)


if __name__ == "__main__":
    answer = 0
    with open("InputDay6_2020.txt", "r") as file:
        data = file.read().split("\n\n")
    for group in data:
        answer += count_answers(group.replace("\n", ""))
    print("Total yes answer:", answer)
    # 2nd part
    answer = 0
    for group in data:
        answer += every_yes(group.split("\n"))
    print("Total yes answer per group:", answer)
