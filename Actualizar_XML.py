import xml.etree.ElementTree as ET
import os

def ModificarXML(path):
    tree = ET.parse(path)
    root = tree.getroot()

    #Generamos la nueva ruta de guardado
    file_Path = path
    file_Path = os.path.splitext(file_Path)[0]
    file_Name = file_Path.split('/')[-1]
    new_Path = "./xmlGUI/annotations/" + file_Name + ".xml" #Definimos la ruta de guardado

    #Agregamos los elementos "folder", "path", "source" & "databases"
    add_Folder = ET.Element("folder")
    add_Folder.text = "train"
    root.insert(0,add_Folder)
    add_Path = ET.Element("path")
    add_Path.text = "C:/temp/Properly-Wearing-Masked-Detect-Dataset/Train"
    root.insert(2,add_Path)
    add_Source = ET.Element("source")
    add_database = ET.SubElement(add_Source, "database")
    add_database.text="PWMD"
    root.insert(3,add_Source)

    #Obtenemos width y height de la imagen y calculamos su area
    img_Size = root.find("size")
    w = img_Size.find("width").text
    h = img_Size.find("height").text
    area_img = int(w) * int(h)

    #Agregamos el elemento "properly" y "size" dentro de cada "object"
    for object in root.iter('object'):
        add_properly = ET.SubElement(object, "properly")
        add_properly.text = "0"

        #Obtenemos width y height de cada objecto
        bbox = object.find('bndbox')
        xmin = int(bbox.find('xmin').text) - 1
        ymin = int(bbox.find('ymin').text) - 1
        xmax = int(bbox.find('xmax').text) - 1
        ymax = int(bbox.find('ymax').text) - 1

        #Calculamos el area de cada objecto
        width_obj = xmax - xmin
        height_obj = ymax - ymin
        area_obj = width_obj * height_obj
        obj_size = area_obj / area_img
        add_size = ET.SubElement(object, "obj_size")
        add_size.text = str(obj_size)

    #Guardamos el archivo modificado en el nuevo directorio
    file_Content = ET.tostring(root, encoding='unicode')
    new_File = open(new_Path, "w")
    new_File.write(file_Content) 

if __name__ == "__main__":
    ModificarXML("./xmlGUI/annot_old/000880.xml")