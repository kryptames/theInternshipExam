import xml.etree.ElementTree as ET
import json
js = {}

def convertor(file): 
    root = ET.parse(file).getroot()
    global js
    for child in root:
        js[child.tag] = child.attrib
        getleaf(child, child.findall("./"))
    return js
def getleaf(root, leaf):
    global js
    if len(leaf) != 0:
        if leaf[0].attrib:
            root.attrib.update({leaf[0].tag: leaf[0].attrib})
        if leaf[0].text:
            root.attrib.update({leaf[0].tag: leaf[0].text})
        getleaf(root, leaf[1:])
    return 
    
jsonname, xmlname = input().split(" ")
file = open(xmlname, "r") 
with open(jsonname+".json", "w") as f:
    f.write(json.dumps(convertor(file)))