# Advent of code Year 2020 Day 9 solution
# Author = Omar Oueidat
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


input_ = [int(line) for line in input.splitlines()]

test_input = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]

preamble = 25
ans1 = 0
ans2 = 0
for i in range(preamble,len(input_)):
    check = input_[i-preamble:i]
    is_correct = False
    for k in range(preamble):  
        for j in range(preamble):
            if check[k] + check[j] == input_[i]:
                is_correct = True
    if not is_correct:
        ans1 = input_[i]

for i in range(len(input_)):
    for j in range(i+2,len(input_)):
        check = input_[i:j]
        if sum(check) == ans1:
            ans2 = min(check)+max(check)
                                
        


print("Part One : "+ str(ans1))



print("Part Two : "+ str(ans2))