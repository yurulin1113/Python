def fn():
    print("我是fn")


def add(a, b):
    r = a+b
    return r


def mul(a, b):
    r = a*b
    return r

# ------------------------------------------------------------


def begin_end(old):

    def new_fun():
        print('fun start~~~')
        old()
        print('fun end~~~')
    return new_fun


f = begin_end(fn)

f()

print("*"*40)
# ----------------------------------------------------------------


def begin_end2(old):

    def new_fun2(a, b):
        print('fun2 start~~~')
        result = old(a, b)
        print('fun2 end~~~')
        return result
    return new_fun2


f = begin_end2(add)
r = f(123, 456)
print(r)


print("*"*40)


# ----------------------------------------------------------------


# 再進階~~~
def begin_end3(old):
    def new_fun3(*args, **kwargs):
        print('fun3 start~~~')
        result = old(*args, **kwargs)
        print('fun3 end~~~')
        return result
    return new_fun3


f1 = begin_end3(fn)
f2 = begin_end3(add)
f3 = begin_end3(mul)

r1 = f1()
r2 = f2(3, 3)
r3 = f3(3, 3)
print(r1, r2, r3)

print("*"*40)
# ----------------------------------------------------------------

# 裝飾器@

# 由內往外


@begin_end
@begin_end3
def sayhello():
    print("大家好~~~")


sayhello()
