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
#6

[[3, 3, 1], [5, 12, 13, 7, 3, 4, 0], [9, 8, 11, 10, 13, 3, 6, 4, 1, 0, 15, 14, 5, 7, 2, 12]]
garfield=[13, 1, 9, 14, 13, 0, 14, 13, 8, 1, 6, 1, 9, 5, 15]
[13, 2, 9, 0, 8, 9, 6, 5, 1, 15]
[13, 1, 9, 14, 13, 0, 14, 13, 8, 6, 9, 5, 15]
print(placer_and_calculator([12,0,12]),"AAAAAAAAAAAAAAAAAAAA")
print(placer_and_calculator([0]),"AAAAAAAAAAAAAAAAAAAA")
[13, 1, 9, 14, 13, 0, 14, 13, 8, 6, 9, 5, 15]
[0, 1, 2, 10, 4, 12, 6, 15, 8, 14, 11, 5, 9, 7, 3, 13]

#5, 14, 8, 6, 12, 15
[4, 7, 6, 14, 0, 10, 2, 9, 12, 15, 13, 5, 8, 11, 3, 1]
#z=1/0
repeat=0
begin=0
end=0
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






for i in range(0,16):
    z=0
    if len(garfield)==1:
        break
    while(z!=len(garfield)-1):
        if len(garfield) == 1:
            break
        #print([2, 3, 4, 1, 1, 4, 3])
        if garfield[z]==garfield[z+1] :
            del garfield[z:z+2]
            z=0
        z+=1
for i in range(0,len(pattern_for_3)):
    z=1
    if len(garfield)==1 or len(garfield)==2:
        break
    while(z!=len(garfield)-1):
        if len(garfield) == 1:
            break
        if [garfield[z-1],garfield[z],garfield[z+1]]==pattern_for_3[i] :

            del garfield[z+1]
            del garfield[z-1]
            z=1
        z+=1
print(garfield,"aaa??ssssss?")


