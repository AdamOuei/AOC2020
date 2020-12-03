# Advent of code Year 2020 Day 3 solution
# Author = Omar Oueidat
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_ = [line for line in input.splitlines()]

## PART 1

pos = 0
n_of_trees = 0
for line in input_[1:]:
    w = len(line)
    pos = (pos + 3) % w
    if (line[pos] == '#'):
        n_of_trees += 1

## PART 2

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
val = 1
n_of_trees2 = 0

for (r,d) in slopes: 
    pos = -r
    n_of_trees2 = 0    
    for line in input_[::d]:
        w = len(line)
        pos = (pos + r) % w
        if(line[pos] == '#'):
            n_of_trees2 += 1
    val *= n_of_trees2


 
print("Part One : "+ str(n_of_trees))



print("Part Two : "+ str(val))