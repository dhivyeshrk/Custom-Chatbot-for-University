import sqlite3

conn = sqlite3.connect('Mail_Feature.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS LEVEL3 (
    NAME VARCHAR(40),
    ROLLNO VARCHAR(40),
    DESTINATION_MAIL1 VARCHAR(60),
    DESTINATION_MAIL2 VARCHAR(60),
    TYPE_OF_QUERY VARCHAR(40),
    IMAGE BLOB
)''')

# cursor.execute('DROP TABLE LEVEL3')
cursor.execute('select * from level3')
columns_info = cursor.fetchall()
print(columns_info)
