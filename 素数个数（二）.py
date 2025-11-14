def fun(lst,idx):
    for i in range(idx+idx,len(lst),idx):
        lst[i]=0
def ES(lst):
    for idx in lst:
        if idx!=0:
            fun(lst,idx)        
n=int(input())
lst=[x for x in range(n+1)]
lst[0]=lst[1]=0
ES(lst)
tp=tuple(x for x in lst if x!=0)
print(len(tp))

    
        