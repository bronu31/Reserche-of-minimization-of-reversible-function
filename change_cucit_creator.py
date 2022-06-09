import random as rd
import time

import pandas as pd



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












x1=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]]
f2=pd.read_csv("DO NOT DELETE.txt",header=None,sep=' ',nrows=192)
x2=f2.values[:,-2:]
f3=pd.read_csv("DO NOT DELETE.txt",header=None,sep=' ',skiprows=192,nrows=2192-192)
x3=f3.values[:,-3:]
f4=pd.read_csv("DO NOT DELETE.txt",header=None,sep=' ',skiprows=2192,nrows=21634-2192-1)
x4=f4.values[:,-4:]
f5=pd.read_csv("DO NOT DELETE.txt",header=None,sep=' ',skiprows=21633,nrows=202350-21634)
x5=f5.values[:,-5:]
f6=pd.read_csv("DO NOT DELETE.txt",header=None,sep=' ',skiprows=202349)
x6=f6.values[:,-6:]
dict_of_sizes={1:x1,
               2:x2,
               3:x3,
               4:x4,
               5:x5,
               6:x6
               }

pattern_for_3=[[0,1,0],[0,2,0],[0,3,0],
               [1,0,1],[1,2,1],[1,3,1],
               [2,0,2],[2,1,2],[2,3,2],
               [3,0,3],[3,1,3],[3,2,3],

               [0,9,0],[0,12,0],[0,13,0],
               [1,6,1],[1,11,1],[1,15,1],
               [2,5,2],[2,8,2],[2,14,2],
               [3,4,3],[3,7,3],[3,10,3],

               [9,0,9],[12,0,12],[13,0,13],
               [6,1,6],[11,1,11],[15,1,15],
               [5,2,5],[8,2,8],[14,2,14],
               [4,3,4],[7,3,7],[10,3,10],

               [13, 4, 13], [12, 5, 12], [9, 6, 9],
               [15, 7, 15], [11, 8, 11], [6, 9, 6],
               [14, 10, 14], [8, 11, 8], [5, 12, 5],
               [4, 13, 4], [7, 14, 7], [7, 15, 7],

               [15,13,15],[14,13,14],[13,14,13],
               [15,14,15],[13,15,13],[14,15,14],

                [11,10,11],[12,10,12],[10,11,10],
               [12,11,12],[10,12,10],[11,12,11],

                [8,7,8],[9,7,9],[7,8,7],
               [9,8,9],[7,9,7],[8,9,8],

                [5,4,5],[6,4,6],[4,5,4],
               [6,5,6],[4,6,4],[5,6,5]

               ]

def placer_and_calculator(diff_element):
    lib.clear()
    #print(diff_element)
    for i in range(0, len(diff_element)):

        if 0 <= diff_element[i] <= 3:
            lib.place_Not(test_dict[str(diff_element[i])])
        else:
            lib.place_Toffoli(test_dict[str(diff_element[i])])

    arrr = [i for i in range(0, 16)]

    for j in arrr: arrr[j] = lib.calculate(j)
    return arrr


def seek_and_destroy(garfield):
    for i in range(0, 16):
        z = 0
        if len(garfield) == 1: break
        while (z != len(garfield) - 1):
            if len(garfield) == 1 or len(garfield) == 0:break
            if garfield[z] == garfield[z + 1]:
                del garfield[z:z + 2]
                z = 0
            z += 1
    for i in range(0, len(pattern_for_3)):
        if len(garfield) == 1 or len(garfield) == 2 or len(garfield) == 0: break
        z = 1
        while (z != len(garfield) - 1):
            if len(garfield) == 1 or len(garfield) == 2: break
            if [garfield[z - 1], garfield[z], garfield[z + 1]] == pattern_for_3[i]:
                del garfield[z + 1]
                del garfield[z - 1]
                z = 1
            z += 1
    return garfield



def change_maker(size):
    begin=1
    end=6
    part=size
    list_of_sizes=[]
    while(part>0):
        if part<6: end=part
        gen=rd.randint(begin,end)
        list_of_sizes.append(gen)
        part-=gen
    return list_of_sizes

def something_something(list_of_sizes):
    end_result=[]
    torture=[]
    rd_pos=0
    for sizes in range(0,len(list_of_sizes)):
        rd_pos=rd.randint(0,len(dict_of_sizes[list_of_sizes[sizes]])-1)
        torture=dict_of_sizes[list_of_sizes[sizes]][rd_pos]
        list_of_sizes[sizes]=str(list_of_sizes[sizes])+str(rd_pos)
        if len(torture)==1:end_result.append(torture[0])
        else:
            for suffering in torture:  end_result.append(int(str(suffering.strip("[,]"))))
    return [list_of_sizes,end_result]

def recreate(fnf):
    party=[fnf[0],fnf[1],placer_and_calculator(seek_and_destroy(fnf[1]))]
    return party




start=time.time()
life=[1, 0, 7, 2, 5, 4, 3, 6, 9, 8, 15, 10, 13, 12, 11, 14]
#[15, 6, 9, 0, 3, 2, 1, 4, 7, 14, 12, 5, 11, 10, 8, 13]
print(time.time()-start)
reclaimer=change_maker(18)
print(reclaimer)
all_shapes_and_sizes=[]

f=open("scream.txt","w")
breaking=False

for i in range(0, 32 - 6):
    all_shapes_and_sizes.append([])
    for z in range(0, 100):
        reclaimer = change_maker(i+7)
        all_shapes_and_sizes[-1].append(
            something_something(reclaimer))

for x in range(0, len(all_shapes_and_sizes)):
    for z in range(0, len(all_shapes_and_sizes[x])):
        all_shapes_and_sizes[x][z] = recreate(all_shapes_and_sizes[x][z])


for x in all_shapes_and_sizes:
    for z in x:
        f.write(str(z) + "\n")

for theta in all_shapes_and_sizes:
    for darkside in theta:
        if darkside[1] == life:
            print(darkside, "aaaaaaaa")
            breaking = True



def something_something_with_pos(list_of_sizes):
    end_result=[]
    torture=[]
    rd_pos=0
    for sizes in range(0,len(list_of_sizes[0])):
        if len(dict_of_sizes[int(list_of_sizes[0][sizes][0])])-1==int(list_of_sizes[0][sizes][1:]):
            if int(list_of_sizes[0][sizes][0])!=6:
                list_of_sizes[0][sizes]=str(int(list_of_sizes[0][sizes][0])+1)+str(0)
            else: list_of_sizes[0][sizes]=str(60)
        else:list_of_sizes[0][sizes]=str(int(list_of_sizes[0][sizes][0]))+str(int(list_of_sizes[0][sizes][1:])+1)
        torture=dict_of_sizes[int(list_of_sizes[0][sizes][0])][int(list_of_sizes[0][sizes][1:])]
        if len(torture)==1:end_result.append(torture[0])
        else:
            for suffering in torture:  end_result.append(int(str(suffering.strip("[,]"))))
    return [list_of_sizes[0],end_result]
#todo система прибавляет к каждому элементу 1!!!





for zeta in range(0,25):

    for i in range(0,len(all_shapes_and_sizes)):
        for z in range(0,len(all_shapes_and_sizes[i])):
            #print(all_shapes_and_sizes[i][z])
            all_shapes_and_sizes[i][z]=something_something_with_pos(all_shapes_and_sizes[i][z])

    for x in range(0,len(all_shapes_and_sizes)):
        for z in range(0,len(all_shapes_and_sizes[x])):

            all_shapes_and_sizes[x][z]=recreate(all_shapes_and_sizes[x][z])


    for theta in all_shapes_and_sizes:
        for darkside in theta:
            if darkside[1]==life:
                print(darkside,"aaaaaaaa")
                breaking=True
                break
    if breaking: break
    for x in all_shapes_and_sizes:
        for z in x:
            f.write(str(z) + "\n")

    print(time.time() - start)



f.close()
print(something_something(reclaimer))
print(time.time()-start)