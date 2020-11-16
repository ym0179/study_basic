import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Grouping (그룹화)
'''
그룹화는 다음 단계 중 하나 이상을 포함하는 프로세스를 나타냄

- 어떤 기준에 따라 여러 그룹으로 데이터 분할(Splitting)
- 각 그룹에 독립적으로 함수(function) 적용(Applying)
- 결과물들을 하나의 자료구조로 결합(Combining)
'''
df = pd.DataFrame(
    {
        'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
        'C' : np.random.randn(8),
        'D' : np.random.randn(8)
    })
print(df)

print(df.groupby('A').sum()) #A 열의 값별로 그룹화 하고 각 그룹에 sum()함수 적용
print(df.groupby(['A', 'B']).sum()) #여러 열을 기준으로 그룹화 -> 계층적 index 형성