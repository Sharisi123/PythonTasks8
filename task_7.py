import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


group = ["Глiб Бразилiй", "Олександр Кушнiр",
         "Ярослав Кривошия", "Олександр Тромса"]

names = {
    "Глiб Бразилiй": datetime.datetime(2003, 5, 12),
    "Олександр Кушнiр": datetime.datetime(2003, 6, 13),
    "Ярослав Кривошия": datetime.datetime(2003, 7, 14),
    "Олександр Тромса": datetime.datetime(2004, 7, 1)
}
print("Сортування за іменем")
group.sort()
for i in range(0, len(group)):
    print("Привіт, " + group[i])

print('\n\n')

print("Сортування за прізвищем")
group.sort(key=lambda name: name.split()[::-1])

for i in range(0, len(group)):
    print("Привіт, " + group[i])


now = datetime.datetime.now()
for i in range(0, len(group)):
    birthday = datetime.datetime(
        now.year, names[group[i]].month, names[group[i]].day)
    if (birthday - now).days <= 30:  # 30 days
        print(
            f" {group[i]}, Скоро буде святкувати своє день народження ( {names[group[i]]} )")
