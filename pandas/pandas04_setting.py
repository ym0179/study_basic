import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20201116', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20201116', periods=6))
print(s1)

df['F'] = s1
print(df)
df.at[dates[0],'A'] = 0 #라벨에 따라 값 설정 (=loc)
print(df)
df.iat[0,1] = 0 #위치에 따라 값 설정 (=iloc)
print(df)
print(len(df))
df.loc[:,'D'] = np.array([5] * len(df)) # 5 6개
print(df)

df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)