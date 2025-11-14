n=int(input())
a=0
b=2
while True:
 s=True
 for i in range(2,int(b**0.5)+1):
   if b%i==0:
      s=False
      break
 if s:
   a+=1
   if a==n:
        print(b,end='')
        break
 b+=1