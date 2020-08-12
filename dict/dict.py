d = {}

d = {'name': '孫悟空', 'age': 24, 'gender': 'male'}
print(d['name'], d['age'], d['gender'])

print("*"*35)

d = dict(name='孫悟空', age=24, gender="male")
print(d, type(d))

print("*"*35)

d = dict([('name', '孫悟空'), ('age', 24), ('gender', "male")])
print(d, type(d))

print("*"*35)

print("len=", len(d))

print("*"*35)

print('name' in d)  # 取鍵

print("孫悟空" in d['name'])  # 取值

print("*"*35)

n = 'name'
print(d[n])
print(d.get('name', 'default'))  # 預設值

print("*"*35)

# 加上
d['address'] = '台中'
print(d)

print("*"*35)

# 添加key-value
result = d.setdefault('name', '沙悟淨')
result = d.setdefault('name2', '沙悟淨')
print('result=', result)
print(d)

print("*"*35)

# 如有重複被後面替換
a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5, 'f': 6}
a.update(b)
print(a)
