
print("ennter the 1st matrix values")
r1=int(input("enter the row no."))
c1=int(input("enter the column no"))
m1 = [[int(input()) for x in range (c1)] for y in range(r1)]

print ("enter th second matrix")
r2=int(input("enter the row no."))
c2=int(input("enter the column no"))
m2 = [[int(input()) for x in range (c2)] for y in range(r2)]

print(m1)
print(m2)

r = [[0 for i in range(r2)]
            for j in range(c1)]

for i in range(len(m1)):
   for j in range(len(m2[0])):
      for k in range(len(m2)):
         r[i][j] += m1[i][k] * m2[k][j]
print("The Resultant Matrix Is :-")
for i in r:
   print(i)
