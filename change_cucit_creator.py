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
    for sizes in list_of_sizes:
        torture=dict_of_sizes[sizes][rd.randint(0,len(dict_of_sizes[sizes])-1)]
        if len(torture)==1:end_result.append(torture[0])
        else:
            for suffering in torture:  end_result.append(int(str(suffering.strip("[,]"))))
    return end_result

def recreate(fnf):
    return [fnf,placer_and_calculator(fnf)]




start=time.time()
life=[8, 0, 14, 11, 13, 3, 2, 10, 15, 1, 7, 5, 4, 9, 6, 12]
print(time.time()-start)
reclaimer=change_maker(18)
print(reclaimer)
all_shapes_and_sizes=[]

f=open("scream.txt","w")
while(True):
    for i in range(0,32-6):
        all_shapes_and_sizes.append([])
        for z in range(0,100):
            reclaimer=change_maker(i+7)
            all_shapes_and_sizes[-1].append(
                something_something(reclaimer))



    for x in range(0,len(all_shapes_and_sizes)):
        for z in range(0,len(all_shapes_and_sizes[x])):
            all_shapes_and_sizes[x][z]=recreate(all_shapes_and_sizes[x][z])

    for theta in all_shapes_and_sizes:
        for darkside in theta:
            if darkside[1]==life:
                break
    for x in all_shapes_and_sizes:
        for z in x:
            f.write(str(z) + "\n")
    all_shapes_and_sizes.clear()



f.close()
print(something_something(reclaimer))
print(time.time()-start)