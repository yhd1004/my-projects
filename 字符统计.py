import string
n=input()
a=b=c=d=0
for i in n[::]:
    if i in string.ascii_letters:
        a+=1
    elif i in string.digits:
        b+=1
    elif i in string.whitespace:
        c+=1
    else:
        d+=1
print(b,a,c,d,end=" ")
