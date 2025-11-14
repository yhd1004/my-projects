dict1={'0550':'机械工程学院','0556':'计算机学院','0557':'自动化与电子信息学院', '0560':'化学学院','0565':'化工学院',
       '0572':'材料科学与工程学院','0582':'环境与资源学院', '0580':'土木工程与力学学院','0571':'物理与光电工程学院',
       '0575':'数学与计算科学学院','0501':'马克思主义学院', '0502':'哲学与历史文化学院','0519':'公共管理学院',
       '0525':'法学部', '0513':'商学院','0543':'艺术学院', '0531':'外国语学院', '0537':'文学与新闻学院',
       '0585':'国际交流学院', '0596':'兴湘学院'}
s=input().split()
count={}
for x in s:
    data=x[4:8]
    if data in dict1:
       count_name=dict1[data]
    else:
       count_name='其他'
    if count_name in count:
        count[count_name]+=1
    else:
        count[count_name]=1
tp=sorted(count.items(),key=lambda x:x[1],reverse=True)
for i in range(3):
    k,v=tp[i]
    print(k,v)
    


        
        
       

    

    
        

     
