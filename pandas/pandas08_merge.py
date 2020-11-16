import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Merge (병합)
# 'concat()'으로 Pandas 객체를 연결(concatenating)
df = pd.DataFrame(np.random.randn(10, 4)) #(10,4)
print(df)

# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))

# Join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(pd.merge(left, right, on= 'key'))