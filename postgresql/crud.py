# I have to create a database named school
# Create a table named students using SQL commands

import psycopg2
# from psycopg2 import sql

#connect to the database
conn = psycopg2.connect(
    dbname="school",
    user="postgres",
    password="",
    host="localhost",
    port="5432"
)
print("Connected to database successfully")
    
# create a cursor object
cursor = conn.cursor()

# create a table
def create_table():
    conn = psycopg2.connect(
        dbname="school",
        user="postgres",
        password="",
        host="localhost",
        port="5432"
    )
    
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    roll_no SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    age INT,
                    course VARCHAR(100),
                );
            """)
        print("table created succesfully")    
    
create_table() 
   
#insert data into the table
cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", ("anjila", 23, "OOP"))
conn.commit()
print("Data inserted successfully")

#Read a data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
    
#update data
cursor.execute("UPDATE students SET age = %s WHERE name = %s", (24, "Aman"))
conn.commit()
print("Data updated successfully")

#delete data
cursor.execute("DELETE FROM students WHERE name = %s", ("Aman"))
conn.commit()
print("Data deleted successfully")

#close the connection
cursor.close()
conn.close()