#!/usr/bin/python3
import math
slots_n = 4
slots_min = 1
slots_max = 6

picks = []

def slot_gen(_digit):
    slot = 0
    slot += _digit
    for x in reversed(range(1,slots_n)):
        slot += slots_min * (math.pow(10, x))
    return slot
    
#First pick
min_digit= slot_gen(slots_min)
print(min_digit)
#last pick
max_digit = slot_gen(slots_max)
print(max_digit)
