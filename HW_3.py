# №1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

arr = list(map(int, input("Ведите числа через пробел: ").split()))
print(arr)
print(sum(arr[i] for i in range(1, len(arr), 2)))

# №2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# arr = [2, 3, 4, 5, 6] #list(map(int, input().split()))
# resultArr = [arr[i] * (arr[len(arr) - 1 - i])
#              for i in range(len(arr)-1)
#              if i <= len(arr) - 1 - i]
# print(resultArr)

# №3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# arr = [1.1, 1.2, 3.1, 5, 10.01,]
# for i in arr:
#     if type(i) == int: # исключаем значения без дробей
#         arr.remove(i)
# maxNum = max(x-int(x) for x in arr)
# minNum = min(x-int(x) for x in arr)
# print(round(maxNum, 4) - round(minNum, 4))

# №4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# result = ""
# num = int(input())
# while num // 2 != 0:
#     result += str(num % 2)
#     num = num // 2
# result += str(1)
# if num == 0:
#     print(0)
# else:
#     print(result[::-1])

# №5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def NegFib(n):
#     if n == -2:
#         return -1
#     elif n == -1:
#         return 1
#     return NegFib(n + 2) - NegFib(n + 1)
#
#
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# resultArr = [NegFib(i) for i in range(-8, 0)] + [0] + [fib(i) for i in range(1, 9)]
#
# print(resultArr)
