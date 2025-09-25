
# Project Title

This project is written in Python. It collects student data (name, ID, grades, and credit hours) and calculates the GPA. The program also saves the results in a text file (grades.txt) and logs the process in (grades.log).

## Features

- Calculate GPA for one or more students
- Check if grades are valid (between 0 and 4.3)
- Save results into a text file
- Log steps, warnings, and errors

## How to Run

python main.py
    
## Usage/Examples

Enter the number of students: 1
Enter your name of the person (1): Ahmad
Enter your id of the person (1): 2001
Enter your material (1): 2
Enter your grade: 3.5
Enter your hour: 3
Enter your grade: 4.0
Enter your hour: 2


The program will create a grades.txt file with something like this:

Name : Ahmad
ID Student : 2001
Grade : [3.5, 4.0]
Hours : [3, 2]
GPA : 3.70
--------------------
