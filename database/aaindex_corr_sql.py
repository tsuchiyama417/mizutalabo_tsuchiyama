import sqlite3

dbname = ('aaindex.db')
conn = sqlite3.connect(dbname, isolation_level=None) 
cur = conn.cursor()

cur.execute("CREATE TABLE AAINDEX(accession_id integer, name text)")
cur.execute("CREATE TABLE AAINDEX2(accession_id integer, name text)")

sql = "INSERT INTO AAINDEX VALUES(?,?);"
data = []
count = 0
with open('d/namelist.txt') as fi: 
    for line in fi:
        data.append([count, line.replace('\n', '')])
        count += 1

fi.close()

cur.executemany(sql, data)

print(cur.execute("SELECT * FROM AAINDEX"))
print(cur.fetchall())


conn.commit()
cur.close()
conn.close() 