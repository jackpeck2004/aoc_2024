# locations identified by location ID
# INPUT FROMAT: two side-by-side lists of locations IDs is the input
# TASK:
#   Pair up the smallest location IDS of the left list with the smallest location IDS of the right list
#   Find distance between the paired locations
#   add up all of the distances
import heapq

input_file_path = "input.txt"

def main_1():

    # two min-heaps
    left_heap = []
    right_heap = []
    heapq.heapify(left_heap)
    heapq.heapify(right_heap)

    with open(input_file_path, "r") as f:
        for line in f:
            inp = line.split()
            heapq.heappush(left_heap, int(inp[0]))
            heapq.heappush(right_heap, int(inp[1]))

    diff = 0
    while len(left_heap) > 0:
        left = heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)
        diff += abs(left- right) 

    return diff

def main_2():
    freq = {}

    arr = []

    with open(input_file_path, "r") as f:
        for line in f:
            inp = line.split()
            freq[int(inp[0])] = 0
            arr.append(int(inp[1]))
    
    # keys = list(freq.keys())
    for i in arr:
        if i in freq:
            freq[i] += 1

    sum = 0
    for k, v in freq.items():
        sum += k*v

    return sum



if __name__ == "__main__":
    print(f"Day 1 part 1: {main_1()}")
    print(f"Day 1 part 2: {main_2()}")
