class dog():
    count = 0

    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age

    def bark(self):
        print(f'{self.hidden_name}汪~~~~~')

    # get獲取
    def get_name(self):
        print('使用者讀取屬性!')
        dog.count += 1
        return self.hidden_name

    def get_age(self):
        print('使用者讀取屬性!')
        dog.count += 1
        return self.hidden_age

    # set改值
    def set_name(self, name):
        print('使用者修改屬性!')
        self.hidden_name = name

    def set_age(self, age):
        # 設條件
        if age > 0:
            print('使用者修改屬性!')
            self.hidden_age = age


dog1 = dog('來福', 8)

dog1.set_name('旺財')
dog1.set_age(-10)

print(dog1.get_name(), dog1.get_age(), f'\n讀取:{dog.count}')
