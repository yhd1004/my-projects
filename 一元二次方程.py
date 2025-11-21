a,b,c=map(float,input().split())
a!=0
delta=b**2-4*a*c
if delta>0:
    x1=(-b-(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b+(b**2-4*a*c)**0.5)/(2*a)
    if x1>x2:
        x1,x2=x2,x1
    print(f'x1={x1:.5f};x2={x2:.5f}')
elif delta==0:
    x1=x2=(-b+(b**2-4*a*c)**0.5)/(2*a)
    print(f'x1=x2={x1}')
else:
    print('No answer!')