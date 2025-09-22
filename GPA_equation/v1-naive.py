# Ticket #701
class student:
    def __init__(self,name,id,grades):
        self.name = name
        self.id = id
        self.grades = grades
    def GPA(self):
        return sum(self.grades)/len(self.grades)

# Ticket #702
f = open("grades.txt", "r")
data = f.read()
print(data)

# Ticket #703
students = [("Ali", 101), ("Sara", 102), ("Omar", 103)]
print(students[1000])

# Ticket #704
with open("grades.txt","w") as f:
    f.write("Ali, A")

# Ticket #705
class stu: pass
def gpA(x): return sum(x)/len(x) 