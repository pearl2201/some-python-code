import sqlite3
conn = sqlite3.connect('user.db')

c = conn.cursor()


# Create table
#c.execute('''CREATE TABLE scores
             #(id INTEGER PRIMARY KEY AUTOINCREMENT, iduser text, score INTEGER)''')

# Insert a row of data
c.execute("INSERT INTO scores(iduser,score) VALUES ('PEARL',20)")
#c.execute("INSERT INTO scores VALUES (2,'SHARK',30)")
#c.execute("INSERT INTO scores VALUES (3,'NGOC',10)")

#for row in c.execute("select  p1.*, (select  count(*) from scores as p2   where   p2.score > p1.score ) as rank from scores as p1 "):
#    print (row)

#for row in c.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 50"):
#   print (row)
#for i in range(4,50):
 #   c.execute("INSERT INTO scores VALUES (?,?,?)",(i,"id" + str(i),i))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()