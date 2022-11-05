from random import randint

dividend = randint(0, 100)
divisor = randint(0, 100)

print(f'\n\t{dividend=}\n\t{divisor=}')
print(f'\tРезультат целочисленного деления: {dividend // divisor}')
print(f'\tОстаток от деления: {dividend % divisor}')