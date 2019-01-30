# coding: utf-8
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# データを読み込む
data = np.loadtxt("simple.txt")
x = data.T[0]
y = data.T[1]

# サンプルの数
nsample = x.size

# おまじない (後で解説)
X = np.column_stack((np.repeat(1, nsample), x))

# 回帰実行
model = sm.OLS(y, X)
results = model.fit()

# 結果の概要を表示
#print results.summary()

# パラメータの推定値を取得
a, b = results.params

# プロットを表示
plt.plot(x, y, 'o')
plt.plot(x, a+b*x)
plt.text(0, 0, "a={:8.3f}, b={:8.3f}".format(a,b))
plt.show()
