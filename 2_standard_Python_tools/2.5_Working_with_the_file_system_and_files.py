# f= open("test.txt")
# # x = f.readline().rstrip()
# # x = x.splitlines()
# # print(repr(x))
# for line in f:
#     line = line.rstrip()
#     print(repr(line) ).

# f = open("test1.txt", "w")
# lines = ["line 1", "line 2", "line 3"]
# contents = "\n".join(lines)
# f.write(contents)
#
# f.close()

# f = open("test_append.txt", "a")
# f.write("Hello\n")
#
# f.close()

# with open("test.txt") as f:
#     for line in f:
#         line = line.rstrip()
#         print(line)

# with open("test.txt") as f, open("tes_copy.txt", "w") as w :
#     for line in f:
#         w.write(line)
'''Вам дается текстовый файл, содержащий некоторое количество непустых строк.

На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:

ab
c
dde
ff

Пример выходного файла:

ff
dde
c
ab
'''
# with open('dataset_24465_4.txt') as f1:
#     f1_lines = f1.read().splitlines()
#
# with open('result.txt', 'w') as f2:
#     for line in f1_lines[::-1]:
#         f2.write('%s\n' % line)

import os.path
# import shutil
# # print(os.getcwd())
# # print(os.listdir())
# # print(os.path.exists("test.txt"))
# #
# # for current_dir, dirs, files in os.walk("."):
# #     print(current_dir, dirs,files)
# shutil.copy("test1.txt", "test2.txt")

# import os
#
# with open('result.txt', 'a') as f:
#     for current_dir, dirs, files in os.walk('main'):
#         if list(filter(lambda x: x.endswith('.py'), files)):
#             f.write('{}\n'.format(current_dir))

import os

for cur_dir, subdirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            print(cur_dir)
            break