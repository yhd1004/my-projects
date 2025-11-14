n=int(input())
count=0
for i in range(n):
    num=int(input())
    count+=num
average=float(count/n)
print(f'{average:.2f}')