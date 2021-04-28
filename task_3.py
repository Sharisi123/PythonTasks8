import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


class Ship():
    def __init__(self, length, width, name):
        self.length = length
        self.width = width
        self.name = name

    def get_ship_info(self):
        print("Довжина корабля", self.name, self.length, "метрів")
        print("Ширина корабля", self.name, self.width, "метрів")


class Spacecraft(Ship):
    def computer(self, computer):
        self.computer = computer

    def get_ship_computer(self):
        print("Обладнання корабля", self.name, "-", self.computer)


class Starship(Spacecraft):
    def engine(self, engine):
        self.engine = engine

    def get_ship_engine(self):
        print("Двигун корабля ", self.name, "-", self.engine)


ship = Ship(80, 30, "Перемога")
spaceCraft = Spacecraft(77, 122, "Вiкторiя")
starShip = Starship(50, 66, "Дружба")

spaceCraft.computer("Lenovo")
starShip.computer("HP")
starShip.engine("v8 220 General Motors")

ship.get_ship_info()
print(" ")
spaceCraft.get_ship_info()
spaceCraft.get_ship_computer()
print(" ")
starShip.get_ship_info()
starShip.get_ship_computer()
starShip.get_ship_engine()
