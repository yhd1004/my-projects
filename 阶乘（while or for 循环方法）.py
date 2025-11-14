n=int(input())
a=1
'''
i=1
while i<=n:
    a*=i
    i+=1
print(a)
'''
for i in range(1,n+1):
    a*=i
print(a)
