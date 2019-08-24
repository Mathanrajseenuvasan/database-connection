import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "testdb"
)

cursor = db.cursor()

class Emp():

    def __init__(self):
        x = int(raw_input("< 1 > Register \n< 2 > Delete\n"))
        if x == 1 :
            self.user()
        elif x == 2:
            self.delete()
        else:
            print("sorry")

    def user(self):
        self.name = raw_input("Enter name: ")
        self.age = raw_input("Enter age: ")
        cursor.execute("INSERT INTO students(name, age) VALUES (%s, %s)" , (self.name,self.age))

    def delete(self):
        
        cursor.execute("DELETE FROM students WHERE name = 'mathan')

    def update(self):

        cursor.execute("UPDATE students SET age = 20 WHERE name = 'mathan'")    


emp = Emp()   
db.commit()

# sql = "UPDATE details SET college = %s WHERE name = %s"