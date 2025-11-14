import random
lst=list(random.randint(x) for x in range(25))
dct={data:lst.count(data) for data in lst}
max_value=max(dct.values())
tp=tuple(item for item in dct if item[1]==max_value)
print(max(tp))
