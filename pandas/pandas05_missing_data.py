import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas는 missing data(결측치)를 표현하기 위해 주로 np.nan 값을 사용
dates = pd.date_range('20201116', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))
print(df)
# reindex로 지정된 축 변경/추가/삭제, 데이터 복사본 반환
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E']) #index 0-3행, Nan값이 있는 E 열 추가
print(df1)
df1.loc[dates[0]:dates[1],'E'] = 1 # dates[1]행 까지 E열 값 1.0으로 변환 (NaN은 float)
print(df1)

# 결측치 처리
print(df1.dropna(how='any')) #결측치 있는 행 지우기
print(df1.dropna(axis=1))  #결측치 있는 열 지우기
print(df1.fillna(value=5)) #결측치 5로 채우기
print(pd.isna(df1)) #결측치 있으면 True 표시
print(df1.replace(np.nan, 1.5)) #결측치 1.5로 대체
print(df1.replace([np.nan, 1.0], [1.5,'a'])) #결측치 1.5, 1.0은 'a'로 대체
