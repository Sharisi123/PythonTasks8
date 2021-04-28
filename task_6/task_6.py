import student
import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


class Course():
    def __init__(self, name, studyCredit, profesors, endStart):
        self.name, self.studyCredit, self.profesors, self.endStart = name, studyCredit, profesors, endStart

    def get_info(self):
        print('Назва курсу:', self.name)
        print('Кількість навчальних кредитів:', self.studyCredit)
        print('Викладачi курсу:', self.profesors)
        print('Розклад:', self.endStart)


class Pulpit():
    def __init__(self, name, profesors, courseNames, credits, endStart):
        self.name = name
        self.profesors = profesors
        self.courses = []

        for i in range(0, 2):
            self.courses.append(
                Course(courseNames[i], credits[i], profesors[i], endStart[i]))

    def pulputCourses(self):
        print('Список курсiв данноi кафедри:')
        for course in self.courses:
            print(course.get_info())


petro = student.Student('Man', 70, 175, 'Petro', 16, 'ЧДБК', 2, 2019, 100)
petro.get_age()

programingPulpit = Pulpit('Кафедра програмування', [['A.Н.Антоненко, Б.Г.Раунд'], [
                          'Ф.Ф.Феофiлов']], ['Програмування', 'Ремонт ПК'], [4, 4], ['10:00-11:20', '8:30-9:50'])
programingPulpit.pulputCourses()
