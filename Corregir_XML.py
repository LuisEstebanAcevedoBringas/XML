import xml.etree.ElementTree as ET
from glob import glob
import os

label_change = {1:0, 3:1, 4:2, 5:3, 6:4}
name_change = {0:'cloth', 1:'none', 2:'respirator', 3:'surgical', 4:'valve'}

def CorregirXLM(path):
    tree = ET.parse(path)
    root = tree.getroot()

    #Cambiamos el valor del tag "folder" de "train" a "valid"
    new_folder = root.find("folder")
    new_folder.text = "valid"

    #atributos_source = root.find("path").text
    #print(ET.tostring(atributos_source, encoding='utf8').decode('utf8'))

    Contador_objetos = 0

    for object in root.iter("object"):
        object.remove(object.find("score")) #Eliminamos el tag "score" de cada objeto
        new_label = object.find("label")
        new_name = object.find("name")

        #Cambiamos el tag label y name de cada objeto.
        last_label = int(new_label.text)
        new_label.text = label_change[last_label]
        new_name.text = name_change[new_label.text]

        bbox = object.find('bndbox')
        #bbox.remove(bbox.find("object_prob"))
        xmin = int(bbox.find('xmin').text) - 1
        ymin = int(bbox.find('ymin').text) - 1
        xmax = int(bbox.find('xmax').text) - 1
        ymax = int(bbox.find('ymax').text) - 1

        Area_pix = (xmax - xmin) * (ymax - ymin) #Calculamos el area de cada bndbox

        #Agregamos el tag "obj_size" a cada bndbox
        object_size = bbox.find("obj_size")
        object_size.text = str(Area_pix)

        #Agregamos el tag "size" a cada objeto
        add_size = ET.SubElement(object, "size")
        if Area_pix < 3666 :
            add_size.text = "0"
        elif Area_pix > 3665 and Area_pix < 14522:
            add_size.text = "1"
        elif Area_pix > 14521:
            add_size.text = "2"
    
        Contador_objetos += 1

    #Actualizamos el numero del tag "faces" segun la cantidad de "objetos en el xml
    new_face = root.find("faces")
    new_face.text = str(Contador_objetos)

    #Guardamos el archivo modificado en el nuevo directorio
    file_Content = ET.tostring(root, encoding='unicode')
    new_File = open(path, "w")
    new_File.write(file_Content) 

if __name__ == "__main__":

    #Paths = glob("./valid/Annotations/*.xml")
    #for p in Paths:
    #    CorregirXLM(p)
    CorregirXLM("./E_0AcW4VgAYXanL.xml")