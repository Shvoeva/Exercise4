number = float(input('\n\tВведите дробное число: '))

print('\t2 знака после запятой: {0:.2f}'.format(number))
print('\tЦелое число: {0:.0f}'.format(number))
print('\tЧисло, занимающее 11 знаков: {0:=011}'.format(number))