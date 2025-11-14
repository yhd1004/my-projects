s=input()
dct={}
for x in s:
 if x.islower():
  dct[x]=dct.get(x,0)+1
if not dct:pass
sorted_items=sorted(dct.items(),key=lambda x:(-x[1],x[0]))
print(*sorted_items[0])


