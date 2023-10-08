import mysql.connector

dataBase = mysql.connector.connect(
  host = "db4free.net",
  user = "azzula",
  passwd = "8Nkon1jb82uf!"
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrmdb")

print("Database created successfully")