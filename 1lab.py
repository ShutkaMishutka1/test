import math
k = [int(s) for s in input('Введите 3 коэффициента через пробел: ').split(' ')]
d = k[1] * k[1] - 4 * k[0] * k[2]
if d < 0:
    print("Корней нет")
elif d >= 0:
    print("Корни уравнения ", (-k[1] + math.sqrt(d)) / (2 * k[0]), ' ;', (-k[1] - math.sqrt(d)) / (2 * k[0]))