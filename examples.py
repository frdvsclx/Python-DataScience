import seaborn as sns
import numpy as np
import pandas as pd

pd.set_option('display.width',500)
pd.set_option('display.max_columns',None)

df= sns.load_dataset("car_crashes")

df.columns
df.head()
df.info()

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

#["a" + "_flag" for a in ~df.columns.str.contains("no")]

[col.upper() + "_FLAG" if "no" not in col else col.upper()  for col in df.columns]

#~df.columns.str.contains("abbrev" & "no_previous")

og_list=["abbrev","no_previous"]
new_list=[col for col in df.columns if col not in og_list]
df[new_list].head()

df2= sns.load_dataset("titanic")
df2.head()
df2["sex"].value_counts()

list=["pclass","parch"]
df2[list].nunique() #bu değişkenlere ait kaç çeşit data var mesela alive kısmında yes/no gibi

df2["embarked"].dtype
df2["embarked"]= df2["embarked"].astype("category")
df2["embarked"].value_counts()

df2[df2["embarked"]=='C'].head()
df2[df2["embarked"]!='S'].head(10)

df2[(df2["sex"] == "female") & (df2["age"] < 30)].head(10)

df2[(df2["fare"].astype(int) >500) | (df2["age"] >70)].head(10)

df2.isnull().sum()

df2.drop("who",axis=1)

df2["deck"].mode() #bu en cok tekrar edenden en aza dogru liste olusturur
df2["deck"].fillna(df2["deck"].mode()[0]) #en cok tekrar edeni aradıgımızda
#0. indexini alırız

df2["deck"].fillna(df2["deck"].mode()[0], inplace=True)

df2["age"].fillna(df2["age"].median())




