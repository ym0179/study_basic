import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20201116', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))
print(df)
print(df.head())
print(df.tail(1))
print(df.index)
print(df.columns)

print(df.to_numpy()) #index나 column 라벨을 포함 X
print(df.describe()) #quick statistic summary

print(df.T) #행 열 바꾸기
print(df.sort_index(axis=0,ascending=False)) #axis=0 행 기준, axis=1 열 기준
print(df.sort_values(by="B",ascending=False))