# Tested against sample input/output
number_of_inputs = int(input())
students = []


class Student:
    def __init__(self, id, name, cgpa):
        self.id = id
        self.name = name
        self.cgpa = cgpa


for _ in range(number_of_inputs):
    input_str = input("")
    inputs = input_str.split(" ")
    students.append(Student(int(inputs[0]), inputs[1], float(inputs[2])))

students.sort(key=lambda x: (-x.cgpa, x.name, x.id))

for student in students:
    print("{}".format(student.name))
