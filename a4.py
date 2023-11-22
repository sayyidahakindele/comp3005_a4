import psycopg2
from psycopg2 import sql, errors

# Replace these values with your PostgreSQL connection details
DB_HOST = input("Enter the database host: ")
DB_NAME = input("Enter the database name: ")
DB_USER = input("Enter the database username: ")
DB_PASSWORD = input("Enter the database password: ")

# Function to establish a database connection
def connect():
    try:
        return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    except psycopg2.Error as e:
        print(f"Error: Unable to connect to the database. {e}")
        exit()

#Function to print all students
def getAllStudents():
    print("\n\nGetting all students")
    connection = connect()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM students;")
        students = cursor.fetchall()

        for student in students:
            print(student)
    finally:
        cursor.close()
        connection.close()

# Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    print("\n\nAdd student")
    connection = connect()
    cursor = connection.cursor()

    try:
        insert_query = sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ({}, {}, {}, {});").format(
            sql.Literal(first_name),
            sql.Literal(last_name),
            sql.Literal(email),
            sql.Literal(enrollment_date)
        )

        cursor.execute(insert_query)
        connection.commit()
        print("Student added successfully!")
    except errors.UniqueViolation as e:
        connection.rollback()
        print(f"Error: {e}")
        print("A student with the same email already exists.")
    finally:
        cursor.close()
        connection.close()

# Function to update a student's email
def updateStudentEmail(student_id, new_email):
    print("\n\nUpdating student email")
    connection = connect()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT student_id FROM students WHERE email = %s;", (new_email,))
        existing_student = cursor.fetchone()

        if existing_student:
            print(f"Error: Email '{new_email}' already belongs to another student. Update failed.")
        else:
            # Perform the update if the email is not already in use
            update_query = sql.SQL("UPDATE students SET email = {} WHERE student_id = {};").format(
                sql.Literal(new_email),
                sql.Literal(student_id)
            )

            cursor.execute(update_query)
            connection.commit()
            print("Email updated successfully!")
    except errors.NoData as e:
        connection.rollback()
        print(f"Error: {e}")
        print(f"No student found with student_id {student_id}.")
    finally:
        cursor.close()
        connection.close()

# Function to delete a student
def deleteStudent(student_id):
    print("\n\nDelete student")
    connection = connect()
    cursor = connection.cursor()

    try:
        delete_query = sql.SQL("DELETE FROM students WHERE student_id = {};").format(sql.Literal(student_id))
        cursor.execute(delete_query)
        connection.commit()
        print("Student deleted successfully!\n")
    except errors.NoData as e:
        connection.rollback()
        print(f"Error: {e}")
        print(f"No student found with student_id {student_id}.")
    finally:
        cursor.close()
        connection.close()

def main():
    connect()
    
    while True:
        print("\nOptions:")
        print("1. Print all records")
        print("2. Add a record")
        print("3. Update a record")
        print("4. Delete a record")
        print("0. Leave")

        choice = input("Enter your choice: ")

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter id: ")
            email = input("Enter new email: ")
            updateStudentEmail(student_id, email)
        elif choice == "4":
            student_id = input("Enter id: ")
            deleteStudent(student_id)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

# Run the main function
if __name__ == "__main__":
    main()