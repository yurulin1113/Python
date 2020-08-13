# 不定長參數*
def sum(*nums):
    result = 0
    for n in nums:
        result += n
    print(result)


sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# *c後面全給
def fn(a, b, *c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


fn(1, 2, 3, 4, 5, 6, 7)

print("*"*40)


# 注意*放中間或前面需給值給c或b
def fn2(a, b, *c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


fn2(1, 2, 3, 4, 5, 6, 7)

print("*"*40)


# 在開頭放*所有都附值
def fn3(*, a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


fn3(a=3, b=4, c=5)

print("*"*40)


# **可以接收其他參數,value式參數
def fn4(b, c, **a):
    print("a=", a, type(a))
    print("b=", b, type(b))
    print("c=", c, type(c))


fn4(b=1, c=2, d=98, e=10, f=20)
