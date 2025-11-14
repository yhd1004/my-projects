m,n=map(int,input().split())
lst=[]
for i in range(m,n):
    if i%3==1 and i%7==2 and i%11==3:
        for j in range(2,int(i**1/2)+1):
                        if i%j!=0:
                          lst.append(i)
print(lst.index(0))
                        
