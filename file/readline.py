import pprint

file_name = 'file/123.txt'
with open(file_name, encoding='utf-8') as file_obj:
    # readline()讀取一行內容
    # print(file_obj.readline(), end='')
    # print(file_obj.readline(), end='')

    # readlines()
    # 一行一行讀取,封裝到一個列表
    # r = file_obj.readlines()
    # pprint.pprint(r[0])
    # pprint.pprint(r[1])
    # pprint.pprint(r[2])

    for t in file_obj:
        print(t, end='')
