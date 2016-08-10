import sqlite3
query1="SELECT SUM(area_land) from facts WHERE area_land!= \"\"";
query2="SELECT SUM(area_water) from facts WHERE area_water!= \"\"";
conn=sqlite3.connect('factbook.db');
data_land=conn.execute(query1).fetchall();
data_sea=conn.execute(query2).fetchall();

print(data_land[0][0]/data_sea[0][0]);
