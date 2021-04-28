import random
import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')
client = {
    "1": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "2": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "3": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "4": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "5": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "6": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "7": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "8": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "9": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "10": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "11": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5),
    "12": random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)+random.randint(2, 5)
}
list_client = list(client.items())
list_client.sort(key=lambda i: i[1])
time = datetime.timedelta(minutes=0, seconds=0)
seconds = int(list_client[0][1])
timesec = 0
wait = 0
all = 0
for i in range(0, 12):
    cassa = random.randint(5, 35)
    time = datetime.timedelta(minutes=0, seconds=seconds)
    if i != 0:
        wait = all - timesec
        if wait < 0:
            wait = 0
        all = seconds+cassa+wait
        alltime = datetime.timedelta(minutes=0, seconds=all)
    else:
        wait = 0
        all = cassa+seconds
        alltime = datetime.timedelta(minutes=0, seconds=all)

    a = str(time)[2:] + "   0 секунд      " + str(cassa) + \
        " секунд  " + str(alltime)[2:] if i == 0 else str(time)[2:] + "    " + str(wait) + " секунд" + \
        "   " + str(cassa) + " секунд  " + str(alltime)[2:]

    print(f"""# клієнта | # у черзі | Час | Тривалість | Тривалість | Час |
    {list_client[i][0]}          {i+1}       {a}   
    """)
    seconds += list_client[i+1][1]
    timesec = seconds
