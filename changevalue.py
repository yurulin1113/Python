a = [1, 2, 3]
print("修改前:", a, id(a))

# 改對象
a[0] = 10
print("修改後:", a, id(a))

# 改變量
a = [4, 5, 6]
print("修改後:", a, id(a))
