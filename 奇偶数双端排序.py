n=int(input())
s=map(int,input().split())
jp=[]
op=[]
str=''
for x in s:
    if x%2!=0:
        jp.append(x)
        jp.sort(reverse=True)
    else:
        op.append(x)
        op.sort()
total=jp+op
for y in total:
  print(y,end=' ')
