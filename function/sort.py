# sort()
l = ['bb', 'aaa', 'c', 'ddddd', 'fff']

# l.sort()
# l.sort(key=len)# key-->根據長度排序
# print(l)

l = [2, 5, '1', 3, '6', '4']

# l.sort(key=int)#改類型
# print(l)


# sorted不會影響原序列
l = [2, 5, '1', 3, '6', '4']

print("排序前:", l)
print(sorted(l, key=int))
print("排序后:", l)

print('*'*40)

l = '12165498498498645649879'
print("排序前:", l)
print(sorted(l, key=int))
print("排序后:", l)
