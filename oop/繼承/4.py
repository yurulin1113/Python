class A(object):
    def test(self):
        print('aaa')


class B(object):
    def test(self):
        print('b中test()')

    def test2(self):
        print('bbb')


# 多重繼承指定多個父類認乾爹~~~
# 開發中沒有特殊情況,避免使用多重繼承
# C(誰在前面覆蓋誰的方法)
class C(B, A):
    pass


# __bases__可以獲取當前類所有父類
# print(B.__bases__)
# print(C.__bases__)

c = C()
c.test()
c.test2()
