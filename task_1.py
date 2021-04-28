import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greating(self):
        print("Привіт, мене звати " + self.name)

    def age(self):
        self.age += 1


person = Person("Андрiй", 16)
person.greating()
print("Менi -", person.age, 'рокiв')
