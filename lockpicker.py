#!/usr/bin/python3
import platform, os, math
from random import randrange

slots_n = 4
slots_min = 1
slots_max = 6

slots = []
slots_picked = []

def clear_screen():
    # platforn independent
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')

def slot_to_num(slot_list):
    # print(slot_list)
    number = lambda nums: int(''.join(str(i) for i in slot_list))
    return number(slot_list)

def slot_gen(L_digit, U_digit, slots_n=4):
    slots_list = []
    for i in range(L_digit,U_digit+1):
        for j in range(L_digit,U_digit+1):
            for k in range(L_digit,U_digit+1):
                for l in range(L_digit,U_digit+1):
                    slot_list = [i,j,k,l]
                    slot_number = slot_to_num(slot_list)
                    slots_list.append(slot_number)
                # print()
                # input()
    # print(slots_list)
    return slots_list

#gereate slots    
slots= slot_gen(slots_min, slots_max)
# picking a random slot
while len(slots)>0:
    clear_screen()
    random_index = randrange(0,len(slots))
    print("\t 4digit Combi-lock key generator\n")
    print("\nnumber of tries: %d" % len(slots_picked))
    print("\nnumber of tries left: %d" % len(slots))
    print("\n\t Try :\t%d" % slots[random_index])
    slots_picked.append(slots[random_index])
    check = str(input("\nDid that help?[Y/n]"))
    if check.lower()=="y":
        clear_screen()
        print("\n\n\tCONGRATS:::::>>> %d  works!!!\n\n" % slots[random_index])
        # print("combinations tried: ")
        # print(slots_picked)
        break
    del slots[random_index]
