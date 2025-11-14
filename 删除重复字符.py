s=input()
count_alpha={}
for alpha in s:
    if alpha in count_alpha:
        count_alpha[alpha]+=1
    else:
        count_alpha[alpha]=1
remain_s=''  
for x in count_alpha:
    if count_alpha[x]==1:
        remain_s+=x
if len(remain_s)==0:
 print('none')
else: 
 print(remain_s)
    
