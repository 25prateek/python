
r1=int(input("enter the row no."))
c1=int(input("enter the column no"))
m1 = [[int(input()) for x in range (c1)] for y in range(r1)]
'''
m1=[]
for i in range(r1):
    a=[]
    print("enter  row values")
    for j in range(c1):
        a.append(int(input()))
    m1.append(a)
'''
#print(m1)

r2=int(input("enter the row no."))
c2=int(input("enter the column no"))
m2 = [[int(input()) for x in range (c2)] for y in range(r2)]
'''
m2=[]
for i in range(r2):
    b=[]
    print("enter the values in rows")
    for j in range(c2):
        b.append(int(input()))
    m2.append(b)
'''
print(m1)
print(m2)
'''
def printmatrix(m,rsize,csize):
    for i in range(rsize):
        for j in range(csize):
            print(m[i][j], end=" ")

        print()

printmatrix(m1,r1,c1)
printmatrix(m2,r2,c2)
'''
r = [[0 for i in range(r2)]
            for j in range(c1)]

for i in range(len(m1)):
   for j in range(len(m2[0])):
      for k in range(len(m2)):
         r[i][j] += m1[i][k] * m2[k][j]
print("The Resultant Matrix Is ::>")
for i in r:
   print(i)