# import csv
# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# students = [
#     ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
#     ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
# ]

# with open("example.csv", "a") as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(students)
# import csv
# from collections import Counter
#
# with open('Crimes.csv') as file:
#     reader = csv.reader(file)
#     data = list(reader)[1:]
#     crimes = list(zip(*data))[5]
#     crime_counts = Counter(crimes)
#     print(crime_counts.most_common(1))

# import json
# student1 = {
#     'first_name': 'Greg',
#     'last_name': 'Dean',
#     'scores': [70, 80, 90],
#     'description': "Good job, Greg",
#     'certificate': True
# }
#
# student2 = {
#     'first_name': 'Wirt',
#     'last_name': 'Wood',
#     'scores': [80, 80.2, 80],
#     'description': "Nicely Done",
#     'certificate': True
# }

# data = [student1, student2]
# data_json = json.dumps(data, indent=4, sort_keys=True)
# data_again = json.loads(data_json)
# print(sum(data_again[0]["scores"]))

# print(json.dumps(data, indent=4, sort_keys=True))
# with open("students.json", "w") as f:
#     json.dump(data, f, indent=4, sort_keys=True)

# with open("students.json", "r") as f:
#     data_again = json.load(f)
#     print(sum(data_again[1]["scores"]))

'''¬ам дано описание наследовани€ классов в формате JSON.

ќписание представл€ет из себ€ массив JSON-объектов, которые соответствуют классам. ” каждого JSON-объекта есть поле
 name, которое содержит им€ класса, и поле parents, которое содержит список имен пр€мых предков.

ѕример:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

?Ёквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

√арантируетс€, что никакой класс не наследуетс€ от себ€ €вно или косвенно, и что никакой класс не наследуетс€ €вно
от одного класса более одного раза.

ƒл€ каждого класса вычислите предком скольких классов он €вл€етс€ и выведите эту информацию в следующем формате.

<им€ класса> : <количество потомков>

¬ыводить классы следует в лексикографическом пор€дке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2
'''

import json

initial = json.loads(input())

with_children = {element['name']: [] for element in initial}

for eli in initial:
    for elc in with_children:
        if elc in eli['parents']:
            with_children[elc].append(eli['name'])

for element in with_children:
    with_children[element] = set(with_children[element])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

for element in sorted(with_children.keys()):
    print(element, ':', len(dfs(with_children, element)))