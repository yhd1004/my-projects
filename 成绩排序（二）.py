n=int(input())
lst=[]
for i in range(n):
    s=tuple(input().split())
    lst.append(s)
lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:int(x[1]),reverse=True)
for x in lst:
    a,b=x
    print(a,b)

    