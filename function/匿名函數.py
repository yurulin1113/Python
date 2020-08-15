# filter(func,iterable)
def fn(n):
    return n % 2 == 1


newlist = list(filter(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(newlist)

# lambda作為參數使用
#print(lambda a, b: a+b)

#print((lambda a, b: a+b)(10, 20))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = list(filter(lambda i: i % 3 == 0, l))

print(r)

# map()對所有元素作指定操作
r = list(map(lambda i: i+1, l))
print(r)
