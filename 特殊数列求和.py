a,n=map(int,input().split())
a<=9
n<=10
s=''
count=0
if a>n:
    a,n=n,a
for i in range(n):
    s1=s+str(a)
    count+=int(s1)
    s=s1
print(count)
    