student_list = list()
mentor_list = list()


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def avg_grade(self):
        total_grade = []
        for grade in self.grades.values():
            total_grade += grade
        return sum(total_grade)/len(total_grade)

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname} \nAverage grade: {self.avg_grade()} \n' \
               f'Current courses: {self.courses_in_progress} \nFinished courses: {self.finished_courses}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()
        else:
            print('Someone is not student')
            return

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() > other.avg_grade()
        else:
            print('Someone is not student')
            return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        mentor_list.append(self)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and isinstance(self, Reviewer) and course in self.courses_attached:
            if course in student.courses_in_progress or course in student.finished_courses:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        return student.grades


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_lesson(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.courses_in_progress or course in student.finished_courses:
                if course in self.grades:
                    self.grades[course] += [grade]
                else:
                    self.grades[course] = [grade]
        return self.grades

    def avg_grade(self):
        total_grade = []
        for grade in self.grades.values():
            total_grade += grade
        return sum(total_grade)/len(total_grade)

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname} \nAverage grade: {self.avg_grade()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            print('Someone is not lecturer')
        return

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() > other.avg_grade()
        else:
            print('Someone is not lecturer')
        return


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname}'


harry = Student('Harry', 'Potter', 'male')
harry.finished_courses += 'Quidditch', 'Magical animals'
harry.courses_in_progress += 'Magic', 'Potions', 'Shadow protection', 'Tricks'
harry.grades['Quidditch'] = [10, 10, 10]
harry.grades['Magical animals'] = [7, 8, 9]

hermiona = Student('Hermiona', 'Granger', 'female')
hermiona.finished_courses += 'Logic', 'Magical history'
hermiona.courses_in_progress += 'Magic', 'Potions', 'Shadow protection'
hermiona.grades['Math'] = [10, 10, 10]
hermiona.grades['Magical history'] = [8, 9, 10]

ron = Student('Ronald', 'Weasley', 'male')
ron.finished_courses += 'Magical animals', 'Magical history'
ron.courses_in_progress += 'Magic', 'Potions', 'Shadow protection'
ron.grades['Magical animals'] = [5, 6, 7]
ron.grades['Magical history'] = [4, 5, 6]

draco = Student('Draco', 'Malfoy', 'male')
draco.finished_courses += 'Quidditch'
draco.courses_in_progress += 'Magic', 'Potions', 'Shadow protection'
draco.grades['Quidditch'] = [8, 9, 10]

minerva = Lecturer('Minerva', 'Mcgonagall')
minerva.courses_attached += 'Magic', 'Shadow protection'

rubeus = Reviewer('Rubeus', 'Hagrid')
rubeus.courses_attached += 'Magical animals', 'Quidditch'

dumbledore = Reviewer('Albus', 'Dumbledore')
dumbledore.courses_attached += 'Tricks', 'Magical history'

severus = Lecturer('Severus', 'Snape')
severus.courses_attached += 'Potions', 'Logic'


Reviewer.rate_hw(dumbledore, harry, 'Tricks', 10)
Lecturer.rate_hw(rubeus, harry, 'Magical animals', 10)
#print(harry.grades)
Lecturer.rate_lesson(severus, harry, 'Potions', 10)
Lecturer.rate_lesson(severus, hermiona, 'Potions', 10)
Lecturer.rate_lesson(severus, ron, 'Potions', 7)
#print(severus.grades)
Lecturer.rate_lesson(minerva, harry, 'Magic', 10)
Lecturer.rate_lesson(minerva, hermiona, 'Magic', 10)
Lecturer.rate_lesson(minerva, ron, 'Shadow protection', 4)
#print(minerva.grades)


def avg_hw(course, some_list):
    all_rates = []
    for student in some_list:
        if course in student.grades:
            all_rates += student.grades[course]
    return sum(all_rates)/len(all_rates)


print(avg_hw('Magical history', student_list))


def avg_lesson(course, some_list):
    all_rates = []
    for mentor in some_list:
        if isinstance(mentor, Lecturer):
            if course in mentor.grades:
                all_rates += mentor.grades[course]
    return sum(all_rates)/len(all_rates)

#print(avg_lesson('Potions', mentor_list))

#print(avg_lesson('Potions',mentor_list))


#print(hermiona)
#print(severus)
#print(dumbledore)
#print(minerva)

#print(harry.avg_grade() > hermiona.avg_grade())
#print(severus.avg_grade() > minerva.avg_grade())
#print(harry > ron)
#print(ron > harry)
#print(severus.avg_grade(), minerva.avg_grade())