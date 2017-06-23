from lxml import etree


root = etree.Element("ameba")
doc = etree.SubElement(root, "dupa")
etree.SubElement(doc, "kot", name="rudy").text = "siersciuch"
etree.SubElement(doc, "kot", name="czarny").text = "pierdola"
with open('output.xml', 'wb') as f:
    f.write(etree.tostring(root, pretty_print=True))
    

