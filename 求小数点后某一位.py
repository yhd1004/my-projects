a,b,n=map(int,input().split())
remainder=a%b
for _ in range(n):
    remainder*=10
    m=remainder//b
    remainder%=b
print(m)
