import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 일반적으로 연산은 missing data(결측치)를 제외
dates = pd.date_range('20201116', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))
print(df.mean()) #열 별 mean(평균)
print(df.mean(1)) #행 별 mean(평균)