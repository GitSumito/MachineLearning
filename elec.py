# coding: utf-8
import pandas as pd
import numpy as np

# 電力データの読み込み
kw_df = pd.read_csv("juyo-2016.csv")

# 気温データの読み込み
temp_df = pd.read_csv("data.csv")

# データの結合
df = kw_df
df["temperature"] = temp_df["temperature"]

# 曜日データの取得

import datetime

pp = df["DATE"]
tmp = []

for i in range(len(pp)):
    d = datetime.datetime.strptime(pp[i], "%Y/%m/%d")
    tmp.append(d.weekday())

df["weekday"] = tmp

# 時間データの取得

pp = df["TIME"]
tmp = []

for i in range(len(pp)):
    d = datetime.datetime.strptime(pp[i], "%H:%M")
    tmp.append(d.hour)

df["hour"] = tmp


# 入力
pp = df[["temperature","weekday","hour"]]
X = pp.as_matrix().astype('float')

# 出力
pp = df["elec"]
y = pp.as_matrix().flatten()

# クロスバリデーションのモジュールを読み込む
#from sklearn import cross_validation
from sklearn import model_selection

# ラベル付きデータをトレーニングセット (X_train, y_train)とテストセット (X_test, y_test)に分割
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=.2, random_state=42)

# 正規化のモジュールを読み込む
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# モジュールの読み込み
from sklearn import svm
model = svm.SVC()

# 学習
model.fit(X_train, y_train)
# model.score(X,y)を使って予測精度を出す
print(model.score(X_test,y_test))
