def fn():
    a = 1401

    def fn2():
        print("I'm fn2()", a)
    return fn2


print(fn())

# r是一個函數調用fn返回的函數
r = fn()
r()

# 求平均
#nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(sum(nums)/len(nums))


def makeave():
    nums = []

    def ave(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return ave


ave = makeave()

print(ave(10))
print(ave(20))
print(ave(30))
nums = [1, 2, 3, 4, 5]  # 沒影響函數
print(ave(40))
print(ave(50))
