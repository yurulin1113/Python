s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5}

# &
result = s1 & s2
print("&=", result)

# |
result = s1 | s2
print("|=", result)

# -
result = s1-s2
print("-=", result)

# ^不相交的
result = s1 ^ s2
print("^=", result)

# <=是否另一個子集
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
result = b <= a
print("b是否屬於a的子集?? =", result)
result = {1, 2, 3} <= {1, 2, 3}
print('result=', result)

# <是否另一個真子集
result = b < a
print("b是否屬於a的子集??", result)
result = {1, 2, 3} < {1, 2, 3}
print('result=', result)

# >=是否另一個超集
# >另一個真超集
