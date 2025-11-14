s=input()
s1=s.capitalize()
tp1=('January','February','March','April','May','June','July','August','September','October','November','December')
tp2=('Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.')
dct={tp1[i]:tp2[i] for i in range(12)}
print(dct.get(s1,'Error'))
   

