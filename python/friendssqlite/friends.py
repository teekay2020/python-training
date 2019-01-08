import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
#c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
#insert_query = '''INSERT INTO friends 
# 					VALUES ('Temi', 'Kazeem', 7)'''

# BAD! DO NOT DO THIS!
#form_first = "Tokunbo"
#query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# BETTER WAY!
#form_first = "Tokunbo-Kazeem"
#query = f"INSERT INTO friends (first_name) VALUES (?)"
#c.execute(query, (form_first,))

data = ("Ola", "Kazeem", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

# commit changes
conn.commit()
conn.close()
