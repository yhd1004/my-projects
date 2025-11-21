n=int(input())
while n!=1:
    if n%2!=0:
        print(f'{n}*3+1={n*3+1}')
        n=n*3+1
    else:
        print(f'{n}/2={int(n/2)}')
        n=int(n/2)
print('End')