s=int(input())
if s<=3:
    f=13
elif 3<s<=15:
    f=13+2.3*(s-3)
else:
    f=13+2.3*12+(2.3+2.3*0.5)*(s-15)
print(f'{f:.2f}')