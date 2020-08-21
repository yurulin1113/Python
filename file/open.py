# file_name = 'file/123.txt'

# r絕對路徑
file_name = r'D:\Python\file\123.txt'

# open打開
file_obj = open(file_name)

print(file_obj)

content = file_obj.read()

print(content)
