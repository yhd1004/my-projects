m,n=map(int,input().split())
w=map(int,input().split())
word=list(w)
count=0
lst=[]
for x in word:
  if len(lst)<m:
    if x not in lst:
           lst.append(x)
           count+=1
  if len(lst)==m:
    if x not in lst:
           h=lst[0]
           lst.remove(h)
           lst.append(x)
           count+=1
print(count)


            

    
    