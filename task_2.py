import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


class Ship():

    def __init__(self, x=0, y=0, shipName='define ship name', shipLength='define ship length', shipMembers='define ship members', shipMaxSpeed='define ship speed'):
        self.x = x
        self.y = y
        self.shipName = shipName
        self.shipLength = shipLength
        self.shipMembers = shipMembers
        self.shipMaxSpeed = shipMaxSpeed

    def get_info(self):
        print('Назва корабля: ', self.shipName)
        print('Довжина корпусу корабля: ', self.shipLength)
        print('Кiлькiсть екiпажу корабля: ', self.shipMembers)
        print('Максимальна швидкiсть корабля: ', self.shipMaxSpeed)

    def move_up(self):
        self.y += 1
        print('Координата по y: ', self.y)

    def calc_distance(self, x1, x2, y1, y2):
        print('Дистанцiя мiж кораблями по Х:', x1 - x2)
        print('Дистанцiя мiж кораблями по Y:', y1 - y2)


ship1 = Ship(1, 1, "Аврора", 175, 5, 210)
ship2 = Ship(2, 2)
ship3 = Ship(3, 3)
ship4 = Ship(4, 4)
ship5 = Ship(5, 5)
ship6 = Ship(6, 6)

ship1.get_info()
ship1.calc_distance(ship1.x, ship2.x, ship1.y, ship2.y)
