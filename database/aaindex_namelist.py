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
with open('aaindex1.txt', 'r') as f1:
  for line in f1:
    row_count += 1
    if ("//" in line):
      rows.append(row_count + 1)
      c += 1
      #print(c)
print(rows)

# アクセッション番号の取得
names = []
for i in rows:
  names.append(linecache.getline('aaindex1.txt', i).replace('H ', '').strip())
print(names)

delindex = [472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 520, 523, 524]

for i in reversed(range(len(names))):
  if i in delindex:
    del names[i]
  
print(names)
print(len(names))

f = open('namelist.txt', 'w', encoding='UTF-8')
for i in names:
    f.write("%s\n" % i)
f.close

"""
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


###総当りで相関係数を計算###
com_datalist = pd.Series(list(itertools.combinations(datalist, 3)))
print(com_datalist)


cc = 0
ans = 1
ans_ = []
res_count = 0
x_1 = []
x_2 = []
x_3 = []
for i in range(len(com_datalist)):
  x1 = pd.Series(com_datalist[i][0])
  x2 = pd.Series(com_datalist[i][1])
  x3 = pd.Series(com_datalist[i][2])
  res12 = x1.corr(x2)
  res13 = x1.corr(x3)
  res23 = x2.corr(x3)
  res = abs(res12) + abs(res13) + abs(res23)

  # 絶対値が小さいもの
  if ans > res:
    ans = res
    ans_.append(ans)
    x_1.append(x1)
    x_2.append(x2)
    x_3.append(x3)
    res_count += 1

  cc += 1
  print(cc)


f = open('result.txt', 'w')
for i in range(res_count):
  f.write(str(ans_[i]) + "\n")
  f.write(str(x_1[i]) + "\n")
  f.write(str(x_2[i]) + "\n")
  f.write(str(x_3[i]) + "\n")
  f.write('\n')
f.close()
"""