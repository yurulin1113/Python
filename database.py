import pymysql

# database connection
try:
    db = pymysql.connect(
        host="localhost", user="root", passwd="")

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS maxdb")

    cursor.execute("USE maxdb")

    cursor.execute("CREATE TABLE IF NOT EXISTS students")

    sql = "CREATE TABLE IF NOT EXISTS students( user_id INTEGER AUTO_INCREMENT PRIMARY Key,name VARCHAR(255),age INTEGER(10))"

    cursor.execute(sql)

    while (True):

        a = input("請輸入姓名:")
        cursor.execute("SELECT * FROM students WHERE name LIKE '%" + a + "%'")
        result = cursor.fetchall()
        for row in result:
            print("id=", row[0])
            print("name=", row[1])
            print("age=", row[2])

        key = input("繼續?(Y/N)")
        if(key == 'y'):
            continue
        else:
            break


finally:
    db.close()
    cursor.close()
    print("MySQL connection is closed")
