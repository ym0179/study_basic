import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Series
s = pd.Series([1,3,5,np.nan,6,8]) #s = pd.Series(data, index=index)
# 만약 데이터가 scalar 값이라면 index를 꼭 넣어줘야함
s = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
#slicing
print(s)
print(s[0]) # 첫 행 값
print(s[:3]) # 0번째부터 2번째까지 행
print(s[s > s.median()]) # s안에 값들의 median 보다 큰 값을 가지고 있는 행
print(s[[4, 3, 1]]) #행 index가 4, 3, 1인 행
print(np.exp(s))

# DataFrame
dates = pd.date_range('20201116', periods=6) #20201116부터 6개의 날짜 데이터 생성
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD')) #(6,4) 행렬
# np.random.randint(n) : (시작, n-1) 사이의 랜덤숫자 1개 뽑기
# np.random.rand(m,n) : 0~1 의 균일분포 난수를 matrix array (m,n) 생성
# np.random.randn(m,n) : 평균 0, 표준편차 1의 가우시안 표준정규분포 난수를 matrix array (m,n) 생성
print(df)

df2 = pd.DataFrame({
    'A': 1., #float 데이터 타입
    'B': pd.Timestamp('20201116'), #날짜형식 데이터
    'C': pd.Series(1,index=list(range(4)),dtype='float32'), #float 데이터 타입
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]), #categorical 데이터 타입
    'F' : 'foo' 
})
print(df2)
print(df2.dtypes)
'''
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
'''