from array import *

vals = array('i',[2,5,7,-3,5,6])
print(vals)
#vals.reverse()
#print(vals.buffer_info())
print(vals.typecode)
#print(vals)
#for i in range(6):
#    print(vals[i])

newarr= array(vals.typecode, (i**3 for i in vals))
for e in newarr:
    print(e)