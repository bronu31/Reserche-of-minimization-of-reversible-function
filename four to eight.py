import math
import sys
from itertools import groupby
import library_bulder as lb
import overkill_tactics as ot
import timeit
import Genetic_Algoritm_Struct as GAS
#0 - ничего
#1- отрицание на 0 линии
#2- отрицание на 1 линии
#3- отрицание на 2 линии
#4- тоффоли 0 1 2
#5- тоффоли 1 2 0
#6- тоффоли 2 0 1


#diff_list.append([])

lib=lb.library_bulder(4)
test_dict = {"0": lib.place_Not(0),
                     "1": lib.place_Not(1),
                     "2": lib.place_Not(2),
                     "3": lib.place_Not(3),
                     "4": lib.place_Toffoli([0, 1, 2]),
                     "5": lib.place_Toffoli([0, 1, 3]),
                     "6": lib.place_Toffoli([0, 2, 3]),
                     "7": lib.place_Toffoli([1, 0, 2]),
                     "8": lib.place_Toffoli([1, 0, 3]),
                     "9": lib.place_Toffoli([1, 2, 3]),
                     "10": lib.place_Toffoli([2, 1, 0]),
                     "11": lib.place_Toffoli([2, 0, 3]),
                     "12": lib.place_Toffoli([2, 1, 3]),
                     "13": lib.place_Toffoli([3, 1, 2]),
                     "14": lib.place_Toffoli([3, 1, 0]),
                     "15": lib.place_Toffoli([3, 2, 0])
                     }




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
            lib.place_Not(0)
        elif diff_element[i] == 1:
            lib.place_Not(1)
        elif diff_element[i] == 2:
            lib.place_Not(2)
        elif diff_element[i] == 3:
            lib.place_Not(3)
        elif diff_element[i] == 4:
            lib.place_Toffoli([0, 1, 2])
        elif diff_element[i] == 5:
            lib.place_Toffoli([0, 1, 3])
        elif diff_element[i] == 6:
            lib.place_Toffoli([0, 2, 3])
        elif diff_element[i] == 7:
            lib.place_Toffoli([1, 0, 2])
        elif diff_element[i] == 8:
            lib.place_Toffoli([1, 0, 3])
        elif diff_element[i] == 9:
            lib.place_Toffoli([1, 2, 3])
        elif diff_element[i] == 10:
            lib.place_Toffoli([2, 1, 0])
        elif diff_element[i] == 11:
            lib.place_Toffoli([2, 0, 3])
        elif diff_element[i] == 12:
            lib.place_Toffoli([2, 1, 3])
        elif diff_element[i] == 13:
            lib.place_Toffoli([3, 1, 2])
        elif diff_element[i] == 14:
            lib.place_Toffoli([3, 1, 0])
        elif diff_element[i] == 15:
            lib.place_Toffoli([3, 2, 0])

    arrr = [i for i in range(0, 16)]

    for j in arrr: arrr[j] = lib.calculate(j)
    return arrr

diff_list=[[],[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]]]

Holder_of_Min_NumberCombos=[1313941673647,
2789792421136,
5606234750016,
11212821043200,
3237424,
29727661,
3876255609,
592,
3109,
1959914985,
16,
1565,
7620485,
362881,
7,
121,
0]

#Test=GAS.Genetic_Algorithm()

#print(Test)
#0- отрицание на 0 линии
#1- отрицание на 1 линии
#2- отрицание на 2 линии
#3- отрицание на 3 линии

#4- тоффоли 0 1 2
#5- тоффоли 0 1 3
#6 - тоффоли 0 2 3

#7- тоффоли 1 0 2
#8- тоффоли 1 0 3
#9 - тоффоли 1 2 3

#10- тоффоли 2 1 0
#11- тоффоли 2 0 3
#12 - тоффоли 2 1 3

#13- тоффоли 3 1 2
#14- тоффоли 3 1 0
#15 - тоффоли 3 2 0

f = open('all of 4.txt', 'w')

start = timeit.default_timer()
for gamma in range(0,126618076):
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
                f.write( str(placer_and_calculator(lib, diff_list[-1][-1]))+" "+ str(diff_list[-1][-1]) +"\n")
    if len(Holder_of_Min_NumberCombos)>=126618076: break
    gamma=len(Holder_of_Min_NumberCombos)
    print(len(Holder_of_Min_NumberCombos))
    print('Time: ', timeit.default_timer() - start)

print(len(Holder_of_Min_NumberCombos))
Holder_of_Min_NumberCombos.sort()
print(Holder_of_Min_NumberCombos)
f.close()

x=1/0
