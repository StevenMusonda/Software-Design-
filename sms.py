class Student:
    """Represents a student with an ID, name, age, and major."""

    def __init__(self, student_id, name, age, major):
        self.student_id = student_id  # Unique identifier for the student
        self.name = name  # Name of the student
        self.age = age  # Age of the student
        self.major = major  # Student's major field of study

    def update_info(self, name=None, age=None, major=None):
        """Update student information."""
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if major is not None:
            self.major = major

    def display(self):
        """Display student information in a readable format."""
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")


class StudentDatabase:
    """Manages a collection of students."""

    def __init__(self):
        self.students = {}  # Dictionary to store students with their ID as the key

    def add_student(self, student):
        """Add a student to the database."""
        if student.student_id in self.students:
            print("Student with this ID already exists.")
        else:
            self.students[student.student_id] = student

    def remove_student(self, student_id):
        """Remove a student from the database using their ID."""
        if student_id in self.students:
            del self.students[student_id]
        else:
            print("Student not found.")

    def get_student(self, student_id):
        """Retrieve a student by their ID."""
        return self.students.get(student_id, None)

    def display_all_students(self):
        """Display all students in the database."""
        if not self.students:
            print("No students to display.")
        else:
            for student in self.students.values():
                student.display()


class StudentManagementSystem:
    """Interface for managing student-related operations."""

    def __init__(self):
        self.database = StudentDatabase()  # Initialize the student database

    def add_new_student(self):
        """Prompt user for details and add a new student."""
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")
        student = Student(student_id, name, age, major)
        self.database.add_student(student)

    def delete_student(self):
        """Prompt user for student ID to delete."""
        student_id = input("Enter student ID to delete: ")
        self.database.remove_student(student_id)

    def update_student_info(self):
        """Prompt user for student ID to update and modify their information."""
        student_id = input("Enter student ID to update: ")
        student = self.database.get_student(student_id)
        if student:
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            major = input("Enter new major (leave blank to keep current): ")
            student.update_info(
                name=name if name else None,
                age=int(age) if age else None,
                major=major if major else None
            )
        else:
            print("Student not found.")

    def show_all_students(self):
        """Display all students in the database."""
        self.database.display_all_students()

    def run(self):
        """Start the menu-driven program for student management."""
        while True:
            print("\n1. Add Student")
            print("2. Delete Student")
            print("3. Update Student Info")
            print("4. Show All Students")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_new_student()
            elif choice == "2":
                self.delete_student()
            elif choice == "3":
                self.update_student_info()
            elif choice == "4":
                self.show_all_students()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Entry point of the program
    system = StudentManagementSystem()
    system.run()
