import random as rd
import time

import library_bulder as lb



speed=10

start=time.time()
lib = lb.library_bulder(4)



wrong_pattern=[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],
               [12,12],[13,13],[14,14],[15,15]]

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

from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def add_remove(body_list,number,oper):
    if oper==1:# минус
        while(number!=0):
            number-=1
            if body_list[-1]-1==-1:
                for i in range(1,len(body_list)+1):
                    if body_list[-i]==0:
                        body_list[-i]=15
                    else:
                        body_list[-i]-=1
                        break
            else: body_list[-1]-=1
    elif oper==2:
        while(number!=0):
            number-=1
            if body_list[-1]+1==16:
                for i in range(1,len(body_list)+1):
                    if body_list[-i]==15:
                        body_list[-i]=0
                    else:
                        body_list[-i]+=1
                        break
            else: body_list[-1]+=1
    if all_equal(body_list)==True:
        return random_creator_sized(len(body_list))
    return body_list




def speed_function(one_particle):
    global speed
    P=1
    look_alike=0
    copy_cat=[]
    for i in one_particle.particle_found_minimum:
        if copy_cat==[]:
            copy_cat=i
            continue
        else:
            if (len(copy_cat[0])==len(i[0])) and copy_cat[1]==i[1]:
                look_alike+=1
                copy_cat=i
            else:
                copy_cat = i
                look_alike -=1
    look_alike=float(look_alike/10)
    if look_alike>=0.4 and len(one_particle.particle_found_minimum)>3:
        P=10
    Total_speed=int(speed*0.8*P*float(one_particle.particle_postition/7))
    direction=0
    if len(one_particle.particle_body)>len(one_particle.global_minimum[0]): direction=4
    elif len(one_particle.particle_body)<len(one_particle.global_minimum[0]): direction=1
    elif len(one_particle.particle_body)==len(one_particle.global_minimum[0]):
        for i in range(0,len(one_particle.particle_body)):
            if one_particle.particle_body[i]==one_particle.global_minimum[0][i]:
                continue
        else:
            if one_particle.particle_body[i]>one_particle.global_minimum[0][i]:
                direction=2
            elif one_particle.particle_body[i] < one_particle.global_minimum[0][i]:
                    direction = 3

    #direction=rd.randint(1,4)
    if direction==1: #вверх
        one_particle.add_body_layer()
    elif direction==2:
        one_particle.particle_body=add_remove(one_particle.particle_body,Total_speed,1)
    elif direction==3:
        one_particle.particle_body=add_remove(one_particle.particle_body,Total_speed,2)
    elif direction==4:
        one_particle.particle_body.pop()

    if direction==0:
        one_particle.particle_body=[*random_creator_sized(len(one_particle.particle_body))]

    #speed-=0.2



def distance_from_target(pop):
    distance=0
    for pos in range(0, len(target)):

        if target[pos] == pop[pos]:
            continue
        else:
            distance += 1
    return distance


def the_hunt(entire_swarm):
    min_min=18
    min_pos=-1
    for i in range(0,len(entire_swarm)):
        if min_min>entire_swarm[i].particle_postition:
            min_min=entire_swarm[i].particle_postition
            min_pos=i
    for z in range(0,len(entire_swarm)):entire_swarm[z].global_minimum=[entire_swarm[min_pos].particle_body,entire_swarm[min_pos].particle_postition]
class Particle_swarm:
    def __init__(self, count):
        self.swarm=[]
        for i in range(count):
            self.swarm.append(Particle_class(*random_creator()))
            self.swarm[-1].particle_head=placer_and_calculator(self.swarm[-1].particle_body)
            self.swarm[-1].particle_postition=distance_from_target(self.swarm[-1].particle_head)
            self.swarm[-1].particle_found_minimum.append([self.swarm[-1].particle_body.copy(),self.swarm[-1].particle_postition])
        the_hunt(self.swarm)


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

def random_creator_sized(sizze):
    gates = []
    total = []
    for i in range(0,sizze):
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
    def add_body_layer(self):
        self.particle_body.append(rd.randint(0,15))
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





particles_count=50000
global target
cycles=5000
list_lol=[]
blogalus_minimus=[]
target=[3, 2, 1, 13, 15, 9, 5, 6, 7, 10, 8, 0, 11, 12, 4, 14]
print("begin:" , time.time() - start)
particle_swarm=Particle_swarm(particles_count)
print("created:" , time.time() - start)
#for x in range(0,len(particle_swarm)):
#    print(str(particle_swarm[x]))
for z in range(0,cycles):
    for p in range(0,len(particle_swarm)):
        #print(str(particle_swarm[p]))
        speed_function(particle_swarm[p])
        #print(str(particle_swarm[p]))
        if particle_swarm[p].particle_head==target: list_lol.append(particle_swarm[p])
    blogalus_minimus.append(particle_swarm[0].global_minimum[0])
print(time.time() - start)
print(list_lol)
for i in range(0,len(list_lol)):
    print("AAAAAAAAAAA")
    print(str(list_lol[i]))
for i in range(0,len(blogalus_minimus)):
    print("AAAAAAAAAAA")
    print(str(blogalus_minimus[i]))
