l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fn2(i):
    if i % 2 == 0:
        return True
    return False


def fn3(i):
    if i > 5:
        return True
    return False


def fn(func, lst):
    new_lst = []

    for i in lst:
        if(func(i)):
            new_lst.append(i)
    return new_lst


def fn4(i):
    if i % 3 == 0:
        return True
    return False


print(fn(fn2, l))
print(fn(fn3, l))
print(fn(fn4, l))
