print ("hello, world!")
s = []
s.append(12.5)
print(s)
x = 5
print(3 < x < 7)


y = True
print(not y)


x, y, z = True, False, True
result = x and y or (not z)
print(result)

year = 2020
is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
print(is_leap)

import calendar
print(calendar.isleap(2012))


quote = '"Дайте мне точку опоры, и я переверну мир!"'
print(quote.count("е"))
print("мир".capitalize())

print("1a1".isdigit())

print("я переверну" in "Дайте мне точку опоры, и я переверну мир!")

new_string = "Python"
for letter in new_string:
    print("Letter", letter)

template = " И %s такой молодой, и юный %s впереди"
print(template % ("Ленин", "октябрь"))
print("Давайте {} паузы в {}, произнося и {} снова".format("делать", "словах", "замолкая"))

subject = "елочка"
action = "росла"
print(f"В лесу родилась {subject}, в лесу она {action}")

num = 6/7
print(num)
print(f"{num:.2f}")

#name = input("Input your name:")
#print(f"Hello, {name}!")

company = "yandex.ru"

if "Яндекс" in company:
    print("Подстрока ya найдена")
elif "yandex" in company:
    print("Подстрока yandex найдена")
else:
    print("Подстрока не найдена")

name = "Dmitry"
for letter in name:
    print(letter)

sum = 0
for i in range(101):
    sum += i
print(sum)

for i in range(0,11,2):
    print(i)


for i in range(10,-1,-2):
    print(i)