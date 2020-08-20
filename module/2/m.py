a = 10
b = 20

# _只能在模組內訪問,通過import*引入部會引入
_c = 30


def test():
    print('test')


def test2():
    print('test2')


class person:
    def __init__(self):
        self.name = 'Roger'


# 測試當前是否為主模組
if __name__ == '__main__':
    test()
    test2()
    p = person()
    print(p.name)
