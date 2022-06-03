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

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


# How many elements each
# list should have
n = 2

pattern2=[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],
         [7,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13],
         [14,14],[15,15]]
garfield=[5, 14, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 6, 12, 14, 2, 2, 15, 14]
[0, 1, 2, 10, 4, 12, 6, 15, 8, 14, 11, 5, 9, 7, 3, 13]
[0, 1, 2, 10, 4, 12, 6, 15, 8, 14, 11, 5, 9, 7, 3, 13]

#TODO система защиты от дурака, как её сделать придумать
begin=-1
end=-1
for z in range(0,16):
    for i in range(0,len(garfield)):
        if garfield[i]==z:
            begin=i




for i in garfield:
    print(i)

print(placer_and_calculator([12, 6, 15, 5, 0, 8, 1, 4]))
#5, 14, 8, 6, 12, 15
[4, 7, 6, 14, 0, 10, 2, 9, 12, 15, 13, 5, 8, 11, 3, 1] [12, 6, 15, 5, 2, 12]
