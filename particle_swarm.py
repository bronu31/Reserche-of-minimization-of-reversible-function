import random as rd
import time

import library_bulder as lb



start=time.time()
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






def distance_from_target(head,list_lol):
    distance=0
    for pos in range(0, len(target)):

        if target[pos] == pop[i][z][1][pos]:
            continue
        else:
            distance += 1



class Particle_swarm:
    def __init__(self, count):
        self.swarm=[]
        for i in range(count):
            self.swarm.append(Particle_class(*random_creator()))
            self.swarm[-1].particle_head=placer_and_calculator(self.swarm[-1].particle_body)
            self.swarm[-1].particle_postition=distance_from_target(self.swarm[-1].particle_head)

    def __len__(self):
        return len(self.swarm)

    def __getitem__(self, i):
        return self.swarm[i]

def random_creator():
    gates = []
    total = []
    for i in range(rd.randint(7,32)):
        gates.append(rd.randint(0, 15))
    total.append(gates)
    return total

class Particle_class:
    def __init__(self,body):
        self.particle_body=body # набор вентилей
        self.particle_head=[] # вычисленный вектор истинности
        self.particle_postition=-1 #Как далеко от ответа
        self.global_minimum=[]
        self.particle_found_minimum=[]
    def new_minimum(self):
        print("a")
    def __str__(self):
        return "[ body={}, head={}, position={}, global_min={}, life_min={} ]".format(self.particle_body,
                                                      self.particle_head,
                                                      self.particle_postition,
                                                      self.global_minimum,
                                                      self.particle_found_minimum)







def big_bang(particles_count):
    new_begining=[]
    for matter in particles_count:
        new_begining.append([])





particles_count=15000
global target
target=[8, 0, 14, 11, 13, 3, 2, 10, 15, 1, 7, 5, 4, 9, 6, 12]
particle_swarm=Particle_swarm(particles_count)
for x in range(0,len(particle_swarm)):
    print(str(particle_swarm[x]))
#print(particle_swarm)
print(time.time()-start)
