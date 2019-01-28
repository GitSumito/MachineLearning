# -*- coding: utf-8 -*-

import numpy as np
# ベクトルの定義
# numpyでは([])で括る

# 与えられたもの部屋の広さとか
x = np.array([1,3,5,10,20])
# その結果。値段など。
y = np.array([2.5,6,11,21,38])


# 全ての配列を表示
print ("全ての配列を表示")
print (x)
print (y)

## データの中心化
# 平均の算出
print x.mean()
print y.mean()

print ("中心化")
# cはcenteringの略とする
# pandsでも中心化する方法は存在する
xc = x -x.mean()
print (xc)

yc = y - y.mean()
print(yc)


## パラメータaの計算
print ("パラメータaの計算")
# 要素ごとの掛け算（要素積）
# 中心化したデータを掛け、それを合算させる。
# centeringした値が必要になる
#xx = xc * xc
#print xx

# 実際はサーキットラーンを使うともっと早い
# 分母はxc * xcで、最後に足す
xcxc = xc * xc
print xcxc
print ("分母:")
print xcxc.sum()

# 分子はx * yで最後に足す
xcyc = xc * yc
print ("分子:")
print xcyc.sum()

answer = xcyc.sum()/xcxc.sum()
print ("傾き:")
print (answer)

