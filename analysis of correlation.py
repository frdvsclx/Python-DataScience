#breast cancer csv analysis from kaggle

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)

df= pd.read_csv("data.csv")
df= df.iloc[:,1:-1]

df.head()

num_cols = [col for col in df.columns if df[col].dtypes in ["int64" , "float64"] ]

#correlation func
cor = df[num_cols].corr()

sns.set(rc={'figure.figsize': (12,12)})
sns.heatmap(cor,cmap="RdBu")
plt.show()
