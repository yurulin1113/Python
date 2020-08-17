class dog():

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def bark(self):
        print(f'{self.name}汪~~~~~')

    def bite(self):
        print(f'{self.name}咬死你!!!!')

    def run(self):
        print(f'{self.name}瘋狗跑起來~~~~')


dog1 = dog('中共', 13, 'male', 10)

# 修改屬性的值,這種方式可以隨意修改不安全
dog1.name = '阿黑'
dog1.age = -50
print(dog1.name, dog1.age)
