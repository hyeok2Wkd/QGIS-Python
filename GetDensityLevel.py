from calendar import week
from encodings import utf_8
import csv
from operator import indexOf
from datetime import datetime

src = open('C:/capstone/FLOATING_PEOPLE/REG_PEOPLE_DENSITY.csv',
           'r', encoding='UTF-8')

rdr = csv.reader(src)

rows = []

time = 18

for data in rdr:
    if(data[0] == 'ADM_CD'):
        continue
    temp = []
    temp.append(data[0])
    temp.append(data[1])
    temp.append(data[2+time])
    rows.append(temp)

rows.sort(key=lambda x: x[2])

now = 0
flag = True

for level in range(1, 6):
    for i in range(now, now+132):
        rows[i].append(level)
    now += 132

rows[len(rows)-1].append(5)
rows[len(rows)-2].append(5)


dst = open('C:/capstone/FLOATING_PEOPLE/REG_PEOPLE_DENSITY_'+str(time)+'_LEVEL.csv',
           'w', newline="", encoding='UTF-8')

col = []
col.append("ADM_CD")
col.append("TOT_REG_CD")
col.append(str(time)+"_density")
col.append(str(time)+"_level")

wr = csv.writer(dst)
wr.writerow(col)

for data in rows:
    wr.writerow(data)
