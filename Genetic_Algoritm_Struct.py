import random as rd
import time
import multiprocessing as mp
from multiprocessing import Process

import library_bulder as lb



lib = lb.library_bulder(4)


def placer_and_calculator(diff_element):
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



def parralel_placer(pop_part,L):
    for i in range(0,len(pop_part)):
        L.append([pop_part[i][0],placer_and_calculator(pop_part[i][0])])



def sorting_madnesss(pop):
    for i in range(0,len(pop)):
        level_pop=pop[i]
        level_pop.sort(key=lambda inner_list: inner_list[2])
        pop[i]=level_pop


def fitness(pop,function,list_lol):
    distance=0
    for i in range(0,len(pop)):
        for z in range(0,len(pop[i])):
            distance=0
            for pos in range(0,len(function)):

                if function[pos]==pop[i][z][1][pos]:
                    continue
                else: distance+=1
            pop[i][z].append(distance)
            if distance==0:list_lol.append(pop[i][z])





def generate(pop):
    for i in range(1, 33):
        pop.append([])
        for z in range(0, pop_size):
            pop[-1].append(random_gates(i))


def random_gates(number_of_gates):
    gates = []
    total=[]
    for i in range(0, number_of_gates):
        gates.append(rd.randint(0, 15))
    total.append(gates)
    #total.append(placer_and_calculator(gates))
    return total

def reproduction(pop):
    new_pop=[[] for i in range(0,len(pop))]
    new_pop[0]=pop[0]
    for i in range(1,len(pop)):
        for z in range(0,100):
            new_pop[i].append([take_genes(pop[i][0][0],pop[i][rd.randint(1,len(pop[i])-1)][0])])
        for z in range(0,pop_size-100):
            new_pop[i].append(random_gates(len(pop[i][0][0])))
    new_pop=mutation(new_pop)
    return new_pop


def mutation(pop):
    for i in range(0,len(pop)):
        for z in range(0,len(pop[i])):
            if rd.random()>mutation_chance:
                mut=rd.randint(1,2)
                if mut==1 or len(pop[i][z][0])==1:
                    pop[i][z][0][rd.randint(0,len(pop[i][z][0])-1)]=rd.randint(1,6)
                else:
                    pop[i][z][0][rd.randint(0, len(pop[i][z][0])-1)] = rd.randint(1, 6)
                    pop[i][z][0][rd.randint(0, len(pop[i][z][0])-1)] = rd.randint(1, 6)
            else: continue
    return pop





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

    global pop_size
    pop_size=400
    global target
    target=[3, 2, 1, 13, 15, 9, 5, 6, 7, 10, 8, 0, 11, 12, 4, 14]
    global cycles
    global mutation_chance
    mutation_chance=0.8
    cycles=250
    procs = []
    manager = mp.Manager()
    L = manager.list()


    pop = []
    start = time.time()

    generate(pop)

    Pool_List=manager.list()
    for i in range(0,len(pop)):
        proc = Process(target=parralel_placer, args=(pop[i][:int(len(pop[i]) / 2)], L))
        procs.append(proc)
        proc.start()
        proc = Process(target=parralel_placer, args=(pop[i][int(len(pop[i]) / 2):], L))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    pop.clear()
    for i in range(0,32): pop.append([])
    for i in range(0,len(L)):
        pop[len(L[i][0])-1].append(L[i])

    end = time.time()
    print(end - start)
    list_lol = []
    #x = 1 / 0
    fitness(pop, target,list_lol)
    #


    for i in range(0,cycles):
        L[:] = []
        sorting_madnesss(pop)
        pop=reproduction(pop)
        procs.clear()

        for i in range(0, len(pop)):
            proc = Process(target=parralel_placer, args=(pop[i][:int(len(pop[i])/2)], L))
            procs.append(proc)
            proc.start()
            proc = Process(target=parralel_placer, args=(pop[i][int(len(pop[i])/2):], L))
            procs.append(proc)
            proc.start()

        for proc in procs:
            proc.join()

        pop.clear()
        for i in range(0, 32): pop.append([])
        for i in range(0, len(L)):
            pop[len(L[i][0]) - 1].append(L[i])




        fitness(pop, target,list_lol)
        print(time.time() - start)

    sorting_madnesss(pop)
    end = time.time()
    print(end - start)
    #print(pop)
    print(end - start)
    f = open('text.txt', 'w')
    for i in range(0,len(pop)):
        for z in range(0,len(pop[i])):
            f.write(str(pop[i][z]) + ", \n")
        f.write("\n")
    f.close()
    print(list_lol)
    file=open("answer.txt","w")
    for i in range(0,len(list_lol)):
        file.write(str(list_lol[i])+"\n")
    file.close()



