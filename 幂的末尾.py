a,b=map(int,input().split())
c=a**b
s=str(c)
n=int(s[-3:])
print(f'{n:03d}')
