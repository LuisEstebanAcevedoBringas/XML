import xml.etree.ElementTree as ET
from glob import glob
import numpy as np

name_size = {0: 'Pequeño', 1: 'Mediano', 2: 'Grande'}
name_change = {0: 'cloth', 1: 'none', 2: 'respirator', 3: 'surgical', 4: 'valve'}
contador_labels = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
contador_size = {0: 0, 1: 0, 2: 0}
contador_objetos_size = {0: [], 1: [], 2: []}
contador_faces = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
lista_px = []

def getStatics(path):
    tree = ET.parse(path)
    root = tree.getroot()
    faces = int(root.find('faces').text)
    contador_faces[faces] += 1
    for object in root.iter("object"):
        label = int(object.find('label').text)
        size = int(object.find('size').text)
        contador_labels[label] += 1
        contador_size[size] += 1

        contador_objetos_size[size].append(label)

        lista_px.append(int(object.find('bndbox').find('obj_size').text))

if __name__ == "__main__":

    # Path de todos los xml
    Paths = glob("./valid/Annotations/*.xml")
    for p in Paths:
        getStatics(p)

    print('Objetos correspondientes por clase')
    for i, j in zip(contador_labels.keys(), contador_labels.values()):
        print('{} : {}'.format(name_change[i], j))

    print('\nObjetos correspondientes por size')
    for i, j in zip(contador_size.keys(), contador_size.values()):
        print('{} : {}'.format(name_size[i], j))

    for i in [0, 1, 2]:
        print('\nValor de size {}'.format(i))
        print('{} : {}'.format(name_change[0], contador_objetos_size[i].count(0)))
        print('{} : {}'.format(name_change[1], contador_objetos_size[i].count(1)))
        print('{} : {}'.format(name_change[2], contador_objetos_size[i].count(2)))
        print('{} : {}'.format(name_change[3], contador_objetos_size[i].count(3)))
        print('{} : {}'.format(name_change[4], contador_objetos_size[i].count(4)))

    print('\nObjetos correspondientes por faces')
    for i, j in zip(contador_faces.keys(), contador_faces.values()):
        print('{} : {}'.format(i, j))

    print('\nObjeto mas grande: {}'.format(max(lista_px)))
    print('\nObjeto mas pequeño: {}'.format(min(lista_px)))

    print('\nPromedio de tamaño de objetos: {}'.format(
        sum(lista_px)/len(lista_px)))
    print('\nPromedio de desviacion estandar: {}'.format(np.std(lista_px)))