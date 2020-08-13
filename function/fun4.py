# 解包加*
def fn(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


t = (10, 20, 30)
t = [10, 20, 30]


fn(*t)

print("*"*40)

# 字典解包**
a = {'a': 100, 'b': 200, 'c': 300}
fn(**a)
