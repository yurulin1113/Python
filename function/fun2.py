# 什麼都可以傳
def fn(x):
    print(x)


x = 123
x = "hello"
x = [1, 2, 3]
fn(x)
fn(fn)


# 注意參數類型
def fn2(a, b):

    print(a+b)


#fn2(123, "546")
fn2(123, 456)


# 不會影響其他變量
def fn4(a):
    a = 20
    print(a, id(a))


c = 10
fn4(c)
print(c, id(c))


# 被改變了對象
def fn5(a):
    a[0] = 20
    print(a, id(a))


c = [1, 2, 3]
# 被改變了對象
# fn5(c)

# 傳副本不影響
# fn5(c[:])
fn5(c.copy())
print(c, id(c))
