import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

#connect to postgresql
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="world",
        user="postgres",
        password=os.getenv("PASSWORD"),
        port="5432",
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    # cursor.execute("DROP TABLE IF EXISTS appointment;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointment(
        id SERIAL PRIMARY KEY,
        name VARCHAR NOT NULL,
        contact VARCHAR(20) NOT NULL,
        gender TEXT,
        date DATE,
        time TIME,
        reason VARCHAR(255)
      );
  """)
    conn.commit()
    cursor.close()
    conn.close()

#create an appointments for a user
def create_appointment(name, contact, gender, date, time, reason):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
       INSERT INTO appointment (name, contact, gender, date, time, reason)
       VALUES(%s, %s, %s, %s, %s, %s)
     """, (name, contact, gender, date, time, reason))
    print(name, contact, gender, date, time, reason)

    conn.commit()
    cursor.close()
    conn.close()
    print("data created successfully")


#Read a table
def read_appointments():
    conn = get_connection()
    print("test11")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM appointment")
    rows = cursor.fetchall()
    print(rows)  #print to check

    cursor.close()
    conn.close()
    return rows

#Update a appointment
def update_appointment(id, name, contact, gender, date, time, reason):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
       UPDATE appointment
       SET name = %s, contact = %s, gender=%s, date=%s, time=%s, reason=%s
       WHERE id = %s
    """, (name, contact, gender, date, time, reason, id))

    print('update appointment sucessfully')
    conn.commit()
    cursor.close()
    conn.close()


#delete user
def delete_appointment(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM appointment WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
