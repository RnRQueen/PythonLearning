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
