//**


On my laptop;

When I put the file on anaconda prompt, it looks like;

C:\Users\HP\Desktop\CMPE351\queries.sql

BUT, that should be like this;

C:/Users/HP/Desktop/CMPE351/queries.sql

That's also valids for normalization.sql file

OTHERWISE; there will be an ERROR.

On my laptop; mysql password is "student" same as school computers.


AND

For csv files, first I just wrote the file name but it didn't work. Then I change the path as;

'C:\\Users\\HP\\Desktop\\CMPE351\\all_thursday.csv'



**//



*On a python file, we connected our mysql(Acording to the root name and password). 

*Then, we named the database.Also created tables and entities in this file acording to the diagram that we drew before.

*On the next step. We get the datas from csv files for two different days.Then, instert random values to the tables.
We done that for these three tables.

*And then, we update submission date first:

1.  UPDATE SUBMISSION SET SubDate = CURRENT_TIMESTAMP - INTERVAL FLOOR(RAND() * 14) DAY;

*Then, set submission deadline:

2.  UPDATE SUBMISSION SET SubDeadline = '2017-12-01';

*Add bonus row as null:

3.  ALTER TABLE SUBMISSION ADD Bonus int(11);

*Then update bonus as 10 point:

4.  UPDATE SUBMISSION SET Bonus = 10;

*If that's uploaded before the deadline, we add 10 point:

5.  UPDATE SUBMISSION SET SubGrade = 10 WHERE SubDeadline > SubDate;

*On course grade table, set lab row with random grades:

6.  UPDATE COURSE_GRADE SET Lab = FLOOR(0 + RAND() * 100);

*On course grade table, set midterm row with random grades:

7.  UPDATE COURSE_GRADE SET Midterm = FLOOR(0 + RAND() * 100);


*On course grade table, set final row with random grades:

8. UPDATE COURSE_GRADE SET Final = FLOOR(0 + RAND() * 100);


*Add quiz attribute as null:

9.  ALTER TABLE COURSE_GRADE ADD Quiz int(11);


*Assign random values to quizes:

10.  UPDATE COURSE_GRADE SET Quiz = FLOOR(0 + RAND() * 100);


*Add overal row as null:

11.  ALTER TABLE COURSE_GRADE ADD Overall int(11);


*Calculate overall point according to midterm, final and lab points:

12.  UPDATE COURSE_GRADE inner join STUDENT on COURSE_GRADE.StudentID=STUDENT.StudentID set COURSE_GRADE.Overall=floor(((COURSE_GRADE.Midterm*25)+(COURSE_GRADE.Quiz*15)+(COURSE_GRADE.Lab*20)+(COURSE_GRADE.Final*40))/100);

