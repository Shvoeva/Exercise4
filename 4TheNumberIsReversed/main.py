from random import randint

number = randint(-1000000, 1000000)
print(f'\n\t{number=}')

#Method №1
number_abs = abs(number)

number_invert_vr1 = 0
while number_abs:
    number_invert_vr1 *= 10
    number_invert_vr1 += (number_abs % 10)
    number_abs //= 10

if number < 0:
    number_invert_vr1 *= -1

print(f'\t№1 {number_invert_vr1=}')

#Method №2
str_invert = str(abs(number))[::-1]
number_invert_vr2 = int(str_invert)

if number < 0:
    number_invert_vr2 *= -1

print(f'\t№2 {number_invert_vr2=}')