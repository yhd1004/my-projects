def nms(p):
    M=2**p-1
    flag=True
    end=int(M**0.5)+1
    for i in range(2,end):
        if M%i==0:
            flag=False
            break
    return flag
num=int(input())
if nms(num):
    print('YES')
else:
    print('NO')
    