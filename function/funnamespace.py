a = 20
scope = locals()
#print(scope, type(scope))
# print(a)
# print(scope['a'])

scope['c'] = 1000
# print(c)

# locals()函數


def fun():
    a = 10
    scope = locals()  # 取得函數命名
    scope['b'] = 20  # 不建議
    print(scope)


# fun()

# global


def fun2():
    a = 10
    global_scope = globals()
    global_scope['a'] = 30
    print(global_scope['a'])


fun2()
