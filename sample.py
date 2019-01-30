import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('aaa.csv')
fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

fig = sm.graphics.tsa.plot_acf(df['jsk'],ax=ax1)
fig2 = sm.graphics.tsa.plot_pacf(df['jsk'],ax=ax2)

print (df) 
#model = sm.tsa.SARIMAX(df,order=(2,1,0),seasonal_order=(1,1,1,26))
#result_sarima = model.fit()

#plt.plot(result_sarima.predict(start=1,end=150),label='予測')
plt.plot(df['jsk'],label='jisseki')
plt.legend()
plt.show()
