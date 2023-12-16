import mysql.connector

try:
    # veritabani = mysql.connector.connect(host="localhost",user = "root",password = "1234")
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )
    print("bağlantı tamam!")
    print(myDb)
    try:
        myCursor = myDb.cursor()
        myCursor.execute("CREATE DATABASE pythondersleri")
        print("veritabanı oluşturuldu")
    except:
        print("veritabanı oluşurken bir hata oluştu.")
except: 
    print("bağlantı başarısız.")