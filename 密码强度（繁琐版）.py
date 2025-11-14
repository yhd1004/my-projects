import string
s=input()
letter_count=0
num_count=0
pun_count=0
el_count=0
for x in s:
    if x in string.ascii_letters:
        letter_count=1
    elif x in string.digits:
        num_count=1
    elif x in'''?!.,'";:`_-()[]/*''':
        pun_count=1    
    else:
        el_count=1      
a=len(s)
l=letter_count+num_count+el_count+pun_count
summation=['weak','medium','good','excellent']
if a<8:
    count=0
elif a>=8 and l==1:
    count=0
elif a>=8 and l==2:
    count=1
elif a>=8 and l==3:
    count=2
else:
    count=3
print(summation[count])
    


        
        
