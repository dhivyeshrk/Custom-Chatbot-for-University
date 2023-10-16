import sqlite3

conn = sqlite3.connect('Mail_Feature.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS LEVEL2 (
    ROLLNO VARCHAR(40),
    PASSWORD VARCHAR(40)
)''')


cursor.execute("INSERT INTO LEVEL2 VALUES('CS84', 'MT329')")
cursor.execute("INSERT INTO LEVEL2 VALUES('CS28', 'MT500')")
conn.commit()
cursor.execute('select * from level2')
a = cursor.fetchall()
print(a)
#%%
