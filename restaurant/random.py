import numpy as np
import pandas as pd

df = pd.read_csv("TA_restaurants_curated.csv")
df = df.fillna(value="No Info")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
x = np.random.randint(0, 1666)
result = df.iloc[x]
print(result)