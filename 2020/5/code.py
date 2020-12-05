# Advent of code Year 2020 Day 5 solution
# Author = Omar Oueidat
# Date = December 2020
import math
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

b_pass = [line for line in input.splitlines()]
h_id = 0
id_list = []

# PART 1
for b in b_pass:
    iid = int(b.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2)
    id_list.append(iid)
h_id = max(id_list)

# PART 2
my_seat = 0

for seat in range(2**10):

    if (seat not in id_list) and (seat+1 in id_list) and (seat-1 in id_list):
        my_seat = seat
    
print("Part One : "+ str(h_id))

print("Part Two : "+ str(my_seat))