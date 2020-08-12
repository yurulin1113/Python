# Set重複被省略
S = {1, 2, 3, 4, 5, 6, 1, 5, 6, 3}

S1 = set({1, 2, 3, 4, 5, 6})
S2 = set('hello')
S3 = set({'a': 1, 'b': 2, 'c': 3})
S4 = set({'a', 'b', 1, 2, 3})

print(S1, type(S1))
print(S2, type(S2))
print(S3, type(S3))
print(S4, type(S4))
print(len(S1))

print('*'*40)

# add
a = set({1, 3, 5, 8, 9})
a.add(10)
a.add(10)

print(a)

print('*'*40)

# update
b1 = set({1, 2, 3, 5, 8, 9})
b2 = set('hello')
b1.update(b2)
b1.update({10: 'a', 20: 'b'})  # 只有keys
print(b1)

print('*'*40)

# pop刪除
result = b1.pop()
print('result=', result)
print(b1)

print('*'*40)

# remove()指定
b3 = {1, 2, 3, 4, 5}
result = b3.remove(1)
print('result=', result)
print(b3)

print('*'*40)

# clear

# copy
