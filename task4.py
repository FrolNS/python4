# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.(записать в строку)

# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5
import sympy
from random import randint


def generatePol(k):
    pol = ''
    for i in range(k, -1, -1):
        pol += f'{randint(0, 10)}*x**{i}+'
        if i == 0:
            pol += f'{randint(0, 10)}'
    return pol


k = int(input("Введите натуральную степень: "))

polinom1 = generatePol(k)
pol1 = str(sympy.simplify(polinom1))
print(pol1)
polinom2 = generatePol(k)
pol2 = str(sympy.simplify(polinom2))
print(pol2)

with open('file1.txt', 'w+') as f1:
    f1.write(pol1)

with open('file2.txt', 'w+') as f2:
    f2.write(pol2)
