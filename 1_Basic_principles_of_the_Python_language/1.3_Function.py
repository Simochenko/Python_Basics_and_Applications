# def function_name(argument1, argument2):
#     return argument1 + argument2
#
#
# x = function_name(2, 8)
# y = function_name(x, 21)
# print(y)

# a = []
#
# def foo(arg1, arg2):
#   a.append("foo")
#
# foo(a.append("arg1"), a.append("arg2"))
#
# print(a)

'''['arg1', 'arg2', 'foo']'''

'''В процессе выполнения кода на стек добавляются и со стека снимаются функции. Добавление функции на стек увеличивает его размер на 1, снятие функции со стека уменьшает его размер на 1.

Чему равен максимальный размер стека в процессе выполнения следующего кода?
Обратите внимание, что при интерпретации кода на стеке находится функция module, которую также нужно учесть при подсчете размера стека.
В рамках данного задания можно считать, что функция print не вызывает дополнительных функций внутри себя.

def h():
  print(12)

def f():
  g(h)

def g(a):
  a()

g(f)'''
# 6
# -----------------------
'''Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и 
возвращающую самое маленькое целое число y, такое что:

    y больше или равно x
    y делится нацело на 5

Формат того, что ожидается от вас в качестве ответа:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("
'''

# def closest_mod_5(x):
#     return x if x % 5 == 0 else closest_mod_5(x + 1)
'''Дана функция s:

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res
В результате каких вызовов данная функция вернет число 31?'''
# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
# s(5, 5, 5, 5, 1)
# s(11, 10)
# s(11, 10, b=10)
# s(21)
# s(11, b=20)

'''Сочетанием из n элементов по k называется подмножество этих n элементов размера k.

Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.

Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

Пример:

Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.

Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).

Различных сочетаний три, поэтому C(3, 2) = 3.

Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не 
выбрать. Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов 
выбрать пять.

Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула: 
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10). Ваша программа
 должна вывести единственное число: C(n, k).

Примечание:

Считать два числа n и k вы можете, например, следующим образом:

n, k = map(int, input().split())

Sample Input 1:

3 2

Sample Output 1:

3

Sample Input 2:

10 5

Sample Output 2:

252
'''

n, k = map(int, input().split())


def c(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return c(n - 1, k) + c(n - 1, k - 1)


print(c(n, k))