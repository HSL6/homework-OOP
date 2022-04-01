class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        self.rate = {}

    def get_rates(self):
        self.rate = best_student.grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

review = Reviewer('Some', 'Buddy')
review.courses_attached += ['Python']

review.rate_hw(best_student, 'Python', 10)
review.rate_hw(best_student, 'Python', 10)
review.rate_hw(best_student, 'Python', 10)

lect = Lecturer('Some', 'Buddy')
lect.get_rates()

print(best_student.grades)
