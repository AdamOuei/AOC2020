# Advent of code Year 2020 Day 4 solution
# Author = Omar Oueidat
# Date = December 2020

import re 
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()






valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
fields = input.split('\n\n')

# PART 1
val1 = val2 = 0
for field in fields:
    passport = re.split('[\n ]', field)
    passport_fields = dict(passpor.split(':') for passpor in passport)
    
    if all(valid_field in passport_fields for valid_field in valid_fields ):
        val1 += 1
        # PART 2
        print((passport_fields['hgt'][-2:] == 'cm' and   150 <= int(passport_fields['hgt'][:-2]) <= 190))
        if 1920 <= int(passport_fields['byr']) <= 2002\
                    and 2010 <= int(passport_fields['iyr']) <=2020\
                    and 2020 <= int(passport_fields['eyr']) <= 2030\
                    and ((passport_fields['hgt'][-2:] == 'cm' and  150 <= int(passport_fields['hgt'][:-2]) <= 193  )\
                        or (passport_fields['hgt'][-2:] == 'in' and 59 <= int(passport_fields['hgt'][:-2]) <= 76  ))\
                    and re.match('^#[a-f\d]{6}$', passport_fields['hcl'])\
                    and (passport_fields['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'])\
                    and re.match('^\d{9}$',passport_fields['pid']): 
            val2 += 1






print("Part One : "+ str(val1))



print("Part Two : "+ str(val2))