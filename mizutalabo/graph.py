import numpy as np
import sys

def graph(aminolist): # aminolist = 生物種のND5配列　（例）MACDDIKLTWAH...
    al = aminolist
    xbuf = 0
    ybuf = 0
    zbuf = 0
    Xarr = np.array([]) # x座標
    Yarr = np.array([]) # y座標
    Zarr = np.array([]) # z座標

    dic = {"A":(), # アミノ酸の配置（三次元座標）
           "C":(),
           "D":(),
           "E":(),
           "F":(),
           "G":(),
           "H":(),
           "I":(),
           "K":(),
           "L":(),
           "M":(),
           "N":(),
           "P":(),
           "Q":(),
           "R":(),
           "S":(),
           "T":(),
           "V":(),
           "W":(),
           "Y":()}

    for ch in al:
        if ch in dic:
            xbuf = xbuf + dic[ch][0]
            ybuf = ybuf + dic[ch][1]
            zbuf = zbuf + dic[ch][2]
            Xarr = np.append(Xarr, xbuf)
            Yarr = np.append(Yarr, ybuf)
            Zarr = np.append(Zarr, zbuf)
        elif ch == "\n":
            break
        else:
            print("存在しない文字です")
            print(dic[ch])
            sys.exit()
            
    return (Xarr, Yarr, Zarr)