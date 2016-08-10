# Reading the 10 countries with the least population
import sqlite3
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
c.execute('SELECT * FROM facts order by population asc limit 10;')

print(c.fetchall());



