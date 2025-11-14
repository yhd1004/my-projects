def isprime(n):
    if n==1:return False
    if n%2==0:return False
    if n==2:return True
    end=int(n**0.5)+1
    for i in range(3,end,2):
        if n%i==0:
         return False
    return True
def right(num):
    s=str(num)
    s1=s[1:]
    return int(s1)
def judge(x):
    s=str(x)
    s2=s[1]
    if int(s2)==0:
        return False
    return True
    
s,t=map(int,input().split())
10<=s<=t<=1000000
count=0
for i in range(s,t+1):
    if isprime(i) and isprime(right(i)) and judge(i):
        count+=1
print(count)