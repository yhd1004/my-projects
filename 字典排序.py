s=input().split()
lst1=[]
lst2=[]
for i in range(len(s)):
    if i%2==0:
        lst1.append(s[i])
    else:
        lst2.append(s[i])
tp1=tuple(lst1)
tp2=tuple(lst2)
dct=dict(zip(tp1,tp2))
dct1=sorted(dct.items(),key=lambda x:int(x[1]) ,reverse=True)
for x in dct1:
    k,v=x
    print(k,v,end=' ')

        
