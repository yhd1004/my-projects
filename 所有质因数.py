import math
n=int(input())
max_num=200000
a=[True]*(max_num+1)
a[0]=a[1]=False
for i in range(2,int(math.isqrt(max_num)+1)):
    if a[i]:
        for j in range(i*i,max_num+1,i):
            a[j]=False
b=[i for i,prime in enumerate(a) if prime]
print(b[n-1])




