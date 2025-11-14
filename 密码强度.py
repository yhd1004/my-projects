password=input().strip()
a=b=c=d=0
if len(password)<8:
     summation=1
else:
     for ch in password:
         if ch.isalpha():
             a=1
         elif ch.isdigit():
             b=1
         elif ch in '''?!.,'";:`_-()[]/*''':
             c=1
         else:
             d=1
summation=a+b+c+d
judge=[' ','weak','medium','good','excellent']
print(judge[summation])
  
