class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        rate = 0
        c = 0
        for i in self.grades:
            rate += sum(self.grades[i])
            c += len(self.grades[i])
        rate /= c

        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(rate, 1)}" \
               f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"


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

    def __str__(self):
        rate = 0
        c = 0
        for i in self.rate:
            rate += sum(self.rate[i])
            c += len(self.rate[i])
        rate /= c

        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(rate, 1)}"


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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

review = Reviewer('Some', 'Buddy')
review.courses_attached += ['Python']

print(review)
print()

review.rate_hw(best_student, 'Python', 10)
review.rate_hw(best_student, 'Python', 10)
review.rate_hw(best_student, 'Python', 10)

lect = Lecturer('Some', 'Buddy')
lect.get_rates()

print(lect)
print()
print(best_student)

print()
print(best_student.grades)