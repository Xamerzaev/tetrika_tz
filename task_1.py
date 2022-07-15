import array as arr 

massiv = int(float(input('Введите двоичный код')))

x = [int(a) for a in str(massiv)]

numbers = arr.array('i',x)

print(numbers.index(0))