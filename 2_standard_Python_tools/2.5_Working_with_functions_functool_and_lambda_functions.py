# x = input().split()
# xs = (int(i) for i in x)
#
#
# def even(x):
#     return x % 2 == 0
#
#
# evens = list(filter(even, xs))
# for i in evens:
#     print(i)

# x = [
#     ("Guido", "van", "Rossum"),
#     ("Haskell", "Curry"),
#     ("John", "Backus")
# ]
#
# x.sort(key=lambda name: len(" ".join(name)))
# print(x)
# print(op.add(4, 5))
# print(op.mul(4, 5))
# print(op.contains([1, 2, 3], 4))  # 4 in [1, 2, 3]

# x = [1, 2, 3]
# y = {"123": 3}
# f = op.itemgetter(1)
# print(f(x))
# f = op.itemgetter("123")
# print(f(y))

# f = op.attrgetter("sort")
# print(f([]))

# x = [
#     ("Guido", "van", "Rossum"),
#     ("Haskell", "Curry"),
#     ("John", "Backus")
# ]


# import operator as op
# x.sort(key=op.itemgetter(-1))
# print(x)

# import operator as op
# from functools import partial
#
# sort_by_last = partial(list.sort, key=op.itemgetter(-1))
# print(x)
# sort_by_last(x)
# print(x)
class RandomIterator:
    """
    Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте». Но иногда, когда нужно создавать
     много однотипных лямбда функций, еще удобнее будет создать функцию, которая будет их генерировать.

    Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, которая
    будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

    Пример использования:

    mod_3 = mod_checker(3)
    print(mod_3(3)) # True
    print(mod_3(4)) # False

    mod_3_1 = mod_checker(3, 1)
    print(mod_3_1(4)) # True
    """


# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod


print(RandomIterator.__doc__)
