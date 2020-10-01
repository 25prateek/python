
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    for i in range(6):
        mid=(l+u)//2
        if(n==list[mid]):
            globals()['pos']=mid
            print("found at position after soting",mid+1) # its show two time because second time we call it again  in if conditio
            return True
        else :
            if list[mid] < n:
                l = mid
            else:
                u=mid



list=[4,8,3,16,5,9]
list=sorted(list)
print(list)
n=9
k=search(list,n)

if search(list,n):
    print("found at ",pos+1)