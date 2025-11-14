s=input()
length=len(s)
m=length//2
left_part=s[:m]
right_part=s[-1:m-1:-1]
print(int(right_part)+int(left_part))
    
    