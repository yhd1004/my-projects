n=int(input())
lst=[]
lst1=[]
a=0
summation=0
for _ in range(n):
    s=tuple(input().split())
    lst.append(s)
for x in lst:
    if int(x[1])>80 and int(x[5])>=1:
        a+=8000
    if int(x[1])>85 and int(x[2])>80:
        a+=4000
    if int(x[1])>90:
        a+=2000
    if int(x[1])>85 and x[4]=='Y':
        a+=1000
    if int(x[2])>80 and x[3]=='Y':
        a+=850
    summation+=a
    lst1.append((x[0],a))
    a=0
lst1.sort(key=lambda x:x[1],reverse=True)
p,t=lst1[0]
lst2=[p,t,summation]
for y in lst2:
    print(y)


        
    