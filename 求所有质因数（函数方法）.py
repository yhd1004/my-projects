def isprime(n):
    end=int(n**0.5)+1
    if n==2:return True
    if n%2==0:return False
    for i in range(3,end,2):
        if n%i==0:
            return False
    return True
n=int(input())
lst=[]
i=2
while i<n:
 if n%i==0 and isprime(i):
   lst.append(i)
 i+=1
print(*lst)