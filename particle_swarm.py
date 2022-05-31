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
    Total_speed=int(10*0.8*P*(one_particle.particle_postition/10))
    print(Total_speed,str(one_particle))#TODO РАСПРЕДЕЛЕНИЕ ПО НАПРАВЛЕНИЯМ
    direction=rd.randint(1,4)
    if direction==1: #вверх
        one_particle.add_body_layer()
    elif direction==2:
        if one_particle.particle_body[-1]<Total_speed:
            if one_particle.particle_body[-2]==0:
                one_particle.particle_body[-3]=rd.randint(0,one_particle.particle_body[-3])
                one_particle.particle_body[-2]=15
            else:
                one_particle.particle_body[-2]-=1
                one_particle.particle_body[-1]+=15-Total_speed
        else:one_particle.particle_body[-1]-=Total_speed

    elif direction==3:
        print("a")
    elif direction==4:one_particle.particle_body.pop()


    #что-то что-то* speed
    # здесь должна быть скорость перехода между точками и тд и тп
    speed-=0.2



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
            self.swarm[-1].particle_found_minimum.append([self.swarm[-1].particle_body,self.swarm[-1].particle_postition])
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





particles_count=250
global target
target=[3, 2, 1, 13, 15, 9, 5, 6, 7, 10, 8, 0, 11, 12, 4, 14]
particle_swarm=Particle_swarm(particles_count)
#for x in range(0,len(particle_swarm)):
#    print(str(particle_swarm[x]))
print(particle_swarm[0])
print("AAAAAAAAAAAAAAAAAAA")
for i in range(0,len(particle_swarm)):
    speed_function(particle_swarm[i])
print(time.time()-start)
