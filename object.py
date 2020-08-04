a = 123
b = a

# 地址都一樣,除非重新附值
print(id(a))

print(id(b))

print(a == b)
