file_name = 'file/123.txt'

try:
    with open(file_name, encoding='utf-8') as file_obj:

        # 保存文件
        file_content = ''
        # 指定每次讀取大小
        tmp = 100
        # 循環讀取內容
        while True:
            # 讀取大小
            content = file_obj.read(tmp)

            if not content:
                break

            # print(content, end='')

            file_content += content

except FileNotFoundError:
    print(f'{file_name}文件不存在~~')

print(file_content)
