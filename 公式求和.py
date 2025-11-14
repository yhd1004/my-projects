n=int(input())
n<=10000
q=0
e=0
s=1
for i in range(1,n+1):
    if i%2==0:
        x=s/i
        q+=x
    else:
        y=s/i
        e+=y
print(f"{e-q:.6f}")
