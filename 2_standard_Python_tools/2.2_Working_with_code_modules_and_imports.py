'''В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.

Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
равное days.

Примечание:

Для решения этой задачи используйте стандартный модуль datetime. Вам будут полезны класс datetime.date для хранения
даты и класс datetime.timedelta для прибавления дней к дате.

Sample Input 1:

2016 4 20
14

Sample Output 1:

2016 5 4

Sample Input 2:

2016 2 20
9

Sample Output 2: 2016 2 29

Sample Input 3:

2015 12 31
1

Sample Output 3:

2016 1 1'''

# from datetime import date, timedelta
# inp1 = list(map(int, input().split()))
# inp2 = int(input())
#
# date = date(*inp1)
# days = timedelta(days=inp2)
# result = date + days
#
# print(result.year, result.month, result.day)


# import urllib.request as urllib
#
# passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')
#
# with open('encrypted.bin', 'rb') as inp:
#     encrypted = inp.read()
#
# for password in passwords:
#     password = password[:-1]
#     try:
#         print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
#     except simplecrypt.DecryptionException:
#         print(password, 'is wrong')
#     else:
#         print(password, 'is correct')

# import simplecrypt
# import multiprocessing
#
#
# def decrypt(data, password):
#     try:
#         res = simplecrypt.decrypt(password, data)
#         print(res)
#     except simplecrypt.DecryptionException:
#         print("Password: {} is wrong".format(password))
#
#
# def main():
#     with open("encrypted.bin", "rb") as ef, open("passwords.txt", "r") as pwd:
#         data = ef.read()
#         processes = []
#
#         for p in pwd:
#             password = p.rstrip()
#             t = multiprocessing.Process(target=decrypt, args=(data, password))
#             processes.append(t)
#             t.start()
#
#         for t in processes:
#             t.join()
#
#
# if __name__ == "__main__":
#     main()

# import requests
# from simplecrypt import decrypt, DecryptionException
#
# code = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
# passes = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').content
#
# for p in passes.split():
#     try:
#         s = decrypt(p, code)
#     except DecryptionException:
#         pass
#     else:
#         print(p, s)

# with open("encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
#
# with open("passwords.txt", "rb") as inp:
#     pwds = [s.decode("utf-8") for s in inp.read().split()]
#     for pwd in pwds:
#         try:
#             print('Succesfully: ' + decrypt(pwd, encrypted).decode('utf8'))
#         except:
#             print('Password ' + pwd + ' didnt match')


import simplecrypt
import urllib.request as urllib

passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

for password in passwords:
    password = password[:-1]
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is correct')