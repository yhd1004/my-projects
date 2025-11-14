def isprime(n):
 if n==2:return True
 if n%2==0:return False
 end=int(n**0.5)+1
 for i in range(3,end,2):
  if n%i==0:
    return False
 return True
num=int(input())
j=1
a=2
while j<num:
    a+=1
    if isprime(a):
        j+=1
    if j==num:
        break
print(a)