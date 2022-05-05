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

    #Agregamos elementos "folder", "path", "source" & "databases"
    add_Folder = ET.Element("folder")
    add_Folder.text = "train"
    root.insert(0,add_Folder)
    add_Path = ET.Element("path")
    add_Path.text = "C:temp\Properly-Wearing-Masked-Detect-Dataset\Train"
    root.insert(2,add_Path)
    add_Source = ET.Element("source")
    add_database = ET.SubElement(add_Source, "database")
    add_database.text="PWMD"
    root.insert(3,add_Source)

    #Agregamos el elemento "properly" dentro de cada "object"
    for object in root.iter('object'):
        add_properly = ET.SubElement(object, "properly")
        add_properly.text = "0"

    #Guardamos el archivo modificado en el nuevo directorio
    file_Content = ET.tostring(root, encoding='unicode')
    new_File = open(new_Path, "w")
    new_File.write(file_Content) 

ModificarXML("./xmlGUI/annot_old/000743.xml")