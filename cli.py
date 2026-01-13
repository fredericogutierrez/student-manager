import argparse
from student_manager.manager import StudentManager
from student_manager.persistence import JSONPersistence


def main():
    parser = argparse.ArgumentParser(description="Student Manager CLI")

    parser.add_argument("--add-student", nargs=3, metavar=("NAME", "AGE", "COURSES"))
    parser.add_argument("--add-grade", nargs=2, metavar=("NAME", "GRADE"))
    parser.add_argument("--top", type=float)
    parser.add_argument("--list-course", metavar="COURSE")

    args = parser.parse_args()

    manager = StudentManager()
    persistence = JSONPersistence(manager)
    persistence.load()

    if args.add_student:
        name, age, courses = args.add_student
        manager.add_student(name, int(age), courses.split(","))

    if args.add_grade:
        name, grade = args.add_grade
        manager.add_grade(name, int(grade))

    if args.top is not None:
        print(manager.filter_top_students(args.top))

    if args.list_course:
        print(manager.list_students_by_course(args.list_course))

    persistence.save()


if __name__ == "__main__":
    main()
