from calendar import week
from encodings import utf_8
import csv
from operator import indexOf
from datetime import datetime


def csvWrite(result):    # csv write

    col = ["ADM_CD", "TOT_REG_CD"]
    for i in range(24):
        col.append(str(i) + "_hour")

    dst = open('C:/capstone/FLOATING_PEOPLE/REG_FLOATING_PEOPLE.csv',
               'w', newline="", encoding='UTF-8')
    wr = csv.writer(dst)
    wr.writerow(col)
    for data in result:
        wr.writerow(data)


# weekday
weekDayList = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

ADM_CD = ["11215710",
          "11215730",
          "11215740",
          "11215750",
          "11215760",
          "11215770",
          "11215780",
          "11215810",
          "11215820",
          "11215830",
          "11215840",
          "11215847",
          "11215850",
          "11215860",
          "11215870"
          ]

f = open('C:/capstone/ADM_PEOPLE/행정동별 서울생활인구(내국인)'+'.csv',
         'r', encoding='euc-kr')

rdr = csv.reader(f)

ADM_PEOPLE = []

for i in range(24):
    ADM_PEOPLE.append({})

date_on = False
today = ""

for data in rdr:
    if(data[0] == '기준일ID'):
        continue
    if date_on == False:
        date_on = True
        today = data[0]

    code = data[2]
    if code >= "11215710" and code <= "11215870":
        time = int(data[1])
        ADM_PEOPLE[time][code] = float(data[3])

year = today[:4]
month = today[4:6]
day = today[6:8]
date = year+"-"+month+"-"+day

datetime_date = datetime.strptime(date, '%Y-%m-%d')
weekDay = datetime_date.weekday()
weekDayName = weekDayList[weekDay]

f = open('C:/capstone/REG_PEOPLE_RATIO/' + weekDayName + '_REG_PEOPLE_RATIO.csv',
         'r', encoding='UTF-8')

rdr = csv.reader(f)


result = []


for row in rdr:
    if row[0] == "ADM_CD":
        continue
    data = []
    ADM = row[0]
    REG_CD = row[1]
    data.append(ADM)
    data.append(REG_CD)
    for i in range(24):
        people = ADM_PEOPLE[i][ADM]
        ratio = float(row[i+2])
        data.append(people * ratio)
    result.append(data)


csvWrite(result)
