import xml.etree.ElementTree as ET

def ModificarXML(path):
    tree = ET.parse(path)
    root = tree.getroot()
    new_path = 0

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

    #Agregamos el elemento "properly" dentro de "object"
    for object in root.iter('object'):
        add_properly = ET.SubElement(object, "properly")
        add_properly.text = "0"

    tree.write(new_path) #Guardar el archivo

    print(ET.tostring(root, encoding='utf8').decode('utf8'))

ModificarXML("./xmlGUI/annot_old/000880.xml")