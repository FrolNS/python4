# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy


with open('file1.txt', 'r') as r1:
    pol1 = r1.readline()
print(pol1)
with open('file2.txt', 'r') as r2:
    pol2 = r2.readline()
print(pol2)
pol3 = sympy.simplify(pol1 + '+' + pol2)
print(pol3)
