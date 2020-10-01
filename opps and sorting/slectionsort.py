
def ssort(list):
    for i in range(6):
        min = i
        for j in range(i,6):

            if  list[j] < list[min]:
                min=j
        t = list[i]
        list[i] = list[min]
        list[min] = t
    print(list)

list=[4,8,3,16,5,9]

ssort(list)