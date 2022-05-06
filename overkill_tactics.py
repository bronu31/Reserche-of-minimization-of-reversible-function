import math
import time

import Not_Gate
import library_bulder as lb

def ckeckList(lst):
    chk = True
    for item in lst:
        if 6 != item:
            chk = False
            break
    return chk

def overkill_func(lains,circuit_size):
    if circuit_size==0: return []
    holder=[]
    circuit=[0]*circuit_size
    circuit[0]=1
    start_time = time.time()
    while(not ckeckList(circuit)):

        if(circuit[0]==6):
            for j in range(0, len(circuit)):
                if circuit[j] == 6:
                    circuit[j] = 0
                    continue
                else:
                    circuit[j] += 1
                    break
        else:
            circuit[0]+=1
    print("--- %s seconds ---" % (time.time() - start_time))
    #TODO с ПОМОЩЬЮ TRUE FALSE ПОПЫТАТЬСЯ ОБЕСПЕЧИТЬ ПОЛНЫЙ ПЕРЕБОР

# ЕСЛИ TRUE ТО НАЧАТЬ С NOT ИНАЧЕ ТОФФОЛИ
#СОЗДАТЬ ЛИСТ РАЗМЕРНОСТ СЛОЖНОСТИ