NAME: Doyinsola Sayyidah Akindele
STUDENT ID: 101192813

FILES
-----
- a4.py
- create_and_populate.sql
- README.TEXT
- recording_of_testing_.mp4: https://youtu.be/DN2um3fXk2k


DATABASE SETUP
--------------
1. Create a new database and note down the host, name of database, username and password

Right click on new databse and create QueryTool. Open the provided script - create_and_populate.sql in pgAdmin4 OR
Copy and paste the following code into your pgAdmin4 and run

-- Create the students table
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

-- Insert initial data
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


COMPILE & RUN
------------_
1. If running on Virtual Studio, simply make sure you are in the correct directory and run with the arrow in the top right corner
    Else, open a terminal in the correct directory and run with <python3 a4.py>
2. Answer prompts to connect to database
3. Choose options in the menu and provide neede information
4. If you want to exit program, choose 0

FUNCTIONS
--------
connect()
    establishes a connection to the SQL database using details

getAllStudents()
    gets all students in the database

addStudent(first_name, last_name, email, enrollment_date)
    creates new student record with given information

updateStudentEmail(student_id, new_email)
    updates student record with given email

deleteStudent(student_id)
    deletes student record with matching student id
