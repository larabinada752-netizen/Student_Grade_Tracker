# Student_Grade_Tracker
A simple Python program to manage student grades. Add students, record their grades, view all students, and search for individual students with their average grades.

Features :

Add a student with multiple grades.

Display all students with their grades and average.

Search for a student by name (case-insensitive).

User-friendly menu with error handling.

Handles empty grade lists gracefully.

# Requirements

Python 3.7+

No external libraries needed

# How to Run
1 Download or clone the repository

2 Open terminal in the project folder

3 Run the script:
python student_grade_tracker.py

4 Follow the interactive menu:

1 → Add a student

2 → Show all students

3 → Search for a student

4 → Exit the program

![Run 1](https://github.com/larabinada752-netizen/Student_Grade_Tracker/blob/855ee11464e83053b3c942feaddbd8aedb0729f1/run_1.png.jpeg?raw=true)

# Example Output
=== Student Grade Tracker ===
1. Add Student
2. Show Students
3. Search Student
4. Exit
Choose an option: 1
Enter student name: Alice
Enter grade (or press Enter to stop): 90
Enter grade (or press Enter to stop): 85
Enter grade (or press Enter to stop): 92
Enter grade (or press Enter to stop): 
✅ Alice added successfully!

=== Student Grade Tracker ===
1. Add Student
2. Show Students
3. Search Student
4. Exit
Choose an option: 2

--- Student List ---
Alice - Grades: [90.0, 85.0, 92.0] | Average: 89.00

# Tips
Grades can be entered as floating point numbers.

Leave the grade input blank to stop adding grades for a student.

The program keeps data in memory only (not saved to a file).
