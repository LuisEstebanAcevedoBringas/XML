import xml.etree.ElementTree as ET
from glob import glob


def xml_annotation(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    acum = 0
    size = 0
    for object in root.iter('object'):
        bbox = object.find('bndbox')

        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        size += 1

        acum += (xmax - xmin) * (ymax - ymin)

    return acum / size


lista = glob('/*.xml')

acum = 0
for p in lista:
    acum += xml_annotation(p)

print('Tamaño promedio de las bounding box: {}'.format(acum/len(lista)))
