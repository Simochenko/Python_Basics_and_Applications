# class Base:
#     def __init__(self):
#         self.val = 0
#
#     def add_one(self):
#         self.val += 1
#
#     def add_many(self, x):
#         for i in range(x):
#             self.add_one()
#
# class Derived(Base):
#     def add_one(self):
#         self.val += 10
#
#
# a = Derived()
# a.add_one()
#
# b = Derived()
# b.add_many(3)
#
# print(a.val)
# print(b.val)

# class A:
#    def foo(self):
#       print("A")
#
# class B(A):
#    pass
#
# class C(A):
#    def foo(self):
#       print("C")
#
# class D:
#    def foo(self):
#       print("D")
#
# class E(B, C, D):
#    pass
#
# E().foo()

'''Вам дано описание наследования классов в следующем формате.

имя класса 1 : имя класса 2 имя класса 3 ... имя класса k

Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:

class B(A):
    pass

Класс A является предком класса B, если

    A = B
    A - прямой предок B
    существует такой класс C, что C - прямой предок B и A - предок C

Например:

class B(A):
    pass

class C(B):
    pass

# A -- предок С

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:

Создавать классы не требуется.

Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.

Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате имя класса 1 имя класса 2.

Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не
является.

** Sample Input**:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A

Sample Output:

Yes
Yes
Yes
No
'''
# n = int(input())
#
# parents = {}
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
# q = int(input())
# for _ in range(q):
#     a, b = input().split()
#     print("Yes" if is_parent(b, a) else "No")


# classes = {}
#
# def add_class(classes, class_name, parents):
#     if class_name not in classes:
#         classes[class_name] = []
#     classes[class_name].extend(parents)
#     for parent in parents:
#         if parent not in classes:
#             classes[parent] = []
#
# def found_path(classes, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in classes:
#         return None
#     for node in classes[start]:
#         if node not in path:
#             newpath = found_path(classes, node, end, path)
#             if newpath: return newpath
#     return None
#
# def answer(classes, parent, child):
#     if not(parent or child) in classes or not found_path(classes, child, parent):
#         return 'No'
#     return 'Yes'
#
# n = int(input())
# for _ in range(n):
#     class_description = input().split()
#     class_name = class_description[0]
#     class_parents = class_description[2:]
#     add_class(classes, class_name, class_parents)
#
# q = int(input())
# for _ in range(q):
#     question = input().split()
#     parent = question[0]
#     child = question[1]
#     print(answer(classes, parent, child))

'''Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление 
элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания, умножения
 и целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1), затем снимается 
следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека кладется элемент, равный 
top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления
 (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.

Требуемая структура класса:

class ExtendedStack(list):
    def sum(self):
        # операция сложения

    def sub(self):
        # операция вычитания

    def mul(self):
        # операция умножения

    def div(self):
        # операция целочисленного деления

Примечание

Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop.

Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента.'''

#
# class ExtendedStack(list):
#    def sum(self):
#       self.append(self.pop() + self.pop())
#
#    def sub(self):
#       self.append(self.pop() - self.pop())
#
#    def mul(self):
#       self.append(self.pop() * self.pop())
#
#    def div(self):
#       self.append(self.pop() // self.pop())


# class ExtendedStack(list):
#    def sum(self):
#       top1 = self.pop()
#       top2 = self.pop()
#       self.append(top1 + top2)
#       return self
#
#    def sub(self):
#       top1 = self.pop()
#       top2 = self.pop()
#       self.append(top1 - top2)
#       return self
#
#    def mul(self):
#       top1 = self.pop()
#       top2 = self.pop()
#       self.append(top1 * top2)
#       return self
#
#    def div(self):
#       top1 = self.pop()
#       top2 = self.pop()
#       self.append(top1 // top2)
#       return self

'''Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным
 способом. Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.

Рассмотрим класс Loggable:

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение,
 добавляя при этом текущее время.

Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении 
элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.

Примечание

Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, и он 
будет содержать метод log, описанный выше.'''

# import time
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
# class LoggableList(Loggable, list):
#    def append(self, arg):
#       super(LoggableList, self).append(arg)
#       self.log(arg)


import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(list, Loggable):
   def append(self, x):
      list.append(self, x)
      self.log(x)