# 還有很多一系列特殊方法~~~~~~~~~
class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'hello'

    def __gt__(self, other):
        return self.age > other.age

    def __bool__(self):
        return True


p1 = person('roger', 20)
p2 = person('david', 30)

# print(repr(p))

#print(p1 < p2)
# print(p1 > p2)

# print(bool(p1))

if p1:
    print(p1.name, '成年')

else:
    print(p1.name, '未成年')
