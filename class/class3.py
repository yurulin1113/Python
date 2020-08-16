class person():
    # 不創建對象也會執行
    print('Person程式碼')

    # magic魔術方法不要嘗試調用,自動調用
    # init會在對象創建后執行
    # 初始化~
    def __init__(self, name):
        # print('init執行了~~')
        self.name = name

    def hello(self):
        print(f'大家好,我是{self.name}')


p1 = person('孫悟空')
p1.hello()
print(p1.name)

print("*"*40)

p2 = person('貝吉塔')
p2.hello()
print(p2.name)


# p3 = person()
# p4 = person()


# ---------------------------------------------------------

# 手動添加name,會出問題!!!
# p1 = person()
# p1.name = 'roger'


# p2 = person()
# p2.name = 'kevin'


# p1.hello()
# p2.hello()

# dp1.__init__() 別這麼做!!
