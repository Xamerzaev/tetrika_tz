import array as arr 

#вводим двоичный код (Целое число)
massiv = int(float(input('Введите двоичный код')))

#разбиваем целое число на цифры
x = [int(a) for a in str(massiv)]

#создаем массив из цифр
numbers = arr.array('i',x)

#выводим индекс первого нуля
print(numbers.index(0))