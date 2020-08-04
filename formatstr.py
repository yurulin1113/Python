a = 'hello% s' % '孫悟空'

a = 'hello%s\n你好%s' % ('Davis', '孫悟空')

print(a)

print("---------------------")

b = 'hello%5s' % 'abce'  # 補空格

print(b)

print("---------------------")

c1 = 'hello%10s' % 123.1
print(c1)

c2 = 'hello%.2s' % 123.1  # %s字串符,最多幾位,無法抓小數
print(c2)

c3 = 'hello%.2f' % 123.548  # %.f小數後幾位
print(c3)

c4 = 'hello%d' % 1235.158489  # %d抓整數

print(c4)

print("---------------------")

print('x=%s' % 123456)

print("---------------------")

y1 = ",Yo"
y2 = ",Jack"

y = f'hello{y1}{y2}'

print(f'y1={y1}')

print(f'y2={y2}')

print("---------------------")

name = "孫悟空"

t1 = "歡迎"+name+"光臨"

t2 = f"歡迎{name}光臨"

t3 = "歡迎%s光臨" % name

t1_t3 = f'{t1}\n{t2}\n{t3}'

print(t1_t3)

print("歡迎", name, "光臨")

print("---------------------")

g = '123'

g = g*20

print(g)
