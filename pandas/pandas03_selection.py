import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20201116', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))

# print(df["A"]) #이름이 A 인 열 선택 / Series
# print(df[0:2]) #행 기준 슬라이싱
# print(df['20201116':'20201120']) #행 기준 슬라이싱

#Selection by Label (Label 을 통한 선택)
# print(df.loc[dates[0]]) # 1행
# print(df.loc[:,['A','B']]) #전체 데이터 중에 A, B 열 데이터만 추출
# print(df.loc['20201116':'20201117', ['A','B']]) #20201116부터 20201117까지 행의 A, B 열 데이터만 추출
# print(df.loc[dates[0],'A']) #스칼라값 
# print(df.at[dates[0],'A']) #스칼라값 구하기, loc랑 동일하지만 더 빠르게 구하기

#Selection by Position (위치로 선택하기)
# print(df.iloc[3]) #3행
# print(df.iloc[3:5,0:2]) #3,4 번째 행, 0,1번째 열
# print(df.iloc[[1,2,4],[0,2]]) #정수로 표기된 위치값을 기반
# print(df.iloc[1:3,:]) #1,2번째 행, 모든 열
# print(df.iloc[1,1]) #스칼라값 
# print(df.iat[1,1]) #스칼라값 구하기, iloc랑 동일하지만 더 빠르게 구하기

# Boolean Indexing (부울인덱싱)
print(df)
print(df[df.A > 0]) #A열 중에 0보다 큰 값이 있는 행
print(df[df > 0]) #조건에 충족되는 변수만 나오고 아닌건 NaN으로 모든 데이터 출력
df2 = df.copy() #복사
df2['E'] = ['one', 'one','two','three','four','three']
print(df2)
print(df2[df2['E'].isin(['two','four'])]) #E열 중에 'two', 'four'가 있는 행
