class GradeSystem:
    def __init__(self):
        self.grades = {}

    def add_grade(self, name, grade):
        self.grades[name] = grade
        print(f"Added: {name} - {grade:.2f}")

    def view_grades(self):
        if not self.grades:
            print("No grades available!")
        else:
            print("\nStudent Grades:")
            for name, grade in self.grades.items():
                print(f"{name}: {grade:.2f}")

    def calculate_average(self):
        if not self.grades:
            print("No grades available!")
        else:
            avg = sum(self.grades.values()) / len(self.grades)
            print(f"Class Average: {avg:.2f}")

def main():
    system = GradeSystem()
    while True:
        print("\n1. Add Grade\n2. View Grades\n3. Calculate Average\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter grade: "))
                if 0 <= grade <= 100:
                    system.add_grade(name, grade)
                else:
                    print("Invalid grade! Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric grade.")
        elif choice == "2":
            system.view_grades()
        elif choice == "3":
            system.calculate_average()
        elif choice == "4":
            print("Exiting Grade System.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
main()
