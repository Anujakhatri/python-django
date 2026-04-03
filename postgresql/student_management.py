import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()


class Database:

    def __init__(self):
        self.db_name = "student"
        self.user = "postgres"
        self.password = os.getenv("password")
        self.host = "localhost"
        self.port = "5432"

        self.conn = None
        self.cursor = None

        self.create_database()
        self.connect()
        self.create_table()

    # Create database if not exists
    def create_database(self):

        conn = psycopg2.connect(
            dbname="postgres",
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname=%s",
            (self.db_name,)
        )

        exists = cursor.fetchone()

        if not exists:
            cursor.execute(
                sql.SQL("CREATE DATABASE {}")
                .format(sql.Identifier(self.db_name))
            )
            print("✓ Database created")
        else:
            print("Database student already exists")

        cursor.close()
        conn.close()

    # Connect database
    def connect(self):

        self.conn = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

        self.cursor = self.conn.cursor()
        print("✓ Connected to database")

    # Create table
    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS students(
            roll_no SERIAL PRIMARY KEY,
            name VARCHAR(100),
            dob DATE,
            education VARCHAR(100),
            address TEXT
        )
        """

        self.cursor.execute(query)
        self.conn.commit()

        print("✓ Table ready")

    # Add student
    def add_student(self, name, dob, education, address):

        query = """
        INSERT INTO students(name,dob,education,address)
        VALUES(%s,%s,%s,%s)
        """

        self.cursor.execute(query, (name, dob, education, address))
        self.conn.commit()

        print("✓ Student added")

    # View students
    def view_students(self):

        self.cursor.execute("SELECT * FROM students")

        rows = self.cursor.fetchall()

        if not rows:
            print("No records found")
            return

        print("\n---- Student Records ----")

        for r in rows:
            print(f"""
Roll No : {r[0]}
Name    : {r[1]}
DOB     : {r[2]}
Edu     : {r[3]}
Address : {r[4]}
--------------------------
""")

    # Search student
    def search_student(self, roll):

        query = "SELECT * FROM students WHERE roll_no=%s"

        self.cursor.execute(query, (roll,))
        row = self.cursor.fetchone()

        if row:
            print("\nStudent Found\n")
            print(row)
        else:
            print("Student not found")

    # Update student
    def update_student(self, roll):

        print("\n1 Update Name")
        print("2 Update Education")
        print("3 Update Address")

        choice = input("Choose: ")

        if choice == "1":
            name = input("New name: ")

            query = "UPDATE students SET name=%s WHERE roll_no=%s"
            self.cursor.execute(query, (name, roll))

        elif choice == "2":
            edu = input("New education: ")

            query = "UPDATE students SET education=%s WHERE roll_no=%s"
            self.cursor.execute(query, (edu, roll))

        elif choice == "3":
            addr = input("New address: ")

            query = "UPDATE students SET address=%s WHERE roll_no=%s"
            self.cursor.execute(query, (addr, roll))

        else:
            print("Invalid option")
            return

        self.conn.commit()
        print("✓ Student updated")

    # Delete student
    def delete_student(self, roll):

        query = "DELETE FROM students WHERE roll_no=%s"

        self.cursor.execute(query, (roll,))
        self.conn.commit()

        print("✓ Student deleted")

    # Close connection
    def close(self):

        self.cursor.close()
        self.conn.close()


class StudentManagementSystem:

    def __init__(self):
        self.db = Database()

    def menu(self):

        while True:

            print("""
===============================
STUDENT MANAGEMENT SYSTEM
===============================
1 Add Student
2 View Students
3 Search Student
4 Update Student
5 Delete Student
6 Exit
""")

            choice = input("Enter choice: ")

            if choice == "1":

                name = input("Name: ")
                dob = input("DOB (YYYY-MM-DD): ")
                edu = input("Education: ")
                addr = input("Address: ")

                self.db.add_student(name, dob, edu, addr)

            elif choice == "2":
                self.db.view_students()

            elif choice == "3":
                roll = int(input("Enter roll number: "))
                self.db.search_student(roll)

            elif choice == "4":
                roll = int(input("Enter roll number: "))
                self.db.update_student(roll)

            elif choice == "5":
                roll = int(input("Enter roll number: "))
                self.db.delete_student(roll)

            elif choice == "6":
                self.db.close()
                print("Program closed")
                break

            else:
                print("Invalid choice")


def main():

    system = StudentManagementSystem()
    system.menu()


if __name__ == "__main__":
    main()