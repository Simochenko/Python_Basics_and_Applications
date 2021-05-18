# import simplecrypt
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

from simplecrypt import decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "rb") as inp:
    pwds = [s.decode("utf-8") for s in inp.read().split()]
    for pwd in pwds:
        try:
            print('Succesfully: ' + decrypt(pwd, encrypted).decode('utf8'))
        except:
            print('Password ' + pwd + ' didnt match')