from datetime import datetime
import sqlite3
import MySQLdb
from mysql.connector import Error 
from datetime import date
import mysql.connector

DB_CONFIG = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'crawlerdb',
}
# create a connection to your database
conn = mysql.connector.connect(**DB_CONFIG)

# create a cursor object
cur = conn.cursor()

# define the INSERT statement as a string
insert_query = "insert into navernews(keyword,title,content,link,date) values ('압사','이태원', '누군가의 마지막 장소가 된 밤 압사','temp_content','http://templocal.com','2022-10-29')"


# use a for loop to execute the INSERT statement 1000 times
for i in range(100):
    cur.execute(insert_query)

# commit the changes to the database
conn.commit()

# close the cursor and connection objects
cur.close()
conn.close()
