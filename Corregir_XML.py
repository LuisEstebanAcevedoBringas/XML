import xml.etree.ElementTree as ET
from glob import glob
import os

def CorregirXLM(path):
    tree = ET.parse(path)
    root = tree.getroot()

if __name__ == "__main__":

    Lista_XMLs = glob('/*.xml')
    for xml in Lista_XMLs:
        CorregirXLM()