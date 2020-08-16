class Myclass():
    pass


mc = Myclass()
mc2 = Myclass()
mc3 = Myclass()
mc4 = Myclass()

# 是否一個CLASS
result = isinstance(mc, Myclass)
print('result=', result)

print(id(mc), type(mc))
print(id(Myclass), type(Myclass))

mc.name = '孫悟空'
mc2.name = '貝吉塔'

print(mc.name)
print(mc2.name)
