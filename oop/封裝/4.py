# _一條下滑線隱藏屬性只能在類裡調用私有屬性
class person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


p1 = person('Roger')

# print(p1._person_name)

# 改了
p1._person_name = 'Kevin'

print(p1.get_name())
