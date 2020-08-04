a = True

a = int(a)


print("a=", a)

print("類型", type(a))
print("----------------------------")

a2 = '123'
a2 = int(a2)

a3 = 123.5464
a3 = int(a3)

print("a2=", a2)
print("a2類型", type(a2))

print("a3=", a3)
print("a3類型", type(a3))

# 先轉float
a4 = '11.5'
a4 = int(float(a4))
print("a4=", a4)
print("a4類型", type(a4))

print("----------------------------")

a5 = False
a5 = int(a5)
print("a5=", a5)
print("a5類型", type(a5))

a6 = 132.54
a6 = str(a6)
print("a6=", a6)
print("a6類型", type(a6))

a7 = ''  # 0,None,''--->false
a7 = bool(a7)
print("a7=", a7)
print("a7類型", type(a7))


print("----------------------------")

b = 123

print('hello'+str(b))  # 接串

print("-----------------------------")
