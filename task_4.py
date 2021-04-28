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

    def get_parent_ship_info(self):
        print('Назва корабля:', self.shipName)
        print('Довжина корабля:', self.shipLength)
        print('Екiпаж корабля:', self.shipMembers)
        print('Максимальна швидкiсть корабля:', self.shipMaxSpeed)
        print('Координати корабля по Х Y:', self.x, self.y)


class BattleShip(Ship):
    def __init__(self, x=0, y=0, shipWeapon='define ship weapon', shipName='define ship name', shipLength='define ship length', shipMembers='define ship members', shipMaxSpeed='define ship speed'):
        Ship.__init__(self, x, y, shipName, shipLength,
                      shipMembers, shipMaxSpeed)
        self.shipSpecialization = 'Бойовий корабель'
        self.shipWeapon = shipWeapon

    def get_battle_ship_info(self):
        print('Спецiалiзацiя:', self.shipSpecialization)
        print('Озброення:', self.shipWeapon)


battleShip1 = BattleShip(2, 3, '20 mm Gun', 'Aврора', 175, 5, 240)
battleShip1.get_battle_ship_info()
battleShip1.get_parent_ship_info()
