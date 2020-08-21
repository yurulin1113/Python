print('異常前')
l = []
try:
    # print(c)
    # l[10]
    l+'hello'
    print(10/0)
# except NameError:
#     print('出現NameError')
# except ZeroDivisionError:
#     print('出現ZeroDivisionError')
# except IndexError:
#     print('出現IndexError')

# 捕捉所有異常,可以在異常跟著一個as XX(異常對象)
except Exception as e:
    print('未知異常', e, type(e))

# else有沒有都行~
else:
    print('沒有異常!')

finally:
    print('是否出現異常都會執行!')

print('異常後')
