import random as rd
import time
import multiprocessing as mp
from multiprocessing import Process

import library_bulder as lb

def atom_movement():
    chance=rd.random()
    if 0<chance<0.25:
        #TODO left
        print("AAAAAAAAAA")
    elif 0.25<=chance<0.5:
        print("AAAAAAAAAAA")
        #TODO up
    elif 0.5<=chance<0.75:
        print("AAAAAAAAAA")
        #TODO right
    elif 0.75<=chance<1:
        print("AAAAAAAAAA")
        #TODO down


#TODO create lattice
def lattice_create():
    print("AAAAAAAA")





atoms=[]
