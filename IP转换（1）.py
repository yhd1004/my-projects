a,b,c,d=map(str,input().split('.'))
tp1=tuple(str(int(x,2)) for x in(a,b,c,d))
print('.'.join(tp1))
