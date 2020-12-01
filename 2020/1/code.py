# Advent of code Year 2020 Day 1 solution
# Author = Omar Oueidat
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'rt') as input_file:
    input = input_file.read()
    
input_as_int = [int(line) for line in input.splitlines()]
sorted_list = sorted(input_as_int)
result_2 = 0
size = len(sorted_list)
i = 0
j = size-1
result = 0

for i in input_as_int[:-1]:
    if (2020-i) in input_as_int:
        result = i * (2020-i)
        break

for i in input_as_int[:-1]:
    for j in input_as_int:
        if (2020-i-j) in input_as_int:
            result_2 = i * j * (2020-i-j)
    


print("Part One : "+ str(result))


print("Part Two : "+ str(result_2))