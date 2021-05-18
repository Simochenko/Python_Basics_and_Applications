# import requests
#
# api_url = "http://api.openweathermap.org/data/2.5/weather"
#
# city = input("City? ")
#
# params = {
#     'q': city,
#     'appid': '11c0d3dc6093f7442898ee49d2430d20',
#     'units': 'metric'
# }
#
# res = requests.get(api_url, params=params)
# # print(res.status_code)
# # print(res.headers["Content-Type"])
# # print(res.json())  # returns json.loads(res.text) :)
#
# data = res.json()
# template = 'Current temperature in {} is {}'
# print(template.format(city, data["main"]["temp"]))


# import requests
# import json
#
# with open('dataset_24476_3.txt') as file:
#     for number in file:
#         number = number.strip()
#         params = {'default': 'Boring number is boring', 'json': True}
#         url = 'http://numbersapi.com/{}/math'.format(number)
#         res = requests.get(url, params=params).text
#         data = json.loads(res)
#         if 'Boring' in data['text']:
#             print('Boring')
#         else:
#             print('Interesting')

import requests
import json

client_id = 'c106a77ee4dda462f463'
client_secret = '3aa6adfa54057aa5c4341152482a97ee'


r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token": token}

f = open("dataset_24476_4.txt", "r")
lst = []
for line in f:
    line = line.rstrip()
    template = 'https://api.artsy.net/api/artists/{}'
    r = requests.get(template.format(line), headers=headers)
    r.encoding = 'windows -1251'
    j = json.loads(r.text)
    lst.append(j)
f.close()

sorted_lst = sorted(lst, key=lambda person: (int(person['birthday']), person['sortable_name']))
for item in sorted_lst:
    print(item['sortable_name'])