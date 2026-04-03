class Database:
    def __init__(self):
        print("\n Initializing Database Setup...")

        self.db_name = "anujakhatri"
        self.user = "postgres"
        self.password = ""
        self.host = "localhost"
        self.port = "5432"
        
    # Step 1: Check/Create Database
        self.create_database_if_not_exists()

    # Step 2: Connect to Database
        self.connect()

    # Step 3: Create Table
        self.create_table()     
    
     # Step 1: Check/Create Database
    def create_database_if_not_exists(self):
        print("\nStep 1: Checking database...")
    try:
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
            "SELECT 1 FROM pg_database WHERE datname = %s",
            (self.db_name,)
        )
        exists = cursor.fetchone()

        if exists:
            print(f"Database '{self.db_name}' already exists")
        else:
            
            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(self.db_name)
                )
            )
            print(f"Database '{self.db_name}' created successfully")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error while checking/creating database:", e)  
        
        
     # Step 2: Connect
    def connect(self):
        print("\n Step 2: Establishing connection...")

        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.conn.cursor()

            print(f"Connected to database '{self.db_name}' successfully")

        except Exception as e:
            print(" Connection failed:", e)   
            
    #  Step 3: Create table
    def create_table(self):
        print("\n Step 3: Checking/Creating table...")

        try:
            query = """
            CREATE TABLE IF NOT EXISTS students (
                roll_no SERIAL PRIMARY KEY,
                name VARCHAR(100),
                dob DATE,
                education VARCHAR(100),
                address TEXT
            );
            """
            self.cursor.execute(query)
            self.conn.commit()

            print(" Table 'students' is ready")

        except Exception as e:
            print(" Error creating table:", e)        
                
class Student:
    """Class to represent a student with their details"""
    
    def __init__(self, name, dob, roll_no, education, address):
        """
        Initialize a Student object
        
        Args:
            name (str): Student's name
            dob (str): Date of birth (format: DD/MM/YYYY)
            roll_no (int): Roll number
            education (str): Level of education (e.g., 10th, 12th, Bachelor's)
            address (str): Student's address
        """
        self.name = name
        self.dob = dob
        self.roll_no = roll_no
        self.education = education
        self.address = address
    
    def display(self):
        """Display student information"""
        print("\n" + "="*60)
        print(f"Name:                  {self.name}")
        print(f"Date of Birth:         {self.dob}")
        print(f"Roll Number:           {self.roll_no}")
        print(f"Level of Education:    {self.level_of_education}")
        print(f"Address:               {self.address}")
        print("="*60)
    
    def update(self):
        """Update student information"""
        print("\n--- Update Student Information ---")
        print("1. Update Name")
        print("2. Update Date of Birth")
        print("3. Update Roll Number")
        print("4. Update Level of Education")
        print("5. Update Address")
        print("6. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            self.name = input("Enter new name: ").strip()
            print("✓ Name updated successfully!")
        elif choice == '2':
            self.dob = input("Enter new date of birth (DD/MM/YYYY): ").strip()
            print("✓ Date of birth updated successfully!")
        elif choice == '3':
            try:
                self.roll_no = int(input("Enter new roll number: ").strip())
                print("✓ Roll number updated successfully!")
            except ValueError:
                print("✗ Invalid roll number! Please enter a number.")
        elif choice == '4':
            self.level_of_education = input("Enter new level of education: ").strip()
            print("✓ Level of education updated successfully!")
        elif choice == '5':
            self.address = input("Enter new address: ").strip()
            print("✓ Address updated successfully!")
        elif choice == '6':
            return
        else:
            print("✗ Invalid choice! Please try again.")
    
    def __str__(self):
        """String representation of student for display in lists"""
        return f"Roll: {self.roll_no} | Name: {self.name} | DOB: {self.dob} | Level: {self.level_of_education}"

    #  INSERT
    def insert_student(self, name, dob, education, address):
        print("\n Inserting student...")

        try:
            query = """
            INSERT INTO students (name, dob, education, address)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (name, dob, education, address)) 
            self.conn.commit()

            print(" Student added successfully")

        except Exception as e:
            print(" Insert error:", e)
            
     # SELECT
def view_students(self):
    print("\n Fetching student data...")

    try:
        self.cursor.execute("SELECT * FROM students")
        data = self.cursor.fetchall()

        if not data:
            print("️ No records found")
        else:
            print(f" {len(data)} record(s) fetched")

        return data

    except Exception as e:
        print(" Fetch error:", e)
        return []
    #  CLOSE
    def close(self):
        print("\n Closing database connection...")

        try:
            self.cursor.close()
            self.conn.close()
            print("Connection closed successfully")

        except Exception as e:
            print("Error closing connection:", e)
    Update and delete code       

class StudentManagementSystem:
    """Class to manage multiple students"""
    
    def __init__(self):
        """Initialize the Student Management System"""
        self.students = []
    
    def add_student(self):
        """Add a new student to the system"""
        print("\n--- Add New Student ---")
        try:
            name = input("Enter student name: ").strip()
            if not name:
                print("✗ Name cannot be empty!")
                return
            
            dob = input("Enter date of birth (DD/MM/YYYY): ").strip()
            if not dob:
                print("✗ Date of birth cannot be empty!")
                return
            
            roll_no = int(input("Enter roll number: ").strip())
            
            # Check if roll number already exists
            if any(student.roll_no == roll_no for student in self.students):
                print("✗ A student with this roll number already exists!")
                return
            
            level_of_education = input("Enter level of education (e.g., 10th, 12th, Bachelor's): ").strip()
            if not level_of_education:
                print("✗ Level of education cannot be empty!")
                return
            
            address = input("Enter address: ").strip()
            if not address:
                print("✗ Address cannot be empty!")
                return
            
            # Create and add new student
            student = Student(name, dob, roll_no, level_of_education, address)
            self.students.append(student)
            print(f"✓ Student '{name}' added successfully!")
            
        except ValueError:
            print("✗ Invalid input! Please enter a valid roll number (must be a number).")
    
    def view_all_students(self):
        """Display all students"""
        if not self.students:
            print("\n✗ No students in the system!")
            return
        
        print("\n" + "="*80)
        print("ALL STUDENTS")
        print("="*80)
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student}")
        print("="*80)
    
    def search_student(self):
        """Search for a student by roll number"""
        if not self.students:
            print("\n✗ No students in the system!")
            return None
        
        try:
            roll_no = int(input("\nEnter roll number to search: ").strip())
            for student in self.students:
                if student.roll_no == roll_no:
                    return student
            print(f"✗ Student with roll number {roll_no} not found!")
            return None
        except ValueError:
            print("✗ Invalid roll number! Please enter a number.")
            return None
    
    def view_student(self):
        """View details of a specific student"""
        student = self.search_student()
        if student:
            student.display()
    
    def update_student(self):
        """Update a student's information"""
        student = self.search_student()
        if student:
            student.update()
    
    def delete_student(self):
        """Delete a student from the system"""
        if not self.students:
            print("\n✗ No students in the system!")
            return
        
        student = self.search_student()
        if student:
            confirmation = input(f"\nAre you sure you want to delete '{student.name}'? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                self.students.remove(student)
                print(f"✓ Student '{student.name}' deleted successfully!")
            else:
                print("✗ Deletion cancelled!")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("    STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. View Student Details")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")
        print("="*50)
    
    def run(self):
        """Run the student management system"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.view_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("\n✓ Thank you for using Student Management System!")
                print("Goodbye!\n")
                break
            else:
                print("✗ Invalid choice! Please enter a number between 1 and 6.")


def main():
    """Main function to run the program"""
    system = StudentManagementSystem()
    system.run()


if __name__ == "__main__":
    main()