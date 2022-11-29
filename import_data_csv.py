import csv

def read_data_csv(file_name):
    # Чтение данных из файла в формате csv
    with open(f'{file_name}', 'r', newline='', encoding='utf-8') as f:
        data = [tuple(row) for row in csv.reader(f)]
    return data
            
