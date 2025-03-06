#CATEGORIC VARIABLES

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from xarray.tutorial import load_dataset

pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)

df= sns.load_dataset("diamonds")
df.head()

df["color"].value_counts() #number of variables of the column
df["color"].unique() #variables names
df["color"].nunique() #number of them

df2 = sns.load_dataset("titanic")
df2.info()

categoric_ones = [col for col in df2.columns if str(df2[col].dtypes) in "category,object,bool"]

numeric_but_categoric = [col for col in df2.columns if df2[col].nunique() <5 and df2[col].dtypes in ["int,float"]]

#kardinatilisi yüksek degıskenler: kategorik tür olur ama içinde cok sınıf vardır: örn adlar

def cat_summery(dataframe_name,column_name): #istediğim column degerinin yüzdesini ve degerlerini vericek
    print(pd.DataFrame({column_name: dataframe_name[column_name].value_counts(),
            "Ratio" : 100 * dataframe_name[column_name].value_counts() / len(dataframe_name)}))
    print("$$$$$$$$$$$$$$$$$$$$$$")

[cat_summery(df2,col) for col in categoric_ones ]