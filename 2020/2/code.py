# Advent of code Year 2020 Day 2 solution
# Author = Omar Oueidat
# Date = December 2020

import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_ = [line for line in input.splitlines()]
n_valid = 0
for i in input_:
    split = i.split(':')
    char = split[0][-1]
    numbers = re.findall('[0-9]+',split[0])
    occurences = split[1].count(char)
    if (occurences >= int( numbers[0]) and occurences <= int (numbers[1])):
        n_valid += 1
input_2 = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]
n_valid2 = 0
for i in input_:
    split = i.split(':')
    char = split[0][-1]
    numbers = re.findall('[0-9]+',split[0])
    string = split[1]
    low = int(numbers[0])
    high = int(numbers[1])
    #print("The string was {} and the number interval was {} and {} and character was : {}".format(string,low,high,char))
    #print(string[low])
    #print(string[high])
    if ( bool(char == string[low]) ^ bool(char == string[high])):
        n_valid2 += 1

    



print("Part One : "+ str(n_valid))



print("Part Two : "+ str(n_valid2))