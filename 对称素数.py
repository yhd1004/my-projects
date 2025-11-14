def isprime(n):
    end=int(n**0.5)+1
    for i in range(2,end):
        if n%i==0:
            return False
    return True

def is_symmetric_prime(n):
    s=str(n)
    s1=s[::-1]
    n1=int(s1)
    end=int(n1**0.5)+1
    for i in range(2,end):
        if n1%i==0:
            return False
    return True   
s,t=map(int,input().split())
count=0
for x in range(s,t+1):
     if isprime(x) and is_symmetric_prime(x):
         count+=1
print(count)