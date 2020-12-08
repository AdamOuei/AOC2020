# Advent of code Year 2020 Day 7 solution
# Author = Omar Oueidat
# Date = December 2020
import re
import collections

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

bags = [bag for bag in input.splitlines()]
set_dict = collections.defaultdict(set)
isInList = collections.defaultdict(list)
for lines in bags:
    color = re.match(r'(.+?) bags contain',lines)[1]
    for amount, child in re.findall(r'(\d+) (.+?) bags?[,.]',lines):
        amount = int(amount)
        set_dict[child].add(color)
        isInList[color].append((amount,child))


sets = set()
def recursion(check_color):
    for color in set_dict[check_color]:
        sets.add(color)
        recursion(color)

recursion('shiny gold')
print(sets)

def recursion2 (check_color):
    val = 0
    for amount, child in isInList[check_color]:
        val += amount
        val += amount * recursion2(child)
    return val



print("Part One : "+ str(len(sets)))



print("Part Two : "+ str(recursion2('shiny gold')))