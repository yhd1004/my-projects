s=input().strip()
count_num=0
count_alpha=0
count_spacebar=0
count_other=0
for x in s:
 if x.isdigit():
   count_num+=1
 elif x.isalpha():
   count_alpha+=1
 elif x.isspace():
   count_spacebar+=1
 else:
   count_other+=1
print(count_num,count_alpha,count_spacebar,count_other,end=' ') 
 
