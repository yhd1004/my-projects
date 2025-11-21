n=int(input())
count=0
for i in range(n):
    s=input()
    p=set(s)
    if set(s)=={'X','T','U'}:
     count+=1
print(count)
    
