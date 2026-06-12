class Student:
    def __init__(self):
        self.details = {
            "first_name": None,
            "last_name": None,
            "std": None,
            "sec": None,
            "roll_no": None
        }

    def get_details(self):
        print("\n--- Enter Student Details ---")
        for key in self.details.keys():
            prompt_key = key.replace("_", " ").capitalize()
            userinput = input(f"{prompt_key}: ")
            self.details[key] = userinput


class Marksheet:
    def __init__(self):
        self.student = Student()
        self.marks = {
            "Maths": {},
            "Physics": {},
            "Chemistry": {},
            "English": {},
            "Computer_Science": {}
        }
        self.total_marks = 0
        self.average = 0.0
        self.final_grade = None

    def add_marks(self):

        self.student.get_details()


        total = 0
        print("\n--- Enter Marks ---")
        for key in self.marks.keys():
            while True:
                try:
                    userinput = int(input(f"{key}: "))
                    break
                except ValueError:
                    print("Please enter a valid numeric mark.")

            sub_grade = get_grade(userinput)
            self.marks[key]["marks"] = userinput
            self.marks[key]["grade"] = sub_grade
            total += userinput

        self.total_marks = total


        num_subjects = len(self.marks)
        self.average = total / num_subjects
        self.final_grade = get_grade(self.average)

        print("\nRecord added successfully!")

    def display_record(self):

        print("\n========================================")
        print(f" STUDENT REPORT CARD: {self.student.details['first_name']} {self.student.details['last_name']}")
        print(
            f" Roll No: {self.student.details['roll_no']} | Class: {self.student.details['std']}-{self.student.details['sec']}")
        print("----------------------------------------")
        for subject, data in self.marks.items():
            print(f" {subject.replace('_', ' '):<18} : {data['marks']} (Grade: {data['grade']})")
        print("----------------------------------------")
        print(f" TOTAL MARKS         : {self.total_marks}")
        print(f" AVERAGE SCORE       : {self.average:.2f}%")
        print(f" FINAL OVERALL GRADE : {self.final_grade}")
        print("========================================")


def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


database = []

while True:
    print("\n===== STUDENT DATABASE MENU =====")
    print("1. Add New Student Record")
    print("2. View All Student Records")
    print("3. View Specific Student (by Roll No)")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        record = Marksheet()
        record.add_marks()
        database.append(record)

    elif choice == '2':
        if not database:
            print("\nNo records found in the database.")
        else:
            for record in database:
                record.display_record()

    elif choice == '3':
        if not database:
            print("\nNo records found in the database.")
        else:
            search_roll = input("\nEnter Roll Number to search: ")
            found = False
            for record in database:
                if record.student.details['roll_no'] == search_roll:
                    record.display_record()
                    found = True
                    break
            if not found:
                print(f"\nStudent with Roll No '{search_roll}' not found.")

    elif choice == '4':
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please select between 1 and 4.")
