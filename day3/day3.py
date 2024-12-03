import os
import re

mul_regex = r"mul\(\d{1,3},\d{1,3}\)"
input_file = os.environ.get("INPUT_FILE", "input.txt")

def get_sum_of_muls(line):
    s = 0
    muls = re.findall(mul_regex, line)
    for mul in muls:
        # extract the numbers from the mul
        mul_nums = re.findall(r"\d+", mul)
        s += int(mul_nums[0]) * int(mul_nums[1])
    return s

def main_1(f):
    s = 0
    for line in f:
        # use regex to extract all the muls (e.g. mul(2,3))
        s += get_sum_of_muls(line)

    return s

def split_with_marker(line, marker):
    spl = line.split(marker)
    for x in range(len(spl[:-1])):
        spl.insert(x+1, marker)
    return spl

def main_2(f):
    s = 0
    enabled = True
    for line in f:
        y = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line)
        for x in y:
            if x == "do()":
                enabled = True
                continue
            if x == "don't()":
                enabled = False
                continue
            if enabled:
                s += get_sum_of_muls(x)
    return s
    



if __name__ == "__main__":
    with open(input_file) as f:
        # print(main_1(f))
        print(main_2(f))
