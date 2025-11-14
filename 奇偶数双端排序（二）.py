n=int(input())
array=map(int,input().split())
lst_odd=[]
lst_even=[]
for x in array:
 if x%2!=0:
  lst_odd.append(x)
 else:
  lst_even.append(x)
lst_odd.sort(reverse=True)
lst_even.sort()
print(*lst_odd,*lst_even,end=' ')