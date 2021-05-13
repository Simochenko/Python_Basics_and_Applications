# class EvenLengthMixin:
#     def even_length(self):
#         return len(self) % 2 == 0
#
#
# class MyList(list, EvenLengthMixin):
#     pass
#
#
# ml = MyList([1, 12, 4, 17, 3])
# ml.sort()
# print(ml)

# try:
#     x = [1,2, "hello", 7]
#     x.sort()
#     print(x)
# except TypeError:
#     print("Type error :(")
# print("I can catch")

# def f(x,y):
#     try:
#         return x / y
#     except TypeError:
#         print("Type error :(")
#     except ZeroDivisionError:
#         print("Zero division :(")
# print(f(5,0))

# def f(x,y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError) as e:
#         print(type(e))
#         print(e)
#         print(e.args)
# print(f(5,0))
# print(f(5,[]))

# def f(x,y):
#     try:
#         return x / y
#     except :
#         print("Error(((")
#
# print(f(5,0))
# print(f(5,[]))

# def divide(x, y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     else: print("resul is", result)
#     finally:
#         print("Fiiiinally")
#
# divide(2,1)
# divide(2,0)
# divide(2,[])

'''Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError,
 ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")

Подсказка: https://docs.python.org/3/library/exceptions.html#exception-hierarchy'''

# try:
#     foo()
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ArithmeticError:
#     print('ArithmeticError')
# except AssertionError:
#     print('AssertionError')

'''Вам дано описание наследования классов исключений в следующем формате.

имя исключения 1 : имя исключения 2 имя исключения 3 ... имя исключения k

Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:

class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде 
будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого 
положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.

Важное примечание:

В отличие от предыдущей задачи, типы исключений не созданы.

Создавать классы исключений также не требуется

Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее
 где-то поймали их предка.

Формат входных данных

В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется 
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется 
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений. Следующие m строк содержат имена 
исключений в том порядке, в каком они были написаны у Антона в коде. Гарантируется, что никакое исключение не 
обрабатывается дважды.

Формат выходных данных

Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом
 поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

Пример теста 1

Рассмотрим код

try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")
...

По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение FileNotFoundError можно не 
ловить, ведь мы уже ловим OSError -- предок FileNotFoundError

Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
Sample Output:
FileNotFoundError
'''
# exceptions = {}
# throwed_exceptions = []
#
# def found_path(exceptions, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in exceptions:
#         return []
#     for node in exceptions[start]:
#         if node not in path:
#             newpath = found_path(exceptions, node, end, path)
#             if newpath: return newpath
#     return []
#
# n = int(input())
# for _ in range(n):
#     inpt = input().split()
#     child = inpt[0]
#     parents = inpt[2:]
#     exceptions[child] = parents
#
# m = int(input())
# for _ in range(m):
#     throwing = input()
#     for throwed_exception in throwed_exceptions:
#         if len(found_path(exceptions, throwing, throwed_exception)) > 1:
#             print(throwing)
#             break
#     throwed_exceptions.append(throwing)

# Рекурсивная функция заполняет множество всеми предками переданного ей "исключения"
# def f(query):
#     for parent in d_exceptions[query]:
#         parents.add(parent)
#         f(parent)

# Словарь со всеми "исключениями" вида {'1': [], '3': [], '5': ['1', '3'], ......}
# d_exceptions = {}

# Список с "исключениями которые хотят ловить"
# lst_query = []

# Заолняем словарь d_exceptions всеми исключениями и их предками
# for i in range(int(input())):
#     exception = input()
#     if ' : ' in exception:
#         k, v = exception.split(' : ')
#         d_exceptions[k] = v.split()
#     else:
#         d_exceptions[exception] = []

# Считываем "исключение", которое нам нужно проверить, очищаем множество parents,
# вызываем функцию f, передавая ей в качестве параметра только что считанное исключение
# Функция заполнит множество parents всеми предками, переданного ей "исключения"
# Перебираем всех предков из заполненного множества и проверяем содержатся ли они в списка "исключений"
# lst_query, Если содержатся, то печатаем считанное "исключение" и ВЫХОДИМ из цикла
# Добавляем считанное исключение в список lst_query

# for i in range(int(input())):
#     str_query = input()
#     parents = set()
#     f(str_query)
#     for parent in parents:
#         if parent in lst_query:
#             print(str_query)
#             break
#     lst_query.append(str_query)

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise  ValueError(name + " is inappropriate name")

while True:
    try:
        name = input("Plase enter your name: ")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
        break