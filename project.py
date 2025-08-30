#  Person Class 
class Person:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}"

# Student Class
class Student(Person):
    def __init__(self, id, name, major):
        super().__init__(id, name)
        self._major = major
        self._enrolled_course_codes = []
    def get_major(self):
        return self._major
    def set_major(self, major):
        self._major = major
    def get_enrolled_course_codes(self):
        return self._enrolled_course_codes.copy()
    def enroll_course(self, course_code):
        if course_code not in self._enrolled_course_codes:
            self._enrolled_course_codes.append(course_code)
    def drop_course(self, course_code):
        if course_code in self._enrolled_course_codes:
            self._enrolled_course_codes.remove(course_code)
    def display_details(self):
        base = super().__str__()
        return f"{base}, Major: {self._major}, Enrolled Courses: {len(self._enrolled_course_codes)}"

#  Faculty Class 
class Faculty(Person):
    def __init__(self, id, name, department):
        # Changed _init_ to __init__ for the super call
        super().__init__(id, name)
        self._department = department
        self._assigned_course_codes = []
    def get_department(self):
        return self._department
    def set_department(self, department):
        self._department = department
    def get_assigned_course_codes(self):
        return self._assigned_course_codes.copy()
    def assign_course(self, course_code):
        if course_code not in self._assigned_course_codes:
            self._assigned_course_codes.append(course_code)
    def unassign_course(self, course_code):
        if course_code in self._assigned_course_codes:
            self._assigned_course_codes.remove(course_code)
    def display_details(self):
        base = super().__str__()
        return f"{base}, Department: {self._department}, Assigned Courses: {len(self._assigned_course_codes)}"

#  Course Class 
class Course:
    def __init__(self, course_code, title, credits, prerequisites=None):
        self._course_code = course_code
        self._title = title
        self._credits = credits
        self._prerequisite_codes = prerequisites if prerequisites else []
        self._enrolled_student_ids = []
        self._assigned_faculty_id = None
    def get_course_code(self):
        return self._course_code
    def get_title(self):
        return self._title
    def get_credits(self):
        return self._credits
    def get_prerequisite_codes(self):
        return self._prerequisite_codes.copy()
    def get_enrolled_student_ids(self):
        return self._enrolled_student_ids.copy()
    def get_assigned_faculty_id(self):
        return self._assigned_faculty_id
    def set_assigned_faculty_id(self, faculty_id):
        self._assigned_faculty_id = faculty_id
    def add_prerequisite(self, prerequisite_code):
        if prerequisite_code not in self._prerequisite_codes:
            self._prerequisite_codes.append(prerequisite_code)
    def add_student_id(self, student_id):
        if student_id not in self._enrolled_student_ids:
            self._enrolled_student_ids.append(student_id)
    def remove_student_id(self, student_id):
        if student_id in self._enrolled_student_ids:
            self._enrolled_student_ids.remove(student_id)
    def assign_faculty_id(self, faculty_id):
        self._assigned_faculty_id = faculty_id
    def unassign_faculty_id(self):
        self._assigned_faculty_id = None
    def display_details(self):
        return (
            f"Course Code: {self._course_code}, Title: {self._title}, Credits: {self._credits}, "
            f"Prerequisites: {', '.join(self._prerequisite_codes)}, "
            f"Enrolled Students: {len(self._enrolled_student_ids)}, "
            f"Faculty ID: {self._assigned_faculty_id if self._assigned_faculty_id else 'None'}"
        )

