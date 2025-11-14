s=input()
lst=list(s)
for i in range(len(s)):
    if not lst[i].isalpha():
        lst[i]=' '        
s=''.join(lst).lower()
lst=s.split()
lst.sort()
print(*lst)
