# pattern = r"a.c"
# string = "acc"
# match_object = re.match(pattern, string)
# print(match_object)
#
# string = "abc, a.c, aac, a-c,aBc,azc"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)
#
# fixed_typos = re.sub(pattern, "abc", string)
# print(fixed_typos)

# pattern = r"ab*a"
# pattern = r"ab+a"
# pattern = r"ab?a"
# pattern = r"ab{2}a"
# string = "aa, aba, abba"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)


"""Вам дана последовательность строк.

Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:

Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line

Sample Input:

catcat
cat and cat
catac
cat
ccaatt

Sample Output:

catcat
cat and cat
"""
# import re
# import sys
# pattern = r'((cat).*){2,}'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)

'''Вам дана последовательность строк.

Выведите строки, содержащие "cat" в качестве слова.

Примечание:

Для работы со словами используйте группы символов \b и \B. Описание этих групп вы можете найти в документации.

Sample Input:

cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:

cat
catapult and cat
"cat"
!cat?
'''

# import re
# import sys
# pattern = r'\bcat\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)

'''Вам дана последовательность строк.

Выведите строки, содержащие две буквы "z?", между которыми ровно три символа.

Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:

zabcz
zzxzz
'''
# import re
# import sys
# pattern = r'(z.{3}z)'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)

'''Вам дана последовательность строк.

Выведите строки, содержащие обратный слеш "**\**".

Sample Input:

\w denotes word character
No slashes here

Sample Output:

\w denotes word character'''

# import re
# import sys
# pattern = r'.*\\.*'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)


'''Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa
Sample Output:

blabla is a tandem repetition
123123 is good too'''

# import re
# import sys
# pattern = r'\b(.+)\1\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line):
#         print(line)

'''Вам дана последовательность строк.

В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

Sample Input:

I need to understand the human mind
humanity

Sample Output:

I need to understand the computer mind
computerity
'''
# import re
# import sys
#
# pattern = r'human'
#
# for line in sys.stdin:
#     print(re.sub(pattern, 'computer', line.rstrip()))


'''Вам дана последовательность строк.

В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на
 слово "argh".

Примечание:

Обратите внимание на параметр count у функции sub.

Sample Input:

There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA

Sample Output:

There’ll be no more "argh"
argh AaAaAaA
'''
#
# import re
# import sys
#
# pattern = r'\b[Aa]+\b'
#
# for line in sys.stdin:
#     print(re.sub(pattern, 'argh', line.rstrip(), 1))

'''Вам дана последовательность строк.

В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.

Буквой считается символ из группы \w.

Sample Input:

this is a text
"this' !is. ?n1ce,

Sample Output:

htis si a etxt
"htis' !si. ?1nce,
'''
#
# import re
# import sys
#
# pattern = r'(\w)\1+'
#
# for line in sys.stdin:
#     print(re.sub(pattern, r'\1', line.rstrip()))

'''Примечание:
Эта задача является дополнительной, то есть ее решение не принесет вам баллы.
Задача сложнее остальных задач из этого раздела, и идея ее решения выходит за рамки простого понимания регулярных 
выражений как средства задания шаблона строки.
Мы решили включить данную задачу в урок, чтобы показать, что регулярным выражением можно проверить не только 
"внешний вид" строки, но и заложенный в ней смысл.


Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.

Двоичной записью числа называется его запись в двоичной системе счисления.

Примечание 2:
Данная задача очень просто может быть решена приведением строки к целому числу и проверке остатка от деления
 на три, но мы все же предлагаем вам решить ее, не используя приведение к числу.
Sample Input:

0
10010
00101
01001
Not a number
1 1
0 0
Sample Output:

0
10010
01001'''

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.match(r"(1(01*0)*1|0)*$", line):
        print(line)
