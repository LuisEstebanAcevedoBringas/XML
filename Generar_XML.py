import xml.etree.ElementTree as ET
from PIL import Image
import linecache
import os

def Generar_XML(path_txt, path_img):

    file_Path = path_txt
    file_Path = os.path.splitext(file_Path)[0]
    file_Name = file_Path.split('/')[-1]
    img_Path = path_img
    img_Path = os.path.splitext(img_Path)[0]
    img_Name = img_Path.split('/')[-1]

    if os.path.basename(img_Name) == os.path.basename(file_Name):

        #Definimos la ruta de guardado
        new_Path = "./xmlGUI/annotations/" + file_Name + ".xml"

        #Obtener tamaño de la imagen
        img = Image.open(path_img)
        img_width, img_height = img.size
        img_w, img_h = str(img_width), str(img_height)
        dim = "3"

        #Estructura del xml
        Annotation = ET.Element("annotation")
        add_Folder = ET.SubElement(Annotation,"folder")
        add_Folder.text = "train"
        add_Filename =ET.SubElement(Annotation,"filename")
        add_Filename.text = os.path.basename(path_img)
        add_Path = ET.SubElement(Annotation,"path")
        add_Path.text = "C:temp\Properly-Wearing-Masked-Detect-Dataset\Train"
        add_Source = ET.SubElement(Annotation,"source")
        add_database = ET.SubElement(add_Source, "database")
        add_database.text="PWMD"
        add_size = ET.SubElement(Annotation,"size")
        add_width = ET.SubElement(add_size,"width")
        add_width.text = img_w
        add_height = ET.SubElement(add_size,"height")
        add_height.text = img_h
        add_dimension = ET.SubElement(add_size,"depth")
        add_dimension.text = dim
        
        #Crear los elementos "object"
        with open(path_txt) as myfile:
            lineas_Totales = sum(1 for line in myfile)
            #print("Lineas totales del txt: ",lineas_Totales)
        
        y = 3
        for x in range(lineas_Totales):

            #Agregamos las propiedades "name", "properly" y "bndbox"
            add_Object = ET.SubElement(Annotation,"object")
            add_Name = ET.SubElement(add_Object, "name")
            add_Name.text = "surgical"
            add_Properly = ET.SubElement(add_Object,"properly")
            add_Properly.text = "0"
            add_bndbox = ET.SubElement(add_Object,"bndbox")

            #Obtenemos las propierdad  "xmin", "ymin", "xmax", "ymax"
            linea = linecache.getline(path_txt, y).strip()
            xmin, ymin, w_txt, h_txt, _ = linea.split()
            xmax = int(xmin) + int(w_txt)
            ymax = int(ymin) + int(h_txt)
            add_xmin = ET.SubElement(add_bndbox,"xmin")
            add_xmin.text = xmin
            add_ymin = ET.SubElement(add_bndbox,"ymin")
            add_ymin.text = ymin
            add_xmax = ET.SubElement(add_bndbox,"xmax")
            add_xmax.text = str(xmax)
            add_ymax = ET.SubElement(add_bndbox,"ymax")
            add_ymax.text = str(ymax)
            y += 2
            if y >= lineas_Totales:
                break

        #Guardamos el archivo modificado en el nuevo directorio
        file_Content = ET.tostring(Annotation, encoding='unicode')
        new_File = open(new_Path, "w")
        new_File.write(file_Content) 
    
    else:
        print("Los archivos no estan relacionados.")

Generar_XML("./xmlGUI/annot_txt/EqkccHpXUAAvYjM.txt","./xmlGUI/images/EqkccHpXUAAvYjM.jpg")