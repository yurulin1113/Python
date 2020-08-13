def star():
    print("*"*40)


def a():
    print("hello")


a()

star()


def sum(a, b):
    return a+b


print(sum(1, 3))

star()


def mul(a, b, c):
    return a*b*c


print(mul(5, 6, 3))

star()


def username(x):
    return "歡迎"+x+"光臨"


print(username("孫悟空"))

star()


def fn(a, b, c=30):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fn(1, 2)
fn(1, 2, 3)
