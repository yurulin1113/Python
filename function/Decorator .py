def fn():
    print("我是fn")


def fn2():
    print("函數開始執行")
    fn()
    print("函數執行結束")


fn2()


print('*'*40)


def add(a, b):
    r = a+b
    return r


def newadd(a, b):
    print("函數開始執行")
    r = add(a, b)
    print("函數執行結束")
    return r


r = newadd(123, 456)
print(r)
