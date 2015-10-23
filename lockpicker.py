#!/usr/bin/python3
import math
slots_n = 4
slots_min = 1
slots_max = 6

picks = []

def slot_gen(L_digit, U_digit, slots_n):
    u_limits = []
    steps = []
    i_steps = []
    slot = L_digit
    # slot = 0
    
    for x in reversed(range(L_digit+1,slots_n)):
        slot += int(math.pow(10, x))
    # slot-=
    u_slot = U_digit*slot
    print(u_slot)
    print(slot)
    x = slot
    count = 1
    tens = 0
    runs = 0
    pow1 = 1
    
    # for x in range(0,slots_n):
    # print(x)
    dig = 0
    dig1 = 0
    # dig = math.pow(10,1)
    # z = 0
    counters = range(1, 5)
    for n in counters:
        z = str("1"*n)
        print(int(z))
        dig = int(z)*10
        if z != 1:
            dig1 = int(math.pow(10,1))
        print(dig)
        for x in range(0,U_digit-1):
            # dig1 = math.pow(10,x)*10
            # print(dig1)
            dig1 += dig
            print(dig1)
            # for i in range(slot,slot+U_digit-1):
            #     # for j in range(i,slot+U_digit):
            #     #     print(j+dig1)
            #     dig1 += dig
            #     print(dig1)
            # if dig1 >200:
            #     return True
            
                # return True
                # print(dig1)
                # print(i)
                # print(i+dig1)
                # dig1 += dig
                # print(dig)
        # for y in range(2,len(str(dig))):
        #     dig += math.pow(10,y)
        # print(dig)
        # for y in range(L_digit,U_digit+1):
        #     print(dig*10)
        # for i in range(slot,slot+U_digit):
        #     print(i+dig*10)

    # for i in range(slot,u_slot,10):
    #     
    #     pre_ck=int(i/math.pow(10,1))
    #     pre_ck_mod = int(pre_ck%math.pow(10,1))
    #     print("pre_ck: %d" % pre_ck)
    #     
    #     print("pre_ck_mod: %d" % pre_ck_mod)
    #     if(pre_ck_mod in [0,7,8,9]):
    #         print("true")
    #         continue
    #     print("running: %d" % runs)
    #     print("power: %d" % pow1)
    #     print("tens: %d" % tens)
    #     print(math.pow(U_digit,pow1+1)/(tens+1))
    #     if(runs==(math.pow(U_digit,pow1+1)/(tens+1))):
    #         pre_ck1=int(i/math.pow(10,tens+2))
    #         pre_ck1_mod = int(pre_ck1%math.pow(10,tens+1))
    #         print("pre_ck for pow: %d" % pre_ck1)
    #         print("pre_ck_mod for pow: %d" % pre_ck1_mod)
    #         
    #         if i==2211:
    #             print(pre_ck1%math.pow(10,tens))
    #             return(i)
    #         
    #         if (pre_ck1_mod in [1]):
    #             print(pre_ck1_mod)
    #             print("lll")
    #         #     # return(i)
    #             pow1+=1
    #             tens+=1
    #             print(tens)
    #             print(math.pow(10,tens+1))
    #             print(pow1)
    #         else:
    #             print("gotit")
    #             print(i)
    #             continue
    #     list_A = list(range(i,i+U_digit))
    #     u_limits.extend(list_A)
    #     print(list_A)
    #     runs+=1
    #     input()
        
    # a = list(range(slot,slot+(U_digit)))
    # u_limits.extend(a)
    # print(a)
    # tens = []
    # for t in range(1,slots_n):
    #     tens.append(int(math.pow(10,t)))
    #     
    # for t in tens:
    #     for a in range(t,t+6,1):
    #         # print(a)
    #         steps.append(a)
    #         for i in range(0,len(tens)):
    #             if len(str(a*tens[i])) <=6:
    #                 # print(a*tens[i])
    #                 steps.append(a*tens[i])
    # steps.sort()
    # # print(steps)
    # for l in steps:
    #     n_l = int(slot+l)
    #     if(len(str(n_l))>4):
    #         n_l = int(n_l%math.pow(10,4))
    #     a = list(range(n_l,n_l+U_digit))
    #     # print(a)
    #     u_limits.extend(a)
    # def remove_duplicates(l):
    #     return list(set(l))
    # u_limits = remove_duplicates(u_limits)
    # 
    # u_limits.sort()
    return u_limits
    
#First pick
min_digit= slot_gen(slots_min, slots_max, slots_n)
print(min_digit)
