import logging
import os

# Selected for the file properties
logging.basicConfig(filename='grades.log',level=logging.INFO, filemode='a',\
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Class to represent a student and calculate GPA
class Student:
    def __init__(self, name: str, id: int, grade: list[float], hour: list[int]):
        self.name = name
        self.id = id
        self.grade = grade
        self.hour = hour

    def calculate_gpa(self):
        logging.info(f"Calculated grade for student")
        grade_mod_hour = 0
        sum_hour = 0
        for count_grade in range(len(self.grade)):
            grade_mod_hour += self.grade[count_grade] * self.hour[count_grade]
            sum_hour += self.hour[count_grade]
        return f"{float(grade_mod_hour/sum_hour):.2f}"

# get student input
def submitting_student_data():
    logging.info(f"Starting the input student.\n")
    students = {}
    try:
        number_student = int(input("Enter the number of students: "))
        for num in range(1,number_student+1):
            name = input(f"Enter your name of the person ({num}): ")
            student_id = int(input(f"Enter your id of the person ({num}): "))
            material = int(input(f"Enter your material ({num}): "))
            list_grades = []
            list_hour = []
            while material > 0:
                grade = float(input(f"Enter your grade: "))
                if grade < 0 or grade > 4.3:
                    logging.warning(f"Grade out of range. Please enter a valid grade.")
                else:
                    hour = int(input(f"Enter your hour: "))
                    list_hour.append(hour)
                    list_grades.append(grade)
                    material -= 1
            student_data = Student(name, student_id, list_grades, list_hour)
            students.update({student_id: [student_data, student_data.calculate_gpa()]})

    except ValueError as e:
        logging.error(f"Value entered is invalid {e}. Please enter a valid number.")
        print(f"Error,because the value entered is invalid!")
    logging.info(f"Finished the input student.")
    return [number_student, students]

# Check for a file exist or not exist
def file_exist(student_data):
    num_student = student_data[0]
    data_student = student_data[1]
    logging.info(f"Checking if file exists.\n")
    # Check the exist file
    if os.path.exists("grades.txt"):
        # Open the file for the writing
        with open("grades.txt","w") as writing_file:
            logging.info(f"Open the file for the writing was successfully created")
            for student_key, student_info in data_student.items():
                writing_file.write(f"Name : {student_info[0].name}\n")
                writing_file.write(f"ID Student : {student_key}\n")
                writing_file.write(f"Grade : {student_info[0].grade}\n")
                writing_file.write(f"Hours : {student_info[0].hour}\n")
                writing_file.write(f"GPA : {student_info[1]}\n")
                writing_file.write(f"{'-'*20} \n")
        logging.info(f"Close the file for the writing was successfully closed")

        # Open the reading file
        with open("grades.txt","r") as reading_file:
            logging.info(f"Open the file for the reading was successfully created")
            read = reading_file.read()
            print(f"\nContent of the file is :\n{read}")
            logging.info(f"Reading inside the file 'grades.txt' was successfully opened")
        logging.info(f"Close the file for the reading was successfully closed")
    else:
        logging.error(f"File does not exist. Please create the file first.")

# Created function main
def main():
    student = submitting_student_data()
    file_exist(student)
    logging.info(f"End of the process!")

# Check of the if clause , (True or False)
if __name__ == "__main__":
    main()