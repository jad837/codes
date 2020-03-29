from math import ceil,log2
n=110

x=int(ceil(log2(n)))
print(x)
max_size = 2* (int) (2**x)-1
print (max_size)

st=[0]*max_size
