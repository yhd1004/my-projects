s=input()
lst=[]
for x in s.split('.'):
 x1=str(int(x,2))
 lst.append(x1)
print('.'.join(lst))