class Person():
    def __init__(self, male, weight, toll, name, age):
        self.male, self.weight, self.toll, self.name, self.age = male, weight, toll, name, age

    def get_age(self):
        print('Цiй персонi ', self.age, 'рокiв')
