file_name = 'file/456.txt'

# w不存在文件會創建,若存在會覆蓋所有內容
# a不存在文件會創建,若存在會追加內容
# +為操作符增加功能
# r+文件不存在會報錯
# w+
# a+
with open(file_name, 'r+', encoding='utf-8') as file_obj:

    # 只能用字串
    file_obj.write('aaa\n')
    file_obj.write('bbb\n')
    file_obj.write('ccc\n')

    # 該方法會返回字數~~
    r = file_obj.write(str(123)+'123123\n')
    r = file_obj.write('今天真好')
    print(r)
