# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]
n = int(input("Введите число N: "))
listOfPrime = set()
d = 2
while d * d <= n:
    if n % d == 0:
        listOfPrime.add(d)
        n //= d
    else:
        d += 1
if n > 1:
    listOfPrime.add(n)
print(listOfPrime)
