# 父類
class animal:
    def run(self):
        print('動物跑')

    def sleep(self):
        print('動物睡')

    def bark(self):
        print('動物叫')


# 繼承
class dog(animal):
    def bark(self):
        print('汪汪汪汪!!')


class tiger(animal):
    def eat(self):
        print('老虎開吃!!!')


d = dog()
t = tiger()

t.eat()

# d.bark()
# d.run()
# d.sleep()

# isinstance函數來判斷一個對像是否是一個已知的類型
# r1 = isinstance(d, dog)
# r2 = isinstance(d, animal)
# print(r1)
# print(r2)

# issubclass是否另一類的子類
print(issubclass(animal, animal))
print(issubclass(animal, tiger))
print(issubclass(animal, dog))


# 省略父類則預設父類object
class person:
    pass


print(issubclass(person, object))
