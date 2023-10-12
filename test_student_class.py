import unittest
from io import StringIO
import sys

class Student:
    def __init__(self, id, name, cgpa):
        self.id, self.name, self.cgpa = id, name, cgpa

    @classmethod
    def from_input(cls, s):
        id, name, cgpa = s.split()
        return cls(int(id), name, float(cgpa))

class TestStudent(unittest.TestCase):

    def test_initialization(self):
        student = Student(1, "John", 8.5)
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "John")
        self.assertEqual(student.cgpa, 8.5)

    def test_from_input_valid(self):
        student = Student.from_input("1 John 8.5")
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "John")
        self.assertEqual(student.cgpa, 8.5)

    def test_from_input_invalid_format(self):
        with self.assertRaises(ValueError):
            Student.from_input("1 John")

    def test_from_input_invalid_types(self):
        with self.assertRaises(ValueError):
            Student.from_input("John 1 8.5")

    def test_sorted_students(self):
        students_input = ["1 Alice 8.5", "2 Bob 9.0", "3 Charlie 8.5"]
        students = [Student.from_input(data) for data in students_input]
        sorted_students = sorted(students, key=lambda x: (-x.cgpa, x.name, x.id))
        self.assertEqual([student.name for student in sorted_students], ["Bob", "Alice", "Charlie"])

    def test_input_output_flow(self):
        # Simulate user input
        input_data = "3\n1 Alice 8.5\n2 Bob 9.0\n3 Charlie 8.5\n"
        sys.stdin = StringIO(input_data)

        output_data = StringIO()
        sys.stdout = output_data

        try:
            students = [Student.from_input(input("Enter student details (id name cgpa): ")) for _ in range(int(input("Enter the number of students: ")))]

            for student in sorted(students, key=lambda x: (-x.cgpa, x.name, x.id)):
                print(student.name)

        except ValueError:
            print("Invalid input!")

        expected_output = (
        "Enter the number of students: "
        "Enter student details (id name cgpa): "
        "Enter student details (id name cgpa): "
        "Enter student details (id name cgpa): "
        "Bob\nAlice\nCharlie\n"
)
        self.assertEqual(output_data.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
