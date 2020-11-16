import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Apply (적용하기): 데이터에 기능 적용
dates = pd.date_range('20201116', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))
print(df)
print(df.apply(np.cumsum)) #열 기준으로 누적 합 계산
#np.cumsum: 배열에서 주어진 축에 따라 누적되는 원소들의 누적 합을 계산
print(df.apply(lambda x: x.max() - x.min()))

# Histogramming (히스토그래밍)
s = pd.Series(np.random.randint(0, 7, size=10))
print(s.value_counts())
print(df["C"].value_counts()) #df 에서는 안되고 시리즈 에서만 됨


# String Mathods (문자열 메서드)
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())