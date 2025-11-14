electricity_consumption=int(input())
if electricity_consumption<=200:
 fee=electricity_consumption*0.588
elif 200<electricity_consumption<=350:
 fee=200*0.588+(electricity_consumption-200)*0.638
else:
 fee=200*0.588+150*0.638+(electricity_consumption-350)*0.888
print(f'{fee:.2f}')
    
