# December 4th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman
import re

KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def valid_passport_1(data):
    for key in KEYS:
        if re.search(key, data) == None:
            return 0
    return 1


def valid_passport_2(data):
    dic = dict()
    passport_data_1 = data.replace("\n", " ")
    passport_data_2 = passport_data_1.split()
    for da in passport_data_2:
        x = da.split(":")
        dic.update({x[0]: x[1]})
    if (1920 <= int(dic.get("byr")) <= 2002) and (2010 <= int(dic.get("iyr")) <= 2020) and (2020 <= int(dic.get("eyr")) <= 2030) and (dic.get("ecl") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        hgt = dic.get("hgt")
        if (("cm" in hgt) and (150 <= int(hgt.strip("cm")) <= 193)) or (("in" in hgt) and (59 <= int(hgt.strip("in")) <= 76)):
            pid = dic.get("pid")
            if len(pid) == 9:
                if re.search("[0-9]{9}", pid) != None:
                    hcl = dic.get("hcl")
                    if re.search("^#[0-9a-f]{6}$", hcl) != None:
                        return 1
    return 0


if __name__ == "__main__":
    valid = 0
    new_list = []
    with open("InputDay4_2020.txt", "r") as f:
        passport_list = list(f.read().split("\n\n"))
    for passport in passport_list:
        if valid_passport_1(passport):
            valid += 1
            new_list.append(passport)
    print("Total of valid passports:", valid)
    # 2nd part
    valid = 0
    for passport in new_list:
        valid += valid_passport_2(passport)
    print("New rules valid passport:", valid)
