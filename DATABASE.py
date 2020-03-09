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
                             autocommit=True,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 
        
        sql = "create database `CMPE351`;"
        sql2 = "use `CMPE351`"
        sql3 = "CREATE TABLE `STUDENT` (`StudentID` int(11),`Department` varchar(255),`RegType` varchar(255),`RegDate` varchar(255),PRIMARY KEY (`StudentID`));"
        sql4 = "CREATE TABLE `SUBMISSION` (`StudentID` int(11),`AssignmentID` int(11) AUTO_INCREMENT,`SubGrade` int(11),`SubDeadline` date,`SubDate` date,UNIQUE (`AssignmentID`),KEY `FK` (`StudentID`));"
        sql5 = "CREATE TABLE `COURSE_GRADE` (`StudentID` int(11),`Midterm` int(11),`Final` int(11),`Lab` int(11),KEY `FK` (`StudentID`),PRIMARY KEY (`StudentID`));"
        cursor.execute(sql)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
            

finally:
    connection.close()
