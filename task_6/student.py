import person


class Student(person.Person):
    def __init__(self, male, w, t, n, a, study, currentCurse, yearOfStartStudy, avarageMark):
        person.Person.__init__(self, male, w, t, n, a)
        self.study, self.currentCurse, self.yearOfStartStudy, self.avarageMark = study, currentCurse, yearOfStartStudy, avarageMark

    def get_study(self):
        print('Цей студент навчаеться в', self.study)
