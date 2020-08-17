class person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 調用屬性像get一樣
    @property
    def name(self):
        print('get方法執行~~~')
        return self._name

    @property
    def age(self):
        return self._age

    # 調上面name,age屬性
    @name.setter
    def name(self, name):
        print('set方法執行~~~')
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age


p1 = person('Roger', 18)
p1.name = 'kevin'
p1.age = 20

# 調方法
print(p1.name)
print(p1.age)
