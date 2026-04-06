import psycopg2

# connection create
conn = psycopg2.connect(
    dbname="school",
    user="anujakhatri",
    password="",
    host="localhost",
    port="5432"
)

print("Connected to database")

# create table
def create_table():
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            age INT NOT NULL,
            course VARCHAR(100)
        )
        """)
        conn.commit()
        print("Table created")

# insert data
def insert_user(name, age, course):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students(name, age, course) VALUES (%s, %s, %s)",
            (name, age, course)
        )
        conn.commit()
        print("Data inserted")

# fetch data
def fetch_users():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()

        for row in rows:
            print(row)

# update data
def update_users():
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE students SET age = %s WHERE name = %s",
            (23, "Ram")
        )
        conn.commit()

# delete data
def delete_users():
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM students WHERE name = %s",
            ("Ram",)
        )
        conn.commit()

# run functions
create_table()
insert_user("Shyam", 22, "IT")
fetch_users()

conn.close()