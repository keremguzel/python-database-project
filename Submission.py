#This script connects to mysql server with given connection parameters. 
#Modify the user, password and database information to adapt to your environment. 
#Before running, make sure that you activated the cmpe351 virtual environment and installed pymysql within the environment. 

import pymysql.cursors #import cursors module of pymysql package
import csv
a=[]
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='student',
                             db='CMPE351',
                             autocommit=True,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor, open('C:\\Users\\HP\\Desktop\\CMPE351\\all_thursday.csv', newline='') as csvfile:
        # 
        reader = csv.DictReader(csvfile, delimiter=';')
        sql = "INSERT INTO `SUBMISSION` (`StudentID`)VALUES (%s);"
        for row in reader:
            cursor.execute(sql, (row['StudentID']))
            
        result = cursor.fetchall()

finally:
    connection.close()
