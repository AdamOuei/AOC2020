# Advent of code Year 2020 Day 10 solution
# Author = Omar Oueidat
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

adap = [int(line) for line in input.splitlines()]

adap.append(3 + max(adap))
adap.append(0)
adap = sorted(adap)


n_1 = 0
n_3 = 0
for i in range(len(adap)-1):
    diff = adap[i+1] - adap[i]
    if diff == 1:
        n_1 += 1
    elif diff == 3:
        n_3 += 1


print("Part One : "+ str(n_3*n_1))

checked = {}
def recursion(adapter):
    if adapter == len(adap) -1:
        return 1
    if adapter in checked:
        return checked[adapter]
    val = 0
    for j in range(adapter+1,len(adap)):
        if adap[j] - adap[adapter] == 1:
            val += recursion(j)
        if adap[j] - adap[adapter] == 2:
            val += recursion(j)
        if adap[j] - adap[adapter] == 3:
            val += recursion(j)
    checked[adapter] = val
    return val

print("Part Two : "+ str(recursion(0)))