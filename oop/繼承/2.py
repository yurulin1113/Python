# 優先去當前對象中尋找是否有方法
# 如果沒有,則去當前父類中尋找
# 如果有又沒有,則去父類的父類找


# 父
class A(object):
    def test(self):
        print('aaa')


# 子
class B(A):
    def test(self):
        print('bbb')


# 孫
class C(B):
    def test(self):
        print('ccc')
    pass


c = C()

c.test()
