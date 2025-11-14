
n=int(input())
2<=n<=50000
a=[True]*(n+1)
a[0]=a[1]=False
for i in range(2,int(n**0.5)+1):
    if a[i]:
        for j in range(i*i,n+1,i):
            a[j]=False
print(sum(a[2:]))

'''
n = int(input())
if n < 2:
    print(0)
else:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    print(sum(is_prime[2:]))
'''
