s=input()
weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,1,]
dct={x:12-x for x in range(3,11)}
print(dct)
dct1={0:1,1:0,2:'X'}
dct.update(dct1)
m=0
for i in range(0,17):
    m+=int(s[i])*int(weight[i])
y=m%11
x=dct[y]
print(x)
