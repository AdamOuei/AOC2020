# Advent of code Year 2020 Day 6 solution
# Author = Omar Oueidat
# Date = December 2020
import string
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n\n')


correct_ans = []

for i in input:
    ans = i.split('\n')
    char_ans = [list(char) for char in ans]
    flat_char = [val for sublist in char_ans for val in sublist]
    unique_ans = set(flat_char)
    correct_ans.append(len(unique_ans))

## PART2

correct_ans2 = []
for i in input:
    tmp = i.split('\n')
    letters = set(string.ascii_lowercase)
    for ans in tmp:
        letters &= set(char for char in ans if 'a' <= char <= 'z') 
    correct_ans2.append(len(letters))
            

print("Part One : "+ str(sum(correct_ans)))



print("Part Two : "+ str(sum(correct_ans2)))