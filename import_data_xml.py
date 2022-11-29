import xml.etree.ElementTree as ET

def parse_xml(file_name):
    # Чтение данных из файла в формате xml
    with open(f'{file_name}', 'r'):
        data = [tuple([i.text  for i in ET.parse(f'{file_name}').getroot()[j]]) 
                for j in range(len(ET.parse(f'{file_name}').getroot()))]
        # print(data)
    return data

