s=input().strip()
n=int(input())
t=s.index('*')
lst=[]
lst1=[]
for i in range(n):
    a=input().strip()
    lst.append(a)
for x in lst:
   if len(x)<len(s):
    if x[0:t]==s[0:t] and x[t:]==s[t+1:]:
        lst1.append('Y')
    else:
        lst1.append("N")
   elif len(x)==len(s):
    if x[0:t]==s[0:t] and x[t+1:]==s[t+1:]:
        lst1.append('Y')
    else:
        lst1.append("N")
   else:     
    h=len(x)-len(s)
    if x[0:t]==s[0:t] and x[t+1+h:]==s[t+1:]:
        lst1.append('Y')
    else:
        lst1.append('N')
for y in lst1:
    print(y,end='')
                
    
        
        
