import pandas as pd
import itertools

N = 553

df = pd.read_csv('d/aaindex_corr.csv', index_col = 0) # index_col indexの指定
print(df)

# 相関行列の読み込み
dic1 = {}
for i in range(0, N):
    for j in range(i + 1, N):
        dic1[df.index[i]+df.columns[j]]= df.iat[i, j]
#print(dic1)

# 名前リストの読み込み
nameli = []
for i in range(N):
    nameli.append(df.index[i])
#print(nameli)

# 相関係数の絶対値の和
corr_li = []
for i in range(0, N):
    
    # # TEST
    # if i == 1:
    #     break

    for j in range(i + 1, N):
        for k in range(j + 1, N):
            #print((nameli[i] + nameli[j] + nameli[k]), end = ":")
            #print(abs(dic1[nameli[i]+nameli[j]]) + abs(dic1[nameli[j]+nameli[k]]) + abs(dic1[nameli[i]+nameli[k]]))
            corr_li.append([(nameli[i] + nameli[j] + nameli[k]), 
                            abs(dic1[nameli[i]+nameli[j]]) + abs(dic1[nameli[j]+nameli[k]]) + abs(dic1[nameli[i]+nameli[k]])])

ans_li = sorted(corr_li, reverse=False, key=lambda x: x[1])  #[1]に注目してソート

with open('d/result.txt', 'w') as f:
    for line in ans_li:
        f.write(str(line))
        f.write("\n")




       




