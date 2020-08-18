class A(object):

    # 類屬性直接在類中定義
    count = 0

    def __init__(self):
        # 實例屬性
        # 類對象無法訪問修改
        self.name = 'Roger'

    # 實例方法
    # 在類定義,以self作為第一個參數的方法都是實例方法
    # 可以通過實例和類去調用
    def test(self):
        print('這是test方法!', self)

    # 類方法
    # cls也會被自動傳遞,是當前類對象
    # 類方法和實例方法的區別,實例方法第一個參數是self,類方法是cls
    # 類方法可通過類去調用,也可以用通過實例調用
    @classmethod
    def test2(cls):
        print('這是test2()方法,是一個類方法', cls)
        print(cls.count)
        cls().test()

    # 靜態方法
    # 靜態方法不需要指定任何參數,可通過類和實例調用
    # 和當前類無關的方法
    @staticmethod
    def test3():
        print('test3執行了')


a = A()


# a.count = 10
# print('A', A.count)
# print('a', a.count)

# 兩個都改掉~~
# A.count = 100
# print('A', A.count)
# print('a', a.count)


# 類方法
# 兩個都一樣
# a.test2()
# A.test2()

# 實例方法
# 兩個都一樣
# a.test()    # 通過實例調用會自動將當前調用對象作為self傳入
# A.test(a)      # 通過類調用,不會自動傳self

# 靜態方法
# 兩個都一樣
# A.test3()
# a.test3()
