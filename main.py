"""
Нужно написать скрипт, который читает данные сотрудников из файлов в формате csv и формирует простой отчет по заработной плате (см. ниже примеры).
В скрипт можно передать несколько файлов и тип отчета который нужно сформировать, в данном случае отчёт по зарплатам payout. Файлы на вход всегда в формате csv,
валидные и без ошибок. Название отчета передается через  параметр --report. Реализовать нужно только отчёт по зарплатам,
но желательно заложить возможность добавления новых отчётов, например если захочется посмотреть среднюю ставку в час по отделам то это можно будет быстро добавить.
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
```
"""

import os.path
import sys
import argparse

"""
class employee:
    def __init__(self, id,email,name,department,hours,rate):
        self.id = id
        self.email = email
        self.name = name
        self.department = department
        self.hours = hours
        self.rate = rate
"""

# Возвращает нужное кол-во пробелов для выравнивания
def get_spaces(n):
    str = ""
    for i in range(0,n):
        str = str + " "
    return str


# Обрабатывает переданный .csv файл, выводит содержимое в формате payout
def get_payout(filename):
    ext = os.path.splitext(filename)[1]
    if ext != ".csv":
        print("Non-csv file was provided, exiting")
        raise SystemExit(1)
    file = open(filename, "r")
    finalString = "               name                 hours   rate   payout"
    i_id = -1
    i_email = -1
    i_name = -1
    i_department = -1
    i_hours = -1
    i_rate = -1
    lines = [line.rstrip() for line in file]
    #print(lines)
    if len(lines) > 0:
        header = lines[0].split(",")
        for i in range(0, len(header)):
                #print(header[i])
                match header[i]:
                    case "id":
                        i_id = i
                    case "email":
                        i_email = i
                    case "name":
                        i_name = i
                    case "department":
                        i_department = i

                    case "hours_worked":
                        i_hours = i
                    case "hourly_rate":
                        i_rate = i
                    case "salary":
                        i_rate = i
                    case "rate":
                        i_rate = i

        if i_id == -1:
            print("Missing id in csv header")
            raise SystemExit(1)
        if i_email == -1:
            print("Missing email in csv header")
            raise SystemExit(1)
        if i_name == -1:
            print("Missing name in csv header")
            raise SystemExit(1)
        if i_department == -1:
            print("Missing department in csv header")
            raise SystemExit(1)
        if i_hours == -1:
            print("Missing hours_worked in csv header")
            raise SystemExit(1)
        if i_rate == -1:
            print("Missing hourly_rate in csv header")
            raise SystemExit(1)

        finalString = finalString + "\n"
        finalString = finalString  + lines[1].split(",")[i_department] + "\n"

        for i in range(1, len(lines)):

            lineParams = lines[i].split(",")
            name = lineParams[i_name]
            rate = int(lineParams[i_rate])
            hours = int(lineParams[i_hours])
            payout = rate * hours

            lineStr = "--------------"
            lineStr = lineStr + " " + name + get_spaces(21 - len(name))
            lineStr = lineStr + str(hours) + get_spaces(8 - len(str(hours)))
            lineStr = lineStr + str(rate) + get_spaces(8 - len(str(rate)))
            lineStr = lineStr + "$" + str(payout)
            finalString = finalString + lineStr + "\n"

        return finalString

if __name__ == '__main__':

    knownTypes = ("payout",)
    fileParser=argparse.ArgumentParser()
    fileParser.add_argument("files",nargs="+")
    fileParser.add_argument("--report",nargs=1)
    fileParser.add_argument("--json",nargs=1,default="out.json")
    args = vars(fileParser.parse_args())
    #print(args)
    jsonFilename = args["json"][0]
    reportType = args["report"][0]
    if reportType not in knownTypes:
        print("Unknown report type")
        raise SystemExit(1)
    #print(reportType)



    #print(args)
    f = open(jsonFilename,"w")
    for i in range(0, len(args["files"])):
                    arg = args["files"][i]
                    #print(arg)
                    if reportType == "payout":
                        #print(get_payout(file))
                            f.write(get_payout(arg))


