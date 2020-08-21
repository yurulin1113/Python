file_name = 'file/123.txt'

try:
    # utf-8文本
    with open(file_name, encoding='utf-8') as file_obj:
        # content = file_obj.read(-1)

        # 從上次最後位置讀
        content = file_obj.read(6)

        print(content)
        print(len(content))

except FileNotFoundError:
    print(f'{file_name}文件不存在~~')
