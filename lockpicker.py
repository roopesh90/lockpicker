#!/usr/bin/python3
import math
slots_n = 4
slots_min = 1
slots_max = 6

picks = []
min_digit = 0
max_digit = 0
#First pick
for x in reversed(range(slots_min,slots_n)):
    min_digit += (math.pow(10, x))
min_digit += slots_min
print(min_digit)
#last pick
for x in reversed(range(slots_max,slots_max+slots_n)):
    max_digit += (math.pow(10, x))
max_digit += slots_max
print(max_digit)


#series_min = slots_min
