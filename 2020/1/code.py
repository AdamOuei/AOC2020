# Advent of code Year 2020 Day 1 solution
# Author = Omar Oueidat
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'rt') as input_file:
    input = input_file.read()
    
input_as_int = [int(line) for line in input.splitlines()]
sorted_list = sorted(input_as_int)
print(sorted_list)
size = len(sorted_list)
for i in input_as_int:
    for j in input_as_int:
        for k in input_as_int:
            if(i + j + k == 2020):
                print(i*j*k)


print("Part One : "+ str(None))


print("Part Two : "+ str(None))