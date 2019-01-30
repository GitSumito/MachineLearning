# coding: utf-8
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# データ読み込み
data = np.loadtxt("regression_2.txt")
x = data.T[0]
y = data.T[1]

# サンプルの数
nsample = x.size

# 行列Xの作成
X = np.column_stack((np.repeat(1, nsample), x, x**2))

# 回帰を実行
model = sm.OLS(y, X)
results = model.fit()

# 結果の概要を表示
#print results.summary()

# パラメータの推定値を取得
a, b, c = results.params

# グラフで表示
plt.plot(x, y, 'o')
plt.plot(x, a+b*x+c*x**2)
plt.title("a={:.4f}, b={:.4f}, c={:.4f}".format(a,b,c))
plt.show()

