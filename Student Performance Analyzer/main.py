# Student Performance Analyzer

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


# Function to add student
def add_student():
    name = input("Enter student name: ")
    marks = []

    # Taking 3 subject marks using loop
    for i in range(3):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    # Creating dictionary
    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    # Writing to file
    with open("students.txt", "a") as file:
        file.write(str(student) + "\n")

    print("Student added successfully!\n")


# Function to display students
def display_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()
            print("\n--- Student Records ---")
            for line in data:
                print(line.strip())
    except FileNotFoundError:
        print("No student records found!")


# Function to find topper
def find_topper():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()
            topper = None
            highest = 0

            for line in data:
                student = eval(line.strip())
                if student["average"] > highest:
                    highest = student["average"]
                    topper = student

            if topper:
                print("\nTopper Details:")
                print(topper)
    except FileNotFoundError:
        print("No data found!")


# Main menu loop
while True:
    print("\n--- Student Performance Analyzer ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        find_topper()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
