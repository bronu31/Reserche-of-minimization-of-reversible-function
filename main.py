import math
import sys
from itertools import groupby
import library_bulder as lb
import overkill_tactics as ot
import timeit
#0 - ничего
#1- отрицание на 0 линии
#2- отрицание на 1 линии
#3- отрицание на 2 линии
#4- тоффоли 0 1 2
#5- тоффоли 1 2 0
#6- тоффоли 2 0 1


#diff_list.append([])

def factorize(holder):
    arr2 = []
    cout = 0
    for i in range(0, len(holder) - 1):
        for z in range(i, len(holder)):
            if holder[i] > holder[z]:
                cout += 1
        arr2.append(cout)
        cout = 0
    for z in range(0, len(arr2)):
        cout += arr2[z] * math.factorial(len(arr2) - z)
    return cout

def placer_and_calculator(lib,diff_element):
    lib.clear()
    for i in range(0, len(diff_element)):

        if diff_element[i] == 0:
            continue
        elif diff_element[i] == 1:
            lib.place_Not(0)
        elif diff_element[i] == 2:
            lib.place_Not(1)
        elif diff_element[i] == 3:
            lib.place_Not(2)
        elif diff_element[i] == 4:
            lib.place_Toffoli([0, 1, 2])
        elif diff_element[i] == 5:
            lib.place_Toffoli([1, 2, 0])
        elif diff_element[i] == 6:
            lib.place_Toffoli([2, 0, 1])
    arrr = [i for i in range(0, 8)]

    for j in arrr: arrr[j] = lib.calculate(j)
    return arrr

diff_list=[[],[[1],[2],[3],[4],[5],[6]]]
lib=lb.library_bulder(3)
Holder_of_Min_NumberCombos=[0, 5167, 11536, 23616, 105, 5, 1]

start = timeit.default_timer()
for gamma in range(0,math.factorial(8)):
    diff_list.append([])
    fact = 0
    for ii in range(0, len(diff_list[-2])):
        for j in range(0, len(diff_list[1])):
            diff_list[-1].append([*diff_list[-2][ii], *diff_list[1][j]])
            fact = factorize(placer_and_calculator(lib, diff_list[-1][-1]))
            if fact in Holder_of_Min_NumberCombos:
                del diff_list[-1][-1]
            else:
                Holder_of_Min_NumberCombos.append(fact)
    if len(Holder_of_Min_NumberCombos)==math.factorial(8): break
    gamma=len(Holder_of_Min_NumberCombos)
    print(len(Holder_of_Min_NumberCombos))
    print('Time: ', timeit.default_timer() - start)

print(len(Holder_of_Min_NumberCombos))
Holder_of_Min_NumberCombos.sort()
print(Holder_of_Min_NumberCombos)

x=1/0

print(diff_list)
lib=lb.library_bulder(3)
arr=[]
holder=[]
for z in range(0,len(diff_list[2])):
    for i in range(0, len(diff_list[2][0])):

        if diff_list[2][z][i] == 0:
            continue
        elif diff_list[2][z][i] == 1:
            lib.place_Not(0)
        elif diff_list[2][z][i] == 2:
            lib.place_Not(1)
        elif diff_list[2][z][i]== 3:
            lib.place_Not(2)
        elif diff_list[2][z][i] == 4:
            lib.place_Toffoli([0, 1, 2])
        elif diff_list[2][z][i] == 5:
            lib.place_Toffoli([1, 2, 0])
        elif diff_list[2][z][i] == 6:
            lib.place_Toffoli([2, 0, 1])

    arrr = [i for i in range(0, 8)]

    for j in arrr: arrr[j] = lib.calculate(j)
    holder.append(arrr.copy())
    print(arrr,lib.gates[0], lib.gates[1])
    lib.clear()

print(holder)
numbersss=[]
for i in range(0,len(holder)):
    arr2 = []
    count = 0
    for z in range(0, len(holder[i]) - 1):
        for x in range(z, len(holder[z])):

            if (holder[i][z] > holder[i][x]):
                count += 1
        arr2.append(count)
        count = 0
    count = 0
    for z in range(0, len(arr2)):
        count += arr2[z] * math.factorial(len(arr2) - z)
    numbersss.append(count)
print(numbersss)
numbersss.sort()
new_x = [el for el, _ in groupby(numbersss)]

print(new_x)
print(len(new_x))
lib.clear()
lib.place_Toffoli([0,1,2])
arrr = [i for i in range(0, 8)]
for j in arrr: arrr[j] = lib.calculate(j)
holder.append(arrr.copy())
print(arrr, lib.gates[0])

