
# +合併
mylist = [1, 2, 3]+[4, 5, 6]

print(mylist)

print("-"*40)

# *重複指定
print(mylist*5)

print("-"*40)

# in判斷

print('7' not in mylist)

print("-"*40)

# min,max,len

print("max=", max(mylist))
print("min=", min(mylist))
print("len=", len(mylist))

print("-"*40)

# index,count

print("index=", mylist.index(2, 1, 5))  # (查的內容,從哪裡找,結束)

print("count=", mylist.count(3))  # 內容出現幾次
