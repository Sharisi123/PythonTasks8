import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


portfolio = [("25-Jan-2018", 43.50, 25, 'CAT', 92.45),
             ("25-Jan-2018", 42.80, 50, 'DD', 51.19),
             ("25-Jan-2018", 42.10, 75, 'EK', 34.87),
             ("25-Jan-2018", 37.58, 100, 'GM', 37.58)
             ]


def get_cost_at_buy_moment(portfolio):
    count = 0
    cost = 0
    for cortage in portfolio:
        count += cortage[2]
        cost += cortage[1]
    result = cost * count
    print('Цiна на момент придбання сягала:', round(result, 2))


def get_cost_at_this_moment(portfolio):
    count = 0
    cost = 0
    for cortage in portfolio:
        count += cortage[2]
        cost += cortage[4]
    result = cost * count
    print('Цiна на даний момент сягае:', round(result, 2))


get_cost_at_buy_moment(portfolio)
get_cost_at_this_moment(portfolio)
