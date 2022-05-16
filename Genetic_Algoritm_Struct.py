import random as rd
import time
import multiprocessing as mp
from multiprocessing import Process

import library_bulder as lb



lib = lb.library_bulder(3)


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



def parralel_placer(pop_part,L):
    for i in range(0,len(pop_part)):
        L.append([pop_part[i][0],placer_and_calculator(pop_part[i][0])])
    print("a")



def sorting_madnesss(pop):
    for i in range(0,len(pop)):
        level_pop=pop[i]
        level_pop.sort(key=lambda inner_list: inner_list[2])
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
    #total.append(placer_and_calculator(gates))
    return total

def reproduction(pop):
    new_pop=[[] for i in range(0,len(pop))]
    new_pop[0]=pop[0]
    for i in range(1,len(pop)):
        for z in range(0,i*100):
            new_pop[i].append(take_genes())
        for z in range(0,i*100):
            new_pop[i].append(random_gates(i))


    def mutation(pop):
        for i in range(0,len(pop)):
            for z in range(0,len(pop[i])):
                if rd.random()>0.6:
                    mut=rd.randint(1,2)
                    if mut==1 or len(pop[i][z][0])==1:
                        pop[0][0][0][rd.randint(1,len(pop[0][0][0]))]=rd.randint(1,6)
                    else:
                        pop[0][0][0][rd.randint(1, len(pop[0][0][0]))] = rd.randint(1, 6)
                        pop[0][0][0][rd.randint(1, len(pop[0][0][0]))] = rd.randint(1, 6)
                else: continue





def take_genes(sub1,sub2):
    child=[]
    size=rd.randint(1,len(sub2)-1)
    if rd.randint(1,2)==1:
        for i in range(0, size):
            child.append(sub1[i])
        for z in range(i, len(sub2) - 1):
            child.append(sub2[z])
    else:
        for i in range(0, size):
            child.append(sub2[i])
        for z in range(i, len(sub2) - 1):
            child.append(sub1[z])
    return child







if __name__ == '__main__':

    procs = []
    manager = mp.Manager()
    L = manager.list()


    pop = []
    start = time.time()

    generate(pop)


    for i in range(0,len(pop)):
        proc = Process(target=parralel_placer, args=(pop[i], L))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    pop.clear()
    for i in range(0,12): pop.append([])
    for i in range(0,len(L)):
        pop[len(L[i][0])-1].append(L[i])

    end = time.time()
    print(end - start)
    #x = 1 / 0
    fitness(pop, [0, 1, 2, 5, 4, 7, 6, 3])
    #
    sorting_madnesss(pop)

    end = time.time()
    print(end - start)
    #print(pop)



