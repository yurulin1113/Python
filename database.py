import pymysql

# database connection
try:
    db = pymysql.connect(
        host="localhost", user="root", passwd="")

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS maxdb")

    cursor.execute("USE maxdb")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS students (user_id INTEGER AUTO_INCREMENT PRIMARY Key,name VARCHAR(255), age INTEGER(99))")
    while(True):
        option = input("請選擇(i/s):")
        print("*"*35)
        if(option == 's'):
            a = input("請輸入姓名:")
            cursor.execute(
                "SELECT * FROM students WHERE name LIKE '%" + a + "%'")
            result = cursor.fetchall()
            for row in result:
                print("id=", row[0])
                print("name=", row[1])
                print("age=", row[2])

        if(option == 'i'):
            sqlStuff = "INSERT INTO students (name, age) VALUES (%s,%s)"
            a = input("請輸入姓名:")
            b = input("請輸入年齡:")
            records = [(a, b)]
            cursor.executemany(sqlStuff, records)
            db.commit()

        key = input("請輸入(y/n)")
        if(key == 'y'):
            continue
        else:
            break
finally:
    db.close()
    cursor.close()
    print("MySQL connection is closed")
