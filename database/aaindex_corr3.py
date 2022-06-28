# -*- coding: utf-8 -*-
import linecache
import re
import pandas as pd
pd.options.display.precision = 20
pd.set_option('display.max_columns', 1000)
import itertools


###行数確認###
row_count = 0 #行数カウンタ
c = 0 #抽出行数カウンタ
rows = []
with open('d/aaindex1.txt', 'r') as f1:
  for line in f1:
    row_count += 1
    if ("I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V" in line):
      rows.append(row_count)
      c += 1
      #print(c)
#print(row_count)
#print(rows)


###対象行をリストに追加###
# data0:1行目 data1:2行目
data0 = []
data1 = []
for i in rows:
  data0.append(linecache.getline('d/aaindex1.txt', i + 1).strip())
  data1.append(linecache.getline('d/aaindex1.txt', i + 2).strip())
#print(data0)
#print(data1)


###数値リストの作成###
#正規表現
datalist0 = []
datalist1 = []
datalist = []
pattern = r'([+-]?[0-9]+\.?[0-9]*)'
for i in data0:
  result = re.findall(pattern, i)
  #print(result)
  datalist0.append(result)
for i in data1:
  result = re.findall(pattern, i)
  #print(result)
  datalist1.append(result)
#print(datalist0)
#print(datalist1)


###数値リストを結合して、例外を除外###
c = 0
for i in datalist0:
  datalist.append(datalist0[c] + datalist1[c])
  c += 1
#print(len(datalist)) #566

remove_row = 0
for i in datalist[:]:
  remove_row += 1
  if len(i) < 20:
    datalist.remove(i)
    #print(remove_row)
#print(len(datalist)) #553


###数値リストの型をstr -> floatに変換###
for i in datalist:
  for j in range(20):
    i[j] = float(i[j])


datali = []
nl = []
cnt = 0
with open('d/namelist.txt', 'r') as f2:
  for line in f2:
    datali.append([[line.replace('\n', '')], pd.Series(datalist[cnt])])
    nl.append(line.replace('\n', ''))
    cnt += 1
    

print(datali)

"""
l1 = [["A",pd.Series([4.35, 4.38, 4.75, 4.76, 4.65, 4.37, 4.29, 3.97, 4.63, 3.95, 4.17, 4.36, 4.52, 4.66, 4.44, 4.5, 4.35, 4.7, 4.6, 3.95])],
      ["B",pd.Series([0.61, 0.6, 0.06, 0.46, 1.07, 0.0, 0.47, 0.07, 0.61, 2.22, 1.53, 1.15, 1.18, 2.02, 1.95, 0.05, 0.05, 2.65, 1.88, 1.32])], 
      ["C",pd.Series([1.18, 0.2, 0.23, 0.05, 1.89, 0.72, 0.11, 0.49, 0.31, 1.45, 3.23, 0.06, 2.67, 1.96, 0.76, 0.97, 0.84, 0.77, 0.39, 1.08])],
      ["D",pd.Series([1.56, 0.45, 0.27, 0.14, 1.23, 0.51, 0.23, 0.62, 0.29, 1.67, 2.93, 0.15, 2.96, 2.03, 0.76, 0.81, 0.91, 1.08, 0.68, 1.14])],
      ["E",pd.Series([1.0, 0.52, 0.35, 0.44, 0.06, 0.44, 0.73, 0.35, 0.6, 0.73, 1.0, 0.6, 1.0, 0.6, 0.06, 0.35, 0.44, 0.73, 0.44, 0.82])]]
li = []
"""

ans = []
c = 0
for i in range(0, len(datali)):
    for j in range(i + 1, len(datali)):
        for k in range(j + 1, len(datali)):
            ans.append([datali[i][0]+datali[j][0]+datali[k][0], (abs(datali[i][1].corr(datali[j][1])) + abs(datali[j][1].corr(datali[k][1])) + abs(datali[k][1].corr(datali[i][1])))])

f = open('test3.txt', 'w', encoding='UTF-8')
for i in ans:
    f.write("%s\n" % i)
f.close



