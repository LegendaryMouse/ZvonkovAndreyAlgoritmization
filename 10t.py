# 1
def is_triangle(a, b, c):
  if a + b > c and a + c > b and b + c > a:
        return 1
    else:
        return 0
# 2
def triangle_type(a, b, c):
  if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "РАВНОСТОРОННИЙ"
        elif a == b or a == c or b == c:
            return "РАВНОБЕДРЕННЫЙ"
        else:
            return "РАЗНОСТОРОННИЙ"
    else:
        return "НЕ ТРЕУГОЛЬНИК"
# 3
def is_leap_year(year):
    if year % 4 == 0:
        return year != 100 and year % 400 != 0
    elif year % 100 == 0:
        return year % 400 != 0
    else:
        return year % 100 != 0 and year % 400 == 0
# 4
color = input()  # Ввод цвета
a, b = map(int, input().split())  # Ввод начальной и конечной интенсивности

for i in range(a, b+1):
    if color == 'red':
        print(f'R{i}')
    elif color == 'green':
        print(f'G{i}')
    elif color == 'blue':
        print(f'B{i}')
# 5
colors = ['R', 'Y', 'B']  # Главные цвета
main_colors = set(colors)  # Уникальные главные цвета

while True:
    color = input()
    if color.upper() in main_colors:
        continue
    else:
        print(color)
        break
# 6
current_size = "ДВУСЛОЖНЫЙ"

while True:
    command = input("Введите команду: ")
    
    if command == "сложность?":
        print(current_size)
    elif command == "поменять!":
        if current_size == "ДВУСЛОЖНЫЙ":
            current_size = "ТРЕХСЛОЖНЫЙ"
        else:
            current_size = "ДВУСЛОЖНЫЙ"
    elif command == "конец!":
        break
# 7
# Изначально считаем, что размер односложный
current_size = "ОДНОСЛОЖНЫЙ"

while True:
    command = input("Введите команду: ")
    
    if command == "сложность?":
        print(current_size)
    elif command == "поменять!":
        if current_size == "ОДНОСЛОЖНЫЙ":
            current_size = "ДВУСЛОЖНЫЙ"
        elif current_size == "ДВУСЛОЖНЫЙ":
            current_size = "ТРЕХСЛОЖНЫЙ"
        elif current_size == "ТРЕХСЛОЖНЫЙ":
            current_size = "ЧЕТЫРЕХСЛОЖНЫЙ"
        else:
            current_size = "ОДНОСЛОЖНЫЙ"
    elif command == "конец!":
        break
# 8
# Изначально считаем, что размер односложный
current_size = "ОДНОСЛОЖНЫЙ"

while True:
    command = input("Введите команду: ")
    
    if command == "сложность?":
        print(current_size)
    elif command == "поменять!":
        if current_size == "ОДНОСЛОЖНЫЙ":
            current_size = "ДВУСЛОЖНЫЙ"
        elif current_size == "ДВУСЛОЖНЫЙ":
            current_size = "ТРЕХСЛОЖНЫЙ"
        elif current_size == "ТРЕХСЛОЖНЫЙ":
            current_size = "ЧЕТЫРЕХСЛОЖНЫЙ"
        else:
            current_size = "ОДНОСЛОЖНЫЙ"
    elif command == "рифма?":
        words = command.split()[1:]
        if words[0][-len(words[1]):] == words[1][-len(words[0]):]:
            print("РИФМА")
        else:
            print("НЕ РИФМА")
    elif command == "больше?":
        words = command.split()[1:]
        if words[0] > words[1]:
            print("БОЛЬШЕ")
        else:
            print("НЕ БОЛЬШЕ")
    elif command == "меньше?":
        words = command.split()[1:]
        if words[0] < words[1]:
            print("МЕНЬШЕ")
        else:
            print("НЕ МЕНЬШЕ")
    elif command == "конец!":
        break
# 9
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

number = int(input("Введите число: "))
if is_prime(number):
    print("1", number)
elif number == 1:
    print("0", number)
else:
    print("2", number)
# 10
number = input("Введите неотрицательное целое число: ")
sum = 0
for digit in number:
    sum += int(digit)
print("Сумма цифр числа:", sum)
