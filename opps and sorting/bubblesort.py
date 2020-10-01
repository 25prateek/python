def bsort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                t=list[j]
                list[j]=list[j+1]
                list[j+1]=t
    print(list)


list=[4,8,3,16,5,9]

bsort(list)
