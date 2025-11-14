s=input()
a=0
b=0
c=0
d=0
for x in s:
 if x.isdigit():
   a+=1
 elif x.isalpha():
   b+=1
 elif x.isspace():
   c+=1
 else:
   d+=1
print(a,b,c,d,end=' ')