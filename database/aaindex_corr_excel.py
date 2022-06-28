# -*- coding: utf-8 -*-
import linecache
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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


#print(datalist)

datadic = {}
nl = []
cnt = 0
with open('d/namelist.txt', 'r') as f2:
  for line in f2:
    datadic[line.replace('\n', '')] = datalist[cnt]
    nl.append(line.replace('\n', ''))
    cnt += 1
    

print(datadic)

df = pd.DataFrame(datalist)

res=df.T.corr()

res.index = nl
res.columns = nl

res.to_csv("d/aaindex_corr.csv")

"""
sns.heatmap(res)
plt.savefig("test.svg")
plt.show()
"""