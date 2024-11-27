import connection as conn


connection = conn.create_connection()
cursor = connection.cursor()
cursor.execute("SELECT * FROM ipo;")
ipo = cursor.fetchall()
print(ipo)

cursor.close()
connection.close()