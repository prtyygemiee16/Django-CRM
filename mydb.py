import pymysql

#Configure PyMySQL to work with Django
pymysql.install_as_MySQLdb()

database = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    charset = 'utf8mb4'
)
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("Database created successfully")
database.close()