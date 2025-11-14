s=input()
lst=[]
for x in s.split('.'):
  x1=str(f'{int(x):08b}')
  lst.append(x1)
print('.'.join(lst))