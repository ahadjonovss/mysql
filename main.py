import mysql.connector

#Salom bu test branchdan
class Student:
    def __init__(self, name, rating, dateOfBirth):
        self.name = name
        self.rating = rating
        self.dateOfBirth = dateOfBirth


class MySQL:
    def __init__(self) -> None:
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='20058082'
        )
        self.cursor = self.db.cursor()

    def CreateDB(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS university;')
        self.cursor.execute("USE university;")

    def CreateTB(self):
        self.cursor.execute("DROP TABLE IF EXISTS students;")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                            id serial,
                            name text,
                            dateOfBirth text,
                            rating int
        );""")

    def InsertTB(self, student: Student):
        self.cursor.execute(
            "INSERT INTO students(name,dateOfBirth,rating) VALUES(%s,%s,%s);",
            (student.name, student.dateOfBirth, student.rating))
        self.db.commit()

    def readTB(self):
        self.cursor.execute(
            "select * from students;")
        print("Here is students")
        print(self.cursor.fetchall())

    def FirstQuery(self):
        self.cursor.execute("""SELECT name,count(id) FROM students group by name having count(id)>1;""")
        # print(self.cursor.fetchall())
        # print(self.cursor.fetchmany(1))
        print("Here is first query's result")
        print(self.cursor.fetchall())

    def secondQuery(self):
        self.cursor.execute("""Update students set rating = 5 where rating = 4 and dateOfBirth like  "%-02-%";""")
        self.db.commit()
        # print(self.cursor.fetchall())
        # print(self.cursor.fetchmany(1))


students_data = [
    Student("Alisher Navoi", 4, "2001-02-15"),
    Student("Temur Malik", 4, "2002-05-21"),
    Student("Nodira Begim", 4, "2000-11-30"),
    Student("Zahiriddin Babur", 5, "2003-01-12"),
    Student("Jaloliddin Manguberdi", 3, "2001-07-08"),
    Student("Ulugbek Mirzo", 5, "2002-09-17"),
    Student("Shirin Mirkarimova", 4, "2000-12-24"),
    Student("Aziza Yusupova", 3, "2003-04-03"),
    Student("Rashidov Bekzod", 4, "2002-08-19"),
    Student("Alisher Navoi", 4, "2001-02-15")
]

obj = MySQL()
for i in students_data:
    obj.InsertTB(i)
obj.secondQuery()
obj.readTB()

