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


def atom_movement(pop):
    chance=rd.random()
    for i in range(0,len(pop)):
        if 0<chance<0.25:

            #TODO left
            print("AAAAAAAAAA")
        elif 0.25<=chance<0.5:
            print("AAAAAAAAAAA")
            pop[i][0].append(rd.randint(0, 15))
            #TODO up
        elif 0.5<=chance<0.75:
            print("AAAAAAAAAA")
            #TODO right
        elif 0.75<=chance<1:
            pop[i][0].pop[-1]
            #TODO down


def entropy_position(pop,function,list_lol):
    distance=0
    for i in range(0,len(pop)):

        distance=0
        for pos in range(0,len(function)):
             if function[pos]==pop[i][1][pos]:
                continue
             else: distance+=1
        pop[i].append(distance)
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
global pop_size
pop_size=4000
locked_postions=[]
target=[0, 1, 2, 10, 4, 12, 6, 15, 8, 14, 11, 5, 9, 7, 3, 13]
lattice_create(atoms)

entropy_position(atoms,target,locked_postions)
print(atoms)
x=1/0

for i in range(0,1000):
    entropy_position(atoms,target,locked_postions)
    atom_movement(atoms)