from random import randint

number = randint(-10000000000, 10000000000)
print(f'\n\t{number=}')

#Method №1
number_abs = abs(number)
number_invert_vr1 = 0

if number.bit_length() < 32:
    while number_abs:
        number_invert_vr1 *= 10
        number_invert_vr1 += (number_abs % 10)
        number_abs //= 10

    if number < 0:
        number_invert_vr1 *= -1

print(f'\t№1 {number_invert_vr1=}')

#Method №2
number_invert_vr2 = 0

if number.bit_length() < 32:
    str_invert = str(abs(number))[::-1]
    number_invert_vr2 = int(str_invert)

    if number < 0:
        number_invert_vr2 *= -1

print(f'\t№2 {number_invert_vr2=}')