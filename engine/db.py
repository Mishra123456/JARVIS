import csv
import sqlite3
con=sqlite3.connect("jarvis.db")
cur=con.cursor()
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cur.execute(query)
query = "INSERT INTO sys_command VALUES (null,'Evernote', 'C:\\Users\\user\\AppData\\Local\\Programs\\Evernote\\Evernote.exe')"
cur.execute(query)
con.commit()
#null because id auto incremented
query = "INSERT INTO sys_command VALUES (null,'GitHub', 'C:\\Users\\user\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe')"
cur.execute(query)
con.commit()
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cur.execute(query)
query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cur.execute(query)
con.commit()
query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/')"
cur.execute(query)
con.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
desired_columns_indices = [0, 18]
# Read data from CSV and insert into SQLite table for the desired columns
with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        selected_data = [row[i] for i in desired_columns_indices]
        cur.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
con.commit()
# con.close()

# query = 'Aanjan'
# query = query.strip().lower()

# cur.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cur.fetchall()
# print(results[0][0])