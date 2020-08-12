# del刪除keyvalue
a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5, 'f': 6}
del a['a']
del b['d']
print(a, b)

print('*'*40)

# poptime()隨機刪除通常都最後一個
c = dict(name='roger', age=18, gender='male')
result = c.popitem()
print('result=', result)
print(c)

print('*'*40)

# pop(key,default)刪除特定
d = dict(a=1, b=2, c=3)
result = d.pop('c')
result = d.pop('z', 'default')
print('result=', result)
print(d)

print('*'*40)

# claer全部清除
v = dict(a=15, b=5, c=5)
print(v)
v.clear()
print(v)

print('*'*40)

# copy複製
ssd = dict(a=516, b=489, c=655)
ssd2 = ssd.copy()
ssd['a'] = 156165
print(ssd)
print(ssd2)

# copy兩個改變??因為只會淺D複製簡單對像內部
ssd3 = {'a': {'name': '孫悟空', 'age': 24}, 'b': 132, 'c': 15156}
ssd4 = ssd3.copy()
ssd4['a']['name'] = '沙悟淨'

print(ssd3)
print(ssd4)
