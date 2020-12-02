# December 2nd, - Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman


def crack_policy(policy):
    cuan, letter, password = policy.split()
    mini, maxi = list(map(int, cuan.split("-")))
    return letter[0], mini, maxi, password


def validator(char, mini, maxi, password):
    """validate the password 1st part"""
    if mini <= password.count(char) <= maxi:
        return 1
    else:
        return 0


def new_policy_validation(char, ind1, ind2, password):
    """validate the password 2nd part new policy"""
    if password[ind1-1] == char and password[ind2-1] != char:
        return 1
    elif password[ind1-1] != char and password[ind2-1] == char:
        return 1
    else:
        return 0


if __name__ == "__main__":
    f = open("InputDay2_2020.txt", "r")
    input_arr = list(map(str, f.read().split("\n")))
    n = 0
    m = 0
    for rule in input_arr:
        char, mini, maxi, password = crack_policy(rule)
        n += validator(char, mini, maxi, password)
        m += new_policy_validation(char, mini, maxi, password)
    print("Valid passwords:", n)
    print("Valid passwords new policy:", m)
