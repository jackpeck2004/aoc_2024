import os

input_file = os.environ.get('INPUT_FILE', 'input.txt')
DEBUG = os.environ.get('DEBUG', False)
PRINT = os.environ.get('PRINT', False)

def can_add(num, seen, nums, rules):
    if num in rules:
        a = set(rules[num])
        required = a.intersection(set(nums))
        h = seen.intersection(required)
        # if h == required:
            # print("num", num) if PRINT else None
            # print("a", a) if PRINT else None
            # print("r", required) if PRINT else None
            # print("h", h) if PRINT else None
        return h == required

def read_rules(lines):
    reading_rules = True
    i = 0
    rules = {}
    while reading_rules:
        line = lines[i]
        if lines[i+1] == '\n':
            reading_rules = False
        [b, a] = line.split('|')
        Y = a.strip()
        X = b.strip()
        if Y in rules:
            rules[Y].append(int(X))
        else:
            rules[Y] = [int(X)]
        i+=1
    return rules, i

def is_valid(nums, rules):
    seen = set([nums[0]])
    # 75,47,61,53,29
    valid = True
    for num in nums[1:]:
        seen.add(num)
        if not can_add(str(num), seen, nums, rules):
            valid = False
            break
    return valid

def main_1(f):
    lines = f.readlines()
    rules, i = read_rules(lines)

    s = 0
    while i < len(lines) - 1:
        line = lines[i + 1]
        nums = list(map(lambda num: int(num.strip()), line.strip().split(',')))
        valid = is_valid(nums, rules)
        if valid:
            s += int(nums[(len(nums) - 1) // 2])

        i+=1
    return s

def fix(nums, rules):
    # get all the rules which are being violated by nums
    seen = set()
    i = 0
    while i < len(nums):
        print(i) if PRINT else None
        print("nums", nums) if PRINT else None
        input() if DEBUG else None
        num = nums[i]
        seen.add(num)
        print("seen", seen) if PRINT else None
        input() if DEBUG else None
        if not str(num) in rules:
            i += 1
            continue
        # rules for num
        a = set(rules[str(num)])
        print("rules for num", num, a) if PRINT else None
        input() if DEBUG else None
        

        # get list of the rules of num which include the elements of nums
        required = a.intersection(set(nums))
        print("required", required) if PRINT else None
        input() if DEBUG else None
        

        h = seen.intersection(required)
        print("h", h) if PRINT else None
        input() if DEBUG else None
        

        if h != required:
            violated = required - h
            print("violated", violated) if PRINT else None
            input() if DEBUG else None
            
            for v in violated:
                v_idx = nums.index(v)
                nums[v_idx], nums[i] = nums[i], nums[v_idx]
                seen = set(nums[:i+1])

        print("nums", nums) if PRINT else None
        input() if DEBUG else None
        print("seen", seen) if PRINT else None
        input() if DEBUG else None
        
        i += 1
    return nums


def main_2(f):
    lines = f.readlines()
    rules, i = read_rules(lines)
    
    s = 0

    while i < len(lines) - 1:
        line = lines[i + 1]
        nums = list(map(lambda num: int(num.strip()), line.strip().split(',')))
        com = False
        while not is_valid(nums, rules):
        # valid = is_valid(nums, rules)
        # if not valid:
            # inplace fix
            print(nums)
            input() if DEBUG else None
            fix(nums, rules)
            print("fixed")
            print(nums)
            print("\n") if PRINT else None
            input() if DEBUG else None
            com = True
        assert(is_valid(nums, rules))
        if com:
            s += int(nums[(len(nums) - 1) // 2])

        i+=1
    return s

if __name__ == '__main__':
    with open(input_file) as f:
        # print(main_1(f)) if PRINT else None
        print(main_2(f))

