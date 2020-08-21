# 也可自定義異常
class MyError(Exception):
    pass


def add(a, b):
    if a < 0 or b < 0:
        # raise用於外部拋出異常
        # raise Exception('不能有負數!!')

        # 自定義異常
        raise MyError('自定義異常')

        # None也可代替異常
        # return None
    r = a+b
    return r


print(add(-1, 1))
