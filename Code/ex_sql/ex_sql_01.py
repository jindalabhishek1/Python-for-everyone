import sqlite3
import re

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
counter = 0
for line in fh:
    org = re.findall('^From .*@([^ ]*)', line)
    if len(org) != 1: continue
    org = org[0]
    x = cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    print (x,'********', row)
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    counter += 1
    if (counter == 9 ):
        conn.commit()
        counter = 0
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
