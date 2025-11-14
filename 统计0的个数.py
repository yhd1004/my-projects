n=input()
ip=[]
for x in n.split('.'):
    s=f'{int(x):08b}'
    ip.append(s)
ip1=".".join(ip)
print(ip1.count('0'))
