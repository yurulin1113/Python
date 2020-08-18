class A:
    def __init__(self):
        self.name = 'A類別'

    # del特殊方法,回收前可調用
    def __del__(self):
        print('A()對象被刪除', self)


a = A()

# 使用b來引用a
b = a


print(a.name)

# 沒有任何變量A()對象進行引用,變成垃圾~~
#a = None
#b = None

# 要一起刪除
#del a, b


input('退出~~')
