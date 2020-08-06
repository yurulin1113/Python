# 質數
from time import *

begin = time()
count = 0
flag = True

for i in range(2, 101):
    for j in range(2, i):
        flag = True
        if(i % j == 0):
            flag = False
            break
    if flag:
        count += 1
        pass
        print(i)

print("總數:%d" % count)

end = time()

print("執行時間:", end-begin, "秒")
