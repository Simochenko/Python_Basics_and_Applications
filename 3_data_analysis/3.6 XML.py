"""Вам дано описание пирамиды из кубиков в формате XML.

Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).

Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:

4 3 1"""

from xml.etree.ElementTree import XMLParser

xml = input()

class ColorWeights:                    # The target object of the parser
    depth = 0
    weights = {'red': 0, 'green': 0, 'blue': 0}

    def start(self, tag, attrib): # Called for each opening tag.
        self.depth += 1
        self.add_weight(attrib)

    def add_weight(self, attrib):
        self.weights[attrib['color']] += self.depth

    def end(self, tag):           # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass                      # We do not need to do anything with data.

    def close(self):              # Called when all data has been parsed.
        weights_list = [self.weights['red'], self.weights['green'], self.weights['blue']]
        return ' '.join(list(map(str, weights_list)))

target = ColorWeights()
parser = XMLParser(target=target)
parser.feed(xml)
print(parser.close())