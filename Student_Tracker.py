# Student Grade Tracker
# Author: Nada Larabi

students = []

def add_student():
    name = input("Enter student name: ")
    grades = []
    while True:
        grade = input("Enter grade (or press Enter to stop): ")
        if grade == "":
            break
        try:
            grades.append(float(grade))
        except ValueError:
            print("Please enter a valid number.")
    students.append({"name": name, "grades": grades})
    print(f"✅ {name} added successfully!\n")

def show_students():
    if not students:
        print("No students found.\n")
        return
    print("\n--- Student List ---")
    for s in students:
        avg = sum(s["grades"]) / len(s["grades"]) if s["grades"] else 0
        print(f"{s['name']} - Grades: {s['grades']} | Average: {avg:.2f}")
    print()

def search_student():
    name = input("Enter student name to search: ")
    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            avg = sum(s["grades"]) / len(s["grades"]) if s["grades"] else 0
            print(f"✅ Found: {s['name']} - Grades: {s['grades']} | Average: {avg:.2f}\n")
            found = True
    if not found:
        print("❌ Student not found.\n")

def main():
    while True:
        print("=== Student Grade Tracker ===")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
