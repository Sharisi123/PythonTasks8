import random
import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


class Coloda():
    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
        self.coloda = []
        self.playerCards = []

    def connect(self):
        for i in range(0, len(self.suits)):
            for j in range(0, len(self.values)):
                card = values[j] + suits[i]
                self.coloda.append(card)
        return self.coloda

    def shuffle(self, coloda):
        lastIndex = len(self.coloda)-1
        while lastIndex > 0:
            randomIndex = random.randint(0, lastIndex)
            last = self.coloda[lastIndex]
            self.coloda[lastIndex] = self.coloda[randomIndex]
            self.coloda[randomIndex] = last
            lastIndex -= 1

    def get_result(self):
        print('Не тасована колода: ', self.coloda)
        self.shuffle(self.coloda)
        print('Перетасована колода: ', self.coloda)

    def cardDispenser(self, shuffledCards):
        countOfPeople = input('Введіть кількість гравців: ')
        countOfCardPerPlayer = input(
            'Введіть кількість карт на одного гравця: ')

        if(int(countOfPeople) * int(countOfCardPerPlayer) > len(shuffledCards)):
            print('Карт на всіх не вистачить')
            return 0

        for i in range(0, int(countOfPeople)):
            self.playerCards = []
            for j in range(0, int(countOfCardPerPlayer)):
                self.playerCards.append(shuffledCards[j])
                shuffledCards.remove(shuffledCards[j])
            print('Карти гравця номер: ', i+1)
            print(self.playerCards)


suits = ["s", "d", "c", "h"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

card = Coloda(suits, values)
card.connect()
card.get_result()
card.cardDispenser(card.connect())
