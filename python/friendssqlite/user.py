import sqlite3
conn = sqlite3.connect("users.db")
# create cursor object
c = conn.cursor()
# execute some sql
#c.execute ("CREATE TABLE users (username TEXT, password TEXT);")

people = [
	("Roald","Amundsen2020"),
	("Rosa", "Parks1000"),
	("Henry", "Hudson2000"),
	("Neil","Armstrong3000"),
	("Daniel", "Boone2100")]

#Insert all at once
c.executemany("INSERT INTO users VALUES (?,?)", people)

#c.execute(query, data)

# commit changes
conn.commit()
conn.close()
