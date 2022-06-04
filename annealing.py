import random as rd
import time
import multiprocessing as mp
from multiprocessing import Process

import library_bulder as lb
lib = lb.library_bulder(4)

test_dict = {"0": 0,
                     "1": 1,
                     "2": 2,
                     "3": 3,
                     "4": [0, 1, 2],
                     "5": [0, 1, 3],
                     "6": [0, 2, 3],
                     "7": [1, 0, 2],
                     "8": [1, 0, 3],
                     "9": [1, 2, 3],
                     "10": [2, 1, 0],
                     "11": [2, 0, 3],
                     "12": [2, 1, 3],
                     "13": [3, 1, 2],
                     "14": [3, 1, 0],
                     "15": [3, 2, 0]
                     }


def placer_and_calculator(diff_element):
    lib.clear()
    for i in range(0, len(diff_element)):
        if 0 <= diff_element[i] <= 3:
            lib.place_Not(test_dict[str(diff_element[i])])
        else:
            lib.place_Toffoli(test_dict[str(diff_element[i])])

    arrr = [i for i in range(0, 16)]

    for j in arrr: arrr[j] = lib.calculate(j)
    return arrr

def checker(one_atom):
    if one_atom[1]==target:
        print("AAAAAAAAAAAA")
        lol_list.append(one_atom)
        return True
    else: return False
def atom_movement(popul):
    new_move=[]
    for i in range(0, len(popul)):
        new_move=popul[i].copy()
        if checker(popul[i]): continue
        chance = rd.random()
        movement_chance = rd.random() * temperature
        if movement_chance>=0.25:
            if 0<chance<0.25:
                if len(popul[i][0]) == 0: continue
                #TODO left
                pos=rd.randint(0, len(popul[i][0]) - 1)
                new_move[0][pos]=(rd.randint(0, popul[i][0][pos]))
            elif 0.25<=chance<0.5:

                new_move[0].append(rd.randint(0, 15))
                #TODO up
            elif 0.5<=chance<0.75:
                if len(popul[i][0])==0: continue
                pos = rd.randint(0, len(popul[i][0]) - 1)
                new_move[0][pos] = \
                    (rd.randint(popul[i][0][pos], 15))
                #TODO right
            elif 0.75<=chance<1:
                if len(popul[i][0]) == 0: continue
                new_move[0].pop()
                #TODO down
        new_move[2]=entropy_check(new_move[1],target)
        #print(new_move[2], popul[i][2])
        if new_move[2]<popul[i][2]:
            print(new_move,popul[i])
            popul[i]=new_move


def entropy_check(pop_one,function):
    distance=0
    for pos in range(0,len(function)):
        if function[pos]==pop_one[pos]:
            continue
        else: distance+=1
    return distance# TODO STUPID DOG


def entropy_position_first(pop,function,list_lol):
    distance=0
    for i in range(0,len(pop)):

        distance=0
        for pos in range(0,len(function)):
             if function[pos]==pop[i][1][pos]:
                continue
             else: distance+=1
        pop[i].append(distance)# TODO STUPID DOG
        if distance==0:list_lol.append(pop[i])

def entropy_position_second(pop,function,list_lol):
    distance=0
    for i in range(0,len(pop)):

        distance=0
        for pos in range(0,len(function)):
             if function[pos]==pop[i][1][pos]:
                continue
             else: distance+=1
        pop[i][2]=distance# TODO STUPID DOG
        if distance==0:list_lol.append(pop[i])


def lattice_create(pop):
    for z in range(0, pop_size):
        pop.append(random_gates())

def random_gates():
    number_of_gates=rd.randint(0, 32)
    gates = []
    total=[]
    for i in range(0, number_of_gates):
        gates.append(rd.randint(0, 15))
    total.append(gates)
    total.append(placer_and_calculator(gates))
    return total


atoms=[]
lol_list=[]
global pop_size
global temperature
temperature=500
pop_size=3000
locked_postions=[]
target=[1, 0, 3, 4, 5, 2, 7, 6, 9, 8, 11, 12, 13, 15, 14, 10]
start=time.time()
lattice_create(atoms)
print(time.time()-start)
entropy_position_first(atoms,target,locked_postions)


while(temperature>5):
    entropy_position_second(atoms,target,locked_postions)
    atom_movement(atoms)
    temperature-=1
    #print(time.time() - start,temperature)
print(lol_list)