class animal:
    def __init__(self, name):
        self._name = name

    def run(self):
        print('動物跑')

    def sleep(self):
        print('動物睡')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class dog(animal):
    def __init__(self, name, age):
        # super()返回對象調用父類方法,不需要傳self
        super().__init__(name)
        self._age = age

    def bark(self):
        print('汪汪汪汪!!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


d = dog('旺財', 18)

print(d.name)
print(d.age)
