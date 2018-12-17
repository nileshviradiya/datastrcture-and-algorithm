from math import floor, ceil
from heapq import heappush, heappop
def roundNumbers(input):
    output = [floor(x) for x in input]
    remain = round(sum(input) - sum(output))
    it = sorted(enumerate(input), key=lambda i: i[1] - floor(i[1]))
    print(it)
    for _ in range(remain):
        output[it.pop()[0]] += 1

    return output

input = [30.3,2.4,3.5]
print(roundNumbers(input))