class StudentManager:
    def __init__(self):
        self.records = {}

    def add_student(self, name, age, courses):
        if name in self.records:
            return False

        self.records[name] = {
            "age": age,
            "grades": set(),
            "courses": set(courses)
        }
        return True

    def add_grade(self, name, grade):
        if name not in self.records:
            return False

        self.records[name]["grades"].add(grade)
        return True

    def calculate_average_grade(self, name):
        if name not in self.records:
            return None

        grades = self.records[name]["grades"]
        if not grades:
            return 0.0

        return sum(grades) / len(grades)

    def list_students_by_course(self, course):
        return [
            name for name, info in self.records.items()
            if course in info["courses"]
        ]

    def filter_top_students(self, threshold):
        return [
            name for name in self.records
            if self.calculate_average_grade(name) > threshold
        ]
