#!/usr/bin/python3
import math
slots_n = 4
slots_min = 1
slots_max = 6

picks = []

def slot_gen(U_digit, L_digit, slots_n):
    u_limits = []
    for _digit in range(U_digit,L_digit+1):
        slot = 0
        slot += _digit
        for x in reversed(range(1,slots_n)):
            slot += _digit * (math.pow(10, x))
        u_limits.append(slot)
        for x in range(U_digit,L_digit):
            u_limits.append(slot+x)
    return u_limits
    
#First pick
min_digit= slot_gen(slots_min, slots_max, slots_n)
print(min_digit)
