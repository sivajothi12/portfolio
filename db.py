import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20),
        department VARCHAR(25)
    )
""")

cursor.execute("Insert into student (id,name,department) Values(?,?,?)",(1,"siva","CSE"))

cursor.execute("select * from student")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