#  University Class 
class University:
    def __init__(self):
        self._students = {}
        self._faculty = {}
        self._courses = {}
    def add_student(self, student):
        if student.get_id() in self._students:
            return False
        self._students[student.get_id()] = student
        return True
    def remove_student(self, student_id):
        if student_id in self._students and not self._students[student_id].get_enrolled_course_codes():
            del self._students[student_id]
            return True
        return False
    def add_faculty(self, faculty):
        if faculty.get_id() in self._faculty:
            return False
        self._faculty[faculty.get_id()] = faculty
        return True
    def remove_faculty(self, faculty_id):
        if faculty_id in self._faculty and not self._faculty[faculty_id].get_assigned_course_codes():
            del self._faculty[faculty_id]
            return True
        return False
    def add_course(self, course):
        if course.get_course_code() in self._courses:
            return False
        self._courses[course.get_course_code()] = course
        return True
    def remove_course(self, course_code):
        # This condition prevents removal if there are enrolled students, ensuring data integrity.
        if course_code in self._courses and not self._courses[course_code].get_enrolled_student_ids():
            del self._courses[course_code]
            return True
        return False
    def enroll_student_in_course(self, student_id, course_code):
        if student_id not in self._students or course_code not in self._courses:
            return False
        student = self._students[student_id]
        course = self._courses[course_code]
        # Check if student is already enrolled
        if course_code in student.get_enrolled_course_codes():
            print(f"Student {student.get_name()} (ID: {student_id}) is already enrolled in {course_code}.")
            return False
        for prereq in course.get_prerequisite_codes():
            if prereq not in student.get_enrolled_course_codes():
                print(f"Enrollment failed: Student {student.get_name()} (ID: {student_id}) has not met prerequisite: {prereq}")
                return False
        student.enroll_course(course_code)
        course.add_student_id(student_id)
        return True
    def drop_student_from_course(self, student_id, course_code):
        if student_id in self._students and course_code in self._courses:
            student = self._students[student_id]
            course = self._courses[course_code]
            if course_code in student.get_enrolled_course_codes():
                student.drop_course(course_code)
                course.remove_student_id(student_id)
                return True
        return False
    def assign_faculty_to_course(self, faculty_id, course_code):
        if faculty_id not in self._faculty or course_code not in self._courses:
            return False
        faculty = self._faculty[faculty_id]
        course = self._courses[course_code]
        if course.get_assigned_faculty_id() is not None:
            print(f"Course {course_code} already has faculty assigned.")
            return False # Course already has an assigned faculty
        faculty.assign_course(course_code)
        course.assign_faculty_id(faculty_id)
        return True
    def unassign_faculty_from_course(self, faculty_id, course_code):
        if faculty_id in self._faculty and course_code in self._courses:
            faculty = self._faculty[faculty_id]
            course = self._courses[course_code]
            if course.get_assigned_faculty_id() == faculty_id:
                faculty.unassign_course(course_code)
                course.unassign_faculty_id()
                return True
        return False
    def get_course_roster(self, course_code):
        if course_code not in self._courses:
            print(f"Course '{course_code}' not found.")
            return []
        course = self._courses[course_code]
        return [self._students[sid] for sid in course.get_enrolled_student_ids() if sid in self._students]
    def display_all_students(self):
        if not self._students:
            print("No students to display.")
            return
        print("\nAll Students")
        for s in self._students.values():
            print(s.display_details())
    def display_all_faculty(self):
        if not self._faculty:
            print("No faculty to display.")
            return
        print("\n All Faculty")
        for f in self._faculty.values():
            print(f.display_details())
    def display_all_courses(self):
        if not self._courses:
            print("No courses to display.")
            return
        print("\nAll Courses")
        for c in self._courses.values():
            print(c.display_details())

#Main Menu
def main():
    uni = University()
    while True:
        print("\n University Management Menu ")
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Drop Student from Course")
        print("6. Assign Faculty to Course")
        print("7. Unassign Faculty from Course")
        print("8. Display All Students")
        print("9. Display All Faculty")
        print("10. Display All Courses")
        print("11. Display Course Roster")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            sid = input("Student ID: ")
            name = input("Name: ")
            major = input("Major: ")
            print("Student added." if uni.add_student(Student(sid, name, major)) else "Student ID exists.")
        elif choice == '2':
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            print("Faculty added." if uni.add_faculty(Faculty(fid, name, dept)) else "Faculty ID exists.")
        elif choice == '3':
            code = input("Course Code: ")
            title = input("Title: ")
            try:
                credits = int(input("Credits: "))
            except ValueError:
                print("Invalid credits. Please enter a number.")
                continue
            prereqs_input = input("Enter prerequisite course codes (comma-separated, leave blank if none): ")
            prereqs = [p.strip() for p in prereqs_input.split(",") if p.strip()]
            print("Course added." if uni.add_course(Course(code, title, credits, prereqs)) else "Course already exists.")
        elif choice == '4':
            sid = input("Student ID: ")
            code = input("Course Code: ")
            print("Enrolled." if uni.enroll_student_in_course(sid, code) else "Enrollment failed (student/course not found, or prerequisites not met, or already enrolled).")
        elif choice == '5':
            sid = input("Student ID: ")
            code = input("Course Code: ")
            print("Dropped." if uni.drop_student_from_course(sid, code) else "Drop failed (student/course not found, or student not enrolled).")
        elif choice == '6':
            fid = input("Faculty ID: ")
            code = input("Course Code: ")
            print("Assigned." if uni.assign_faculty_to_course(fid, code) else "Assignment failed (faculty/course not found, or course already has assigned faculty).")
        elif choice == '7':
            fid = input("Faculty ID: ")
            code = input("Course Code: ")
            print("Unassigned." if uni.unassign_faculty_from_course(fid, code) else "Unassignment failed (faculty/course not found, or faculty not assigned to this course).")
        elif choice == '8':
            uni.display_all_students()
        elif choice == '9':
            uni.display_all_faculty()
        elif choice == '10':
            uni.display_all_courses()
        elif choice == '11':
            code = input("Course Code: ")
            roster = uni.get_course_roster(code)
            if roster:
                print(f"\n Roster for Course: {code} ")
                for s in roster:
                    print(s.display_details())
            else:
                print(f"No students found in course '{code}' or course does not exist.")
        elif choice == '0':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry Point
if __name__ == "__main__":
    main()
