from calendar import week
from encodings import utf_8
import csv
from datetime import datetime

f = open('./data/dst/REG_FLOATING_PEOPLE.csv',
         'r', encoding='euc-kr')

f2 = open('./data/src/polygon포함.csv',
          'r', encoding='euc-kr')

rdr = csv.reader(f)
rdr2 = csv.reader(f2)

areas = {}

for data in rdr2:
    if(data[0] == 'WKT'):
        continue
    REG_CD = data[1]
    area = data[4]
    areas[REG_CD] = area

result = []

for data in rdr:
    if(data[0] == 'ADM_CD'):
        continue
    temp = []
    temp.append(data[0])
    temp.append(data[1])
    area = areas[data[1]]
    for i in range(24):
        people = data[i+2]
        density = float(people) / float(area)
        temp.append(density)
    result.append(temp)

col = []
col.append("ADM_CD")
col.append("TOT_REG_CD")

for i in range(24):
    col.append(str(i) + "_density")

dst = open('./data/dst/REG_PEOPLE_DENSITY.csv',
           'w', newline="", encoding='UTF-8')

wr = csv.writer(dst)
wr.writerow(col)

for data in result:
    wr.writerow(data)
