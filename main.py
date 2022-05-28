import math

import library_bulder as lb
import timeit

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

print("AAAAAAAAAAAA")


f = open('all of 3.txt', 'w')

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
                f.write( str(placer_and_calculator(lib, diff_list[-1][-1]))+" "+ str(diff_list[-1][-1]) +"\n")
    if len(Holder_of_Min_NumberCombos)==math.factorial(8): break
    gamma=len(Holder_of_Min_NumberCombos)
    print(len(Holder_of_Min_NumberCombos))
    print('Time: ', timeit.default_timer() - start)

print(len(Holder_of_Min_NumberCombos))
Holder_of_Min_NumberCombos.sort()
print(Holder_of_Min_NumberCombos)
f.close()


