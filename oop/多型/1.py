class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    # __len__方法獲取長度
    def __len__(self):
        return 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C:
    pass


p1 = A('Roger')
p2 = B('Kevein')
p3 = C()  # 沒東西~~


def hello(obj):
    print(f'你好!{obj.name}')


# 設條件但是違反多型!!!!!一般開發不會使用
def hello(obj):
    if isinstance(obj, A):
        print(f'你好!{obj.name}')


# hello(p1)
# hello(p2)
# hello(p3)


print(len(p2))
# print(len(p3))  # 沒方法~~
