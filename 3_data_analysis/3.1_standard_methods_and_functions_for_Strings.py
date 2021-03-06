'''Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв. За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s﻿.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a, либо же определить, что это невозможно.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a.

Если после применения любого числа операций в строке s останутся вхождения строки a, выведите Impossible.

Sample Input 1:

ababa
a
b

Sample Output 1:

1

Sample Input 2:

ababa
b
a

Sample Output 2:

1

Sample Input 3:

ababa
c
c

Sample Output 3:

0

Sample Input 4:

ababac
c
c

Sample Output 4:

Impossible'''

# s, a, b = (input() for _ in range(3))
#
#
# def f(s, a, b, counter=0):
#     if a in b and a in s:
#         return 'Impossible'
#     if s == s.replace(a, b):
#         return counter
#     else:
#         counter += 1
#         s = s.replace(a, b)
#         return f(s, a, b, counter)
#
#
# print(f(s, a, b))


# s = input()
# a = input()
# b = input()
#
# if a not in s:
#     print(0)
# elif a in b:
#     print("Impossible")
# else:
#     ans = 0
#     while a in s:
#         s = s.replace(a, b)
#         ans += 1
#
#     print(ans)
'''Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:

s = "abababa"
t = "aba"

Вхождения строки t в строку s:

abababa abababa abababa﻿

Sample Input 1:

abababa
aba

Sample Output 1:

3

Sample Input 2:

abababa
abc

Sample Output 2:

0

Sample Input 3:

abc
abc

Sample Output 3:

1

Sample Input 4:

aaaaa
a

Sample Output 4:

5'''
# s, t = (input() for _ in range(2))
# counter = 0
# for i in range(len(s)):
#     if s.find(t, i, i + len(t)) >= 0:
#         counter += 1
# print(counter)
# s = input()
# t = input()
# ans = 0
# for i in range(len(s)):
#     if s[i:].startswith(t):
#         ans += 1
#
# print(ans)

s = input()
t = input()

print(sum(1 for i in range(len(s)) if s.startswith(t, i)))