'''Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
 положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
 добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая
 ее вместимость.

Класс должен иметь следующий вид

class MoneyBox:
    def __init__(self, capacity):
    # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        # положить v монет в копилку

При создании копилки, число монет в ней равно 0.

Примечание:

Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
Решение

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return self.count + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.count += v
'''
'''Какие числа будут выведены в результате выполнения данного кода?

class A:
    def __init__(self, val=0):
        self.val = val

    def add(self, x):
        self.val += x

    def print_val(self):
        print(self.val)


a = A()
b = A(2)
c = A(4)
a.add(2)
b.add(2)

a.print_val()
b.print_val()
c.print_val()


2, 4, 4'''


class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)

'''Какие числа будут выведены в результате выполнения данного кода?

class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)



2, 3, 3'''

