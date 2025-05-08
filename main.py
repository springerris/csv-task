"""Нужно написать скрипт, который читает данные сотрудников из файлов в формате csv и формирует простой отчет по заработной плате (см. ниже примеры). В скрипт можно передать несколько файлов и тип отчета который нужно сформировать, в данном случае отчёт по зарплатам payout. Файлы на вход всегда в формате csv, валидные и без ошибок. Название отчета передается через  параметр --report. Реализовать нужно только отчёт по зарплатам, но желательно заложить возможность добавления новых отчётов, например если захочется посмотреть среднюю ставку в час по отделам то это можно будет быстро добавить.
Пример файла csv с данными сотрудников:
```
id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60
```
Пример выходного файла json:
```
                  name                    hours   rate   payout
Design
-------------- Bob Smith            150      40     $6000
-------------- Carol Williams      170      60     $10200
                                               320               $16200
Marketing
-------------- Alice Johnson       160      50     $8000
                                               160               $8000
```
Пример запуска скрипта:
```
python3 main.py data1.csv data2.csv data3.csv --report payout
```"""
import sys

class employee:
    def __init__(self, id,email,name,department,hours,rate):
        self.id = id
        self.email = email
        self.name = name
        self.department = department
        self.hours = hours
        self.rate = rate

def readCSV(filename) {
    
}

args = sys.argv[1:]
print(args)

csvFile = args[0]

