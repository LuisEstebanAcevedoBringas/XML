import xml.etree.ElementTree as ET
from glob import glob

lista_imagenes = []

def find_images(path):
    tree = ET.parse(path)
    root = tree.getroot()
    lista_labels = []

    for object in root.iter("object"):
        name_img = root.find("filename").text
        label = object.find("label").text
        lista_labels.append(label)

        if "1" in lista_labels and "2" in lista_labels and "3" in lista_labels and "4" in lista_labels and "0" in lista_labels:
            lista_imagenes.append(name_img)

if __name__ == "__main__":
    
    Paths = glob("C:/Users/LuisB/Desktop/test/Annotations/*.xml")
    for p in Paths:
        find_images(p)
    
    print(lista_imagenes)