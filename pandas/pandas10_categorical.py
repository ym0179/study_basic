import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Categoricals (범주화)
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
print(df)
print(df.dtypes)
# id            int64
# raw_grade    object

df["grade"] = df["raw_grade"].astype("category") #범주형 데이터 
print(df["grade"])
print(df.dtypes)
# id              int64
# raw_grade      object
# grade        category

df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df["grade"])
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df["grade"])
