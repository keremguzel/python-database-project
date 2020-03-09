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
    with connection.cursor() as cursor, open('C:\\Users\\HP\\Desktop\\CMPE351\\all_tuesday.csv', newline='') as csvfile:
        # 
        reader = csv.DictReader(csvfile, delimiter=';')
        sql = "INSERT INTO `STUDENT` (`StudentID`, `Department`, `RegType`, `RegDate`)VALUES (%s, %s, %s, %s);"
        for row in reader:
            cursor.execute(sql, (row['StudentID'], row['Department'], row['Reg.Date'], row['Reg.Type']))
            
        result = cursor.fetchall()

finally:
    connection.close()
