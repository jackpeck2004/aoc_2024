import os

file = os.environ.get("INPUT_FILE", "input.txt")


def main_1(f):
    inp = []
    for line in f:
        tmp = []
        for char in line[:-1]:
            tmp.append(char)
        inp.append(tmp)
    # print(inp)

    s = 0

    for row, l in enumerate(inp):
        # print(len(l))
        for col, c in enumerate(l):
            if c != "X":
                continue
            # check for XMAS to the left
            if col >= 3:
                if inp[row][col - 1] == "M" and inp[row][col - 2] == "A" and inp[row][col - 3] == "S":
                    s += 1
            # check for XMAS to the right
            if col <= len(l) - 4:
                if inp[row][col + 1] == "M" and inp[row][col + 2] == "A" and inp[row][col + 3] == "S":
                    s += 1
            # check for XMAS to the top
            if row >= 3:
                if inp[row - 1][col] == "M" and inp[row - 2][col] == "A" and inp[row - 3][col] == "S":
                    s += 1
            # check for XMAS to the bottom
            if row <= len(inp) - 4:
                if inp[row + 1][col] == "M" and inp[row + 2][col] == "A" and inp[row + 3][col] == "S":
                    s += 1
            # check for XMAS to the left and top diagonal
            if row >= 3 and col >= 3:
                if inp[row - 1][col - 1] == "M" and inp[row - 2][col - 2] == "A" and inp[row - 3][col - 3] == "S":
                    s += 1
            # check for XMAS to the right and top diagonal
            if row >= 3 and col <= len(l) - 4:
                if inp[row - 1][col + 1] == "M" and inp[row - 2][col + 2] == "A" and inp[row - 3][col + 3] == "S":
                    s += 1
            # check for XMAS to the left and bottom diagonal
            if row <= len(inp) - 4 and col >= 3:
                if inp[row + 1][col - 1] == "M" and inp[row + 2][col - 2] == "A" and inp[row + 3][col - 3] == "S":
                    s += 1
            # check for XMAS to the right and bottom diagonal
            if row <= len(inp) - 4 and col <= len(l) - 4:
                if inp[row + 1][col + 1] == "M" and inp[row + 2][col + 2] == "A" and inp[row + 3][col + 3] == "S":
                        s += 1

    return s


            
def main_2(f):
    cn = 0
    # find two MAS forming an X
    lines = f.readlines()
    for y, line in enumerate(lines[1:-1]):
        for x, c in enumerate(line[1:-1]):
            if c != "A":
                continue
            row = y + 1
            col = x + 1
            d = 0
            if (lines[row - 1][col - 1] == "M" and lines[row + 1][col + 1] == "S"):
                d += 1
            if lines[row - 1][col + 1] == "M" and lines[row + 1][col - 1] == "S":
                d += 1
            if lines[row + 1][col - 1] == "M" and lines[row - 1][col + 1] == "S":
                d += 1
            if lines[row + 1][col + 1] == "M" and lines[row - 1][col - 1] == "S":
                d += 1
            if d == 2:
                cn += 1
    return cn


if __name__ == "__main__":
    with open(file) as f:
        # print(main_1(f))
        print(main_2(f))
