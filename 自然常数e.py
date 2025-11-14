n=int(input())
a=1
count=1
for i in range(1,n+1):
    a*=i
    s=1/a
    count+=s
print(f'{count:.10f}')
    