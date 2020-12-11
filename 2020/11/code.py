# Advent of code Year 2020 Day 11 solution
# Author = Omar Oueidat
# Date = December 2020
import itertools
from copy import deepcopy

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

seats = [list('.' + line.strip() + '.')  for line in input.splitlines()]
seats = [['.'] * len(seats[0])] + seats + [['.'] * len(seats[0])]

rows = len(seats)
cols = len(seats[0])

old_seats = None

while seats != old_seats:
    old_seats = deepcopy(seats)
    for row in range(rows):
        for col in range(cols):
            if old_seats[row][col] == '.':
                continue
            counter = 0
            for x,y in itertools.product((1,0,-1),repeat=2):
                if (x,y) != (0,0) and old_seats[row + x][col + y] == '#':
                    counter += 1
            if counter == 0:
                seats[row][col] = '#'
            elif counter >= 4:
                seats[row][col] = 'L'

print("Part One : "+ str(sum(row.count('#') for row in seats )))

seats2 = [list('O' + line.strip() + 'O')  for line in input.splitlines()]
seats2 = [['O'] * len(seats2[0])] + seats2 + [['O'] * len(seats2[0])]
old_seats = None
## PART 2:
while seats2 != old_seats:
    old_seats = deepcopy(seats2)
    for row in range(len(seats2)):
        for col in range(len(seats2[0])):
            if old_seats[row][col] in '.O':
                continue
            counter = 0
            for x,y in itertools.product((-1,0,1),repeat=2):
                if (x,y) == (0,0):
                    continue
                for watch in itertools.count(1):
                    seat = old_seats[row + watch * x][col + watch * y]
                    if seat != '.':
                        counter += (seat == '#')
                        break
            if counter == 0:
                seats2[row][col] = '#'
            elif counter >= 5:
                seats2[row][col] = 'L'

print("Part Two : "+ str(sum(row.count('#') for row in seats2 )))