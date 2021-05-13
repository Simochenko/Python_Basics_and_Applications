'''Какие числа будут выведены на экран в результате выполнения данного кода?

x, y = 1, 2

def foo():
    global y
    if y == 2:
        x = 2
        y = 1

foo()
print(x)
if y == 1:
    x = 3
print(x)'''
# x, y = 1, 2
#
# def foo():
#     global y
#     if y == 2:
#         x = 2
#         y = 1
#
# foo()
# print(x)
# if y == 1:
#     x = 3
# print(x)
'''1,3'''

'''Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

    create namespace parent – создать новое пространство имен с именем namespace внутри пространства parent
    add namespace var – добавить в пространство namespace переменную var
    get namespace var – получить имя пространства, из которого будет взята переменная var при запросе из пространства namespace, или None, если такого пространства не существует

Рассмотрим набор запросов

    add global a
    create foo global
    add foo b
    create bar foo
    add bar a

Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен, созданной при выполнении данного кода

a = 0
def foo():
  b = 1
  def bar():
    a = 2

В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global. Далее мы объявляем функцию foo, что влечет за собой создание локального для нее пространства имен внутри пространства global. В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции foo функцию bar, тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.

Добавим запросы get к нашим запросам

    get foo a
    get foo c
    get bar a
    get bar b

Представим как это могло бы выглядеть в коде

a = 0
def foo():
  b = 1
  get(a)
  get(c)
  def bar():
    a = 2
    get(a)
    get(b)

Результатом запроса get будет имя пространства, из которого будет взята нужная переменная. Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a, но в пространстве global, внутри которого находится пространство foo, она объявлена. Аналогично, результатом запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.

Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве global не была объявлена переменная с.

Более формально, результатом работы get namespace var является

    namespace, если в пространстве namespace была объявлена переменная var
    get parent var – результат запроса к пространству, внутри которого было создано пространство namespace, если переменная не была объявлена
    None, если не существует parent, т. е. namespace﻿ – это global

Формат входных данных

В первой строке дано число n (1 ≤ n ≤ 100) – число запросов. В каждой из следующих n строк дано по одному запросу. Запросы 
выполняются в порядке, в котором они даны во входных данных. Имена пространства имен и имена переменных представляют и
з себя строки длины не более 10, состоящие из строчных латинских букв.

Формат выходных данных

Для каждого запроса get выведите в отдельной строке его результат.

Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
Sample Output:
global
None
bar
foo

Sample Output:

global
None
bar
foo

'''
# n = int(input())
# scopes = {'global': {'funcs': [], 'vars': []}}
#
# def add(scopes, current_namespace, what):
#     if current_namespace not in scopes:
#         scopes[current_namespace] = {}
#         scopes[current_namespace]['vars'] = []
#         scopes[current_namespace]['vars'].append(what)
#     else:
#         if 'vars' not in scopes[current_namespace]:
#             scopes[current_namespace]['vars'] = []
#             scopes[current_namespace]['vars'].append(what)
#         else:
#             scopes[current_namespace]['vars'].append(what)
#
# def create(scopes, current_namespace, parent_namespace):
#     if current_namespace not in scopes:
#         scopes[current_namespace] = {}
#         scopes[current_namespace]['funcs'] = []
#         scopes[current_namespace]['vars'] = []
#         scopes[parent_namespace]['funcs'].append(current_namespace)
#         scopes[current_namespace]['parent'] = parent_namespace
#     else:
#         if 'funcs' not in scopes[current_namespace]:
#             scopes[current_namespace]['funcs'] = []
#             scopes[current_namespace]['parent'] = parent_namespace
#             scopes[parent_namespace]['funcs'].append(current_namespace)
#         else:
#             scopes[current_namespace]['funcs'].append(current_namespace)
#             scopes[parent_namespace]['funcs'].append(current_namespace)
#
# def search(scopes, namespace, what):
#     if what in scopes[namespace]['vars']:
#         return namespace
#     else:
#         try:
#             upper_namespace = scopes[namespace]['parent']
#         except KeyError:
#             return None
#         return search(scopes, upper_namespace, what)
#
# for i in range(n):
#     command = input().split()
#     if command[0] == 'add':
#         add(scopes, command[1], command[2])
#     elif command[0] == 'create':
#         create(scopes, command[1], command[2])
#     elif command[0] == 'get':
#         print(search(scopes, command[1], command[2]))
#

# n = int(input())
#
# parent = {"global": None}
# vs = {"global": set()}
#
# for _ in range(n):
#     t, fst, snd = input().split()
#     if t == "create":
#         parent[fst] = snd
#         vs[fst] = set()
#     elif t == "add":
#         vs[fst].add(snd)
#     else:  # t == get
#         while fst is not None:
#             if snd in vs[fst]:
#                 break
#             fst = parent[fst]
#         print(fst)
#
# class A:
#     def __init__(self, val=0):
#         self.val = val
#
#     def add(self, x):
#         self.val += x
#
#     def print_val(self):
#         print(self.val)
#
#
# a = A()
# b = A(2)
# c = A(4)
# a.add(2)
# b.add(2)
#
# a.print_val()
# b.print_val()
# c.print_val()

