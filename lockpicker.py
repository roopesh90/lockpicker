#!/usr/bin/python3
import math
slots_n = 4
slots_min = 1
slots_max = 6

picks = []
min_digit = 0
#First pick
for x in reversed(range(slots_min,slots_n)):
    min_digit += (math.pow(10, x))
min_digit += slots_min
print(min_digit)


#series_min = slots_min
