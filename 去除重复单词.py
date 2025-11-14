def delete(n):
    lst=[]
    for x in n:
        if x in lst:
            lst=lst
        else:
            if n.count(x)<=1:
             lst.append(x)
    return lst
    
s=input().split()
lst1=delete(s)
s1=' '.join(lst1)
print(s1)