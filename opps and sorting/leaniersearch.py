
def search(list,n):
    l=list
    for i in range(len(list)):
        if l[i]==n :
            print("found")
            break
    else :
        print("not found")


list=[4,8,3,16,5,9]
n=9
n=search(list,n)