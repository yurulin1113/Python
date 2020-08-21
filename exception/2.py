# 異常傳播
def fn():
    print('hello fn')
    print(10/0)


def fn2():
    print('hello fn2')
    fn()


def fn3():
    print('hello fn3')
    fn2()


fn3()
