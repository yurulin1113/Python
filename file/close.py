file_name = r'D:\Python\file\123.txt'

# open打開
file_obj = open(file_name)

content = file_obj.read()

print(content)

# close關閉
file_obj.close()

# 無法再讀取
# file_obj.read()


# with....as(開啟文件自動關閉文件)
with open(file_name) as file_obj:
    # 在這程式李直接用file_obj操作
    # 這能在with中使用~~~~
    print(file_obj.read())


# 捕獲文件異常
file_name = 'hello'

try:
    with open(file_name) as file_obj:
        print(file_obj.read())

except FileNotFoundError:
    print(f'{file_name}文件不存在~~')
