b = 10  # global variable


def fn():
    a = 10
    print('內部:', 'a=', a)
    print('內部:', 'b=', b)


# fn()


def fn2():
    a = 30

    def fn3():
        print('fn3中:', 'a=', a)
    fn3()


# fn2()

a = 20


def fn3():
    global a  # 修改為global
    a = 10  # local variable
    print("內部:", 'a=', a)


fn3()
print("外部:", 'a=', a)
