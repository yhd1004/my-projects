def fun_a(n):
    lst1=[]
    for j in range(n):
     s=tuple(input().split())
     lst1.append(s)
    return lst1   
n=int(input())
lst1=fun_a(n)
dct2={}
for j in range(n):
    r=tuple(input().split())
    y=lst1[j]
    r1={r[1]:(r[0],y[0])}
    dct2.update(r1)
lst2=sorted(dct2.items(),key=lambda x:int(x[0]))
for x in lst2:
    k,v=x[1]
    a=x[0]
    print(a,k,v)
    

   