n=int(input())
count=0
for i in range(1,n+1):
    if i%2==0:
        i=-i
    s=1/i
    count+=s
print(f'{count:.6f}')