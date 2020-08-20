# import m

# print(m.a, m.b)

# m.test()
# m.test2()

# p = m.person()
# print(p.name)

# from 模組 import 變量....
# from m import person
# -------------------------------------------------------


# 引入多個...
#from m import test, person
# -------------------------------------------------------

# 引入所有(不建議)
# from m import*
# -------------------------------------------------------

# 假如不想衝突變量 from 模組 import 變量 as 其他別名....
# from m import test as new_test

# def test():
#     print('主模組test')

# test()
# new_test()

# -------------------------------------------------------

# 引用通過import*引入不會引入_c
from m import *
# print(m._c)
