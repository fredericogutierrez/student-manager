import unittest
from student_manager.manager import StudentManager


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManager()
        self.manager.add_student("Alice", 20, ["Math", "Physics"])
        self.manager.add_student("Bob", 22, ["Math"])

    def test_add_student_duplicate(self):
        result = self.manager.add_student("Alice", 25, ["Biology"])
        self.assertFalse(result)

    def test_add_grade(self):
        self.assertTrue(self.manager.add_grade("Alice", 90))
        self.assertIn(90, self.manager.records["Alice"]["grades"])

    def test_average_grade(self):
        self.manager.add_grade("Alice", 80)
        self.manager.add_grade("Alice", 100)
        self.assertEqual(self.manager.calculate_average_grade("Alice"), 90)

    def test_list_students_by_course(self):
        students = self.manager.list_students_by_course("Math")
        self.assertEqual(students, ["Alice", "Bob"])

    def test_filter_top_students(self):
        self.manager.add_grade("Alice", 95)
        self.manager.add_grade("Bob", 70)
        top = self.manager.filter_top_students(80)
        self.assertEqual(top, ["Alice"])


if __name__ == "__main__":
    unittest.main()
