class Student:
    def __init__(self, id, name, cgpa):
        self.id, self.name, self.cgpa = id, name, cgpa

    @classmethod
    def from_input(cls, s):
        id, name, cgpa = s.split()
        return cls(int(id), name, float(cgpa))

try:
    students = [Student.from_input(input("Enter student details (id name cgpa): ")) for _ in range(int(input("Enter the number of students: ")))]

    for student in sorted(students, key=lambda x: (-x.cgpa, x.name, x.id)):
        print(student.name)

except ValueError:
    print("Invalid input!")
