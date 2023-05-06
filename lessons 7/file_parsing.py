import requests
import csv

# Открыть файл test_file.csv, прочитать, распарсить зп сотрудников в долларах и перевести в гривны на текущую
# дату(курс задается отдельной переменной). Результат сохранить в новый файл salaries_uah.csv


def exchange():
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()
    return float(data[1]['buy'])


usd_to_uah = exchange()


def convert_file(csv_file, usd_rate):
    with open(f'{csv_file}', 'r') as file:
        read = csv.DictReader(file)
        uah_salaries = []
        for raw in read:
            keys = sorted(raw.keys())[1:]
            for key in keys:
                raw[key] = f'{"%.2f" % (float(raw[key]) * usd_rate)}'
            uah_salaries.append(raw)
        with open('salaries_uah.csv', 'w', newline='') as file1:
            writer = csv.DictWriter(file1, fieldnames=raw.keys())
            writer.writeheader()
            writer.writerows(uah_salaries)


convert_file('test_file.csv', usd_to_uah)
