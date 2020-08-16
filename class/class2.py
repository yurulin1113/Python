class person():
    name = 'Roger'

    def hello(self):
        print('你好')


p1 = person()
p2 = person()


p1.hello()
p2.hello()

# --------------------------------------------------------
print('*'*40)

# 修改屬性
p1.name = 'Kevin'
p2.name = 'David'

# 刪除屬性
#del p2.name

print(p1.name)
print(p2.name)

# ----------------------------------------------------
print('*'*40)


class person():
    name = 'Roger'

    def hello(self):
        print(f'你好!我是{self.name}')


p1 = person()
p2 = person()
p3 = person()


p1.name = '孫悟空'
p2.name = '貝吉塔'

p1.hello()
p2.hello()
p3.hello()
