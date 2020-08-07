emp = ["孫悟空\t24\tmale\t台中", "龜仙人\t18\tmale\t台北"]
while (True):
    print("="*10+"歡迎使用員工管理系統"+"="*10)
    print('''請選擇操作:
             1.查詢員工
             2.添加員工
             3.刪除員工
             4.退出系統\n''')

    print("*"*40)

    action = input("請選擇(1-5):")

    porfile = ["序號", "姓名", "年齡", "性別", "住址"]

    if(action == '1'):
        print("序號\t姓名\t年齡\t性別\t住址")
        if len(emp) > 0:
            n = 0
            for j in emp:
                n += 1
                print(f"{n}\t{j}")
        else:
            print("查詢不到人!")

    elif(action == '2'):
        name = input("請輸入姓名:")
        age = input("請輸入年齡:")
        gender = input("請輸入性別:")
        address = input("請輸入地址:")
        empadd = f"{name}\t{age}\t{gender}\t{address}"

        print("以下員工將加入系統中")
        print("*"*40)
        print("姓名\t年齡\t性別\t住址")
        print(empadd)
        print("*"*40)
        confirm = input("是否確認(Y/N)?")

        if(confirm == 'y'):
            emp.append(empadd)
            print("添加成功!!")
        else:
            print("添加取消!")
            pass
    elif(action == '3'):
        del_person = int(input("想刪除的員工序號:"))
        if 0 < del_person <= len(emp):
            del_i = del_person-1
            print("以下員工將移除系統中")
            print("*"*40)
            print("序號\t姓名\t年齡\t性別\t住址")
            print(f"{del_person}\t{emp[del_i]}")
            print("*"*40)
            confirm = input("是否確認(Y/N)?")
            if(confirm == 'y'):
                print(f"{del_person}\t{emp[del_i]}")
                result = emp.pop(del_i)
                print("刪除成功!!")
            else:
                print("操作取消!")
        else:
            print("您輸入錯誤!!")

    elif(action == '4'):
        print("歡迎使用!再見")
        input("Enter退出")
        break
    else:
        print("系統超出範圍!!")
