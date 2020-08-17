# __雙下滑線隱藏屬性只能在類裡調用(微隱藏)一般不用!!外部還是可以
class person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


p1 = person('Roger')

# 改不了了~~~
# p1.name = 'dsdsd'
# p1.__name='sadad'

print(p1._person__name)

# 改了
p1._person__name = 'Kevin'

print(p1.get_name())
