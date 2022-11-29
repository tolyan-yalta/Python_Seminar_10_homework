import xml.etree.ElementTree as ET

def indent(elem, level=0):
    # Форматирование отступов и переносов строк для записи в файл
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def write_new_data_xml(data, file):
    # Запись данных в формате xml
    # print(f'++{data}')

    database = ET.Element('database')

    for p in data:
        person = ET.SubElement(database, 'person')
        id = ET.SubElement(person, 'id').text = p[0]
        famaly = ET.SubElement(person, 'Famaly').text = p[1]
        name = ET.SubElement(person, 'Name').text = p[2]
        last_name = ET.SubElement(person, 'Last_name').text = p[3]
        telephon = ET.SubElement(person, 'Telephon').text = p[4]
        e_mail = ET.SubElement(person, 'E_mail').text = p[5]

    indent(database)
    tree = ET.tostring(database, encoding='unicode')

    with open(f'{file}', 'w', encoding='UTF-8') as f:
        f.write(tree)

