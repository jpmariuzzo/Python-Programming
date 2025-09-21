import sqlite3

conn = sqlite3.connect('emaildb_cnt.sqlite')

#Create a cursor object
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
cur.execute('DELETE FROM Counts')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1].split('@')
    #Opening a set of records to read like a file
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org[1],))
    #Get the first line
    row = cur.fetchone()

    if row is None:
        #Filling count with 1 in case of empty count
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org[1],))
    else:
        #Adding 1 to existent count
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org[1],))
    #Force to everything be written on disk - slow part
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 100'

for row in conn.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
conn.close()