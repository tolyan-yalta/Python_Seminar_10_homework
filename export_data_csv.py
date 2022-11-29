import csv

def write_new_data_csv(data, file):
    # Запись данных в формате csv
    with open(f'{file}', 'w', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerows(data)


