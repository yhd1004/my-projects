ip=input()
ip1=[]
for x in ip.split('.'):
    in_ip=f'{int(x):08b}'
    ip1.append(in_ip)
print('.'.join(ip1))
