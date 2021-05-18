# import requests
#
# res = requests.get("https://docs.python.org/3.5/_static/py.png")
# print(res.status_code)
# print(res.content)
#
#
# with open("python.png", "wb") as f:
#     f.write(res.content)
'''���������� ��� HTML-��������� A � B.

�� A ����� ������� � B �� ���� �������, ���� � A ���� ������ �� B, �. �. ������ A ���� ��� <a href="B">, ��������
� ��������������� ����������� ������ ����. �� A ����� ������� � B �� ��� �������� ���� ���������� ����� ��������
C, ��� �� A � C ����� ������� �� ���� ������� � �� C � B ����� ������� �� ���� �������.

����� ��������� �� ���� �������� ��� ������, ���������� url ���� ���������� A � B. �������� Yes, ���� �� A � B �����
������� �� ��� ��������, ����� �������� No.

�������� �������� �� ��, ��� �� ��� ������ ������ HTML ��������� ����� ����� �� ������������ HTML ���������.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html

https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:

Yes

Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html

https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:

No

Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html

https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:

Yes'''
# import re
# import urllib.request
#
# a = input()
# b = input()
#
# def get_links(url):
#     try:
#         fp = urllib.request.urlopen(url)
#         mybytes = fp.read()
#         mystr = mybytes.decode("utf8")
#         fp.close()
#         links = re.findall(r'<a.*href="([^"]*)"', mystr)
#     except:
#         return []
#     else:
#         return links
#
# def two_steps():
#     links1 = get_links(a)
#
#     for link in links1:
#         links2 = get_links(link)
#         if b in links2:
#             return True
#     return False
#
# if two_steps():
#     print("Yes")
# else:
#     print("No")

'''����� ��������� �� ���� �������� ������ �� HTML ����. ��� ���������� ������� ���� ����, ����� ����� � ��� ��� ������ ���� <a ... href="..." ... > � ������� ������ ������, �� ������� ���� ������.

������ � ������ ������ ����� �������� ��� ������ ������ � ������� ����������. �� ����, ��� ������������������ ��������, ������� ������� ����� ����� �������� ���������, ���� �� ����, �� �������� ����� ��� ����, ���� ��� ����, �� ����������� ������� � �������������� �������� ���� ?.

����� ������� �������� � ���������� �������.

������ HTML �����:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

������ ������:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
'''