import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df.head())
print(df.describe())
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

df['Revenue'] = df['Quantity'] * df['Price']

monthly_sales = df.groupby('Month')['Revenue'].sum()
print(monthly_sales)

monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show()
