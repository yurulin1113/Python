#mytuple = ()
# print(type(mytuple))

#mytuple = (1, 2, 3, 4, 5)
# print(mytuple)
# print(mytuple[2])

#my = 1, 2, 3, 4, 5
# print(type(my))
# print(my)

# 解構
#my = 1, 2, 3, 4, 5
#a, b, c, d, e = my
#print("a=", a)
#print("b=", b)
#print("c=", c)
#print("d=", d)
#print("e=", e)

# 解構交換
#a = 1
#b = 2
#c = 3
#a, b, c = c, b, a
#print(a, b, c)

# 加上*全列出,不能兩個*
my = 1, 2, 3, 4, 5, 6, 7
a, b, *c = my
a, *b, c = my
*a, b, c = my
print("a=", a)
print("b=", b)
print("c=", c)

print("*"*30)

*a, b, c = "hello"
print("a=", a)
print("b=", b)
print("c=", c)
