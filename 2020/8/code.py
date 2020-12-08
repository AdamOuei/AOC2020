# Advent of code Year 2020 Day 8 solution
# Author = Omar Oueidat
# Date = December 2020
import re
import itertools
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_ = [line for line in input.splitlines()]
actions = []
for action in input_:
    val = re.search(r'[+,-]\d+$',action)[0]
    inst = re.match(r'^[a-z]{3}',action)[0]
    actions.append((inst,val))

accu = 0
done_inst = set()
def loop(list,index):
    global accu
    if index in done_inst:
        return 
    size = len(actions)
    done_inst.add(index)
    (inst,val) = list[index]
    if inst == 'jmp':
        index = (index + int(val)) % size
    elif inst == 'acc':
        accu += int(val)
        index = (index + 1) % size     
    elif inst == 'nop':
        index = (index + 1) % size
        
    loop(actions,index)

loop(actions, 0)
print("Part One : "+ str(accu))

def part2(n_runs):
    pointer = 0
    accu2 = 0
    checked = set()
    while  (0 <= pointer < len(actions)):
        if pointer in checked:
            return None
        checked.add(pointer)
        (inst,val) = actions[pointer]
        if pointer == n_runs and inst == 'jmp':
            inst = 'nop'            
        elif pointer == n_runs and inst == 'nop':
            inst = 'jmp'
        if inst == 'jmp':
            pointer += int(val) 
        elif inst == 'acc':
            accu2 += int(val)
            pointer += 1   
        elif inst == 'nop':
            pointer += 1
    return accu2

results = 0
for i in range(len(actions)):
    res = part2(i)
    if res is not None:
        results = res
        
print("Part Two : "+ str(results))
        