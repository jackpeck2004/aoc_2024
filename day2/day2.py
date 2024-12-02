import os

file = os.environ.get("INPUT_FILE", "input.txt")
DEBUG = os.environ.get("DEBUG", False)

def main_1():
    with open(file, "r") as f:
        c = 0
        for line in f:
            c += 1
            report = line.split()
            prev = int(report[0])
            desc = int(report[1]) < prev
            for entry in report[1:]:

                diff = abs(int(entry) - int(prev))
                if diff < 1 or diff > 3:
                    c -= 1
                    break

                if desc:
                    if int(entry) > int(prev):
                        c -= 1
                        break
                else:
                    if int(entry) < int(prev):
                        c -= 1
                        break

                prev = entry
        return c

def x(entry, prev, desc):
    diff = abs(int(entry) - int(prev))
    if diff < 1 or diff > 3:
        return False

    if desc:
        if int(entry) > int(prev):
            return False
    else:
        if int(entry) < int(prev):
            return False
    return True


def is_safe(report, remove=False):
    prev = int(report[0])
    desc = int(report[1]) < prev
    for entry in report[1:]:
        ret = x(entry, prev, desc)
        if not ret:
            return False

        prev = entry

        # if not ret:
        #     if remove:
        #         # create a copy without the entry
        #         cp = report.copy()
        #         cp.remove(entry)
        #         # check if removing the entry the report is safe
        #         c = is_safe(cp)
        #         print(entry) if c else None
        #         if not c:
        #             return False
        #     else:
        #         return False

    print("safe") if remove else None
    return True


def main_2():
    with open(file, "r") as f:
        safe_reports = 0
        for line in f:
            print(line)
            input() if DEBUG else None
            report = line.split()
            if is_safe(report):
                safe_reports += 1
            else:
                for i, entry in enumerate(report):
                    cp = report.copy()
                    cp.pop(i)
                    print(f"remove {entry} at pos: {i}")
                    if is_safe(cp):
                        print(f"remove {entry} is safe")
                        safe_reports += 1
                        break


        #     if is_safe(report, remove=True):
        #         c += 1
        return safe_reports 


if __name__ == "__main__":
    # print(f"Day 2 part 1: {main_1()}")
    # print(f"Day 2 part 2: {main_2()}")
    print(main_2())
