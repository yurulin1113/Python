def fn():
    def fn2():
        print("hello")
    return fn2()


# r = fn()  # 執行返回值
# print(fn())
# print(r)


def fn2():
    a = 10
    return


def fn3():
    print("hello")
    return
    print("abc")


# r = fn3()
# print(r)

def fn4():
    for i in range(5):
        if i == 3:
            return
        print(i)


# fn4()

def sum(*nums):
    result = 0
    for i in nums:
        result += i
    return result


# r = sum(1, 2, 3, 4, 5)
# print(r)
# print(r+15)
