import random as rd
import time

import library_bulder as lb
def placer_and_calculator(diff_element):
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


def sorting_madnesss(pop):
    for i in range(0,len(pop)):
        level_pop=pop[i]
        level_pop.sort(key=lambda inner_list: inner_list[2])
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(level_pop)
        pop[i]=level_pop


def fitness(pop,function):
    distance=0
    for i in range(0,len(pop)):
        for z in range(0,len(pop[i])):
            distance=0
            for pos in range(0,len(function)):

                if function[pos]==pop[i][z][1][pos]:# А ФУНКЦИЯ ТО НЕ ПОСЧИТАНА
                    continue
                else: distance+=1
            pop[i][z].append(distance)
     #спомощью расстояния Хэмминга проверим насколько подходит та или иная особь





def generate(pop):
    for i in range(1, 13):
        pop.append([])
        for z in range(0, i * 200):
            pop[-1].append(random_gates(i))# TODO создать метод рандомной генерации набора гейтов


def random_gates(number_of_gates):
    gates = []
    total=[]
    for i in range(0, number_of_gates):
        gates.append(rd.randint(1, 6))
    total.append(gates)
    total.append(placer_and_calculator(gates))
    return total


pop=[]
start = time.time()
lib=lb.library_bulder(3)
generate(pop)
print(len(pop))


fitness(pop,[0, 1, 2, 5, 4, 7, 6, 3])
#print(pop)
sorting_madnesss(pop)

end = time.time()
print(end - start)
