#CATEGORIC VARIABLES

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

numeric_but_categoric = [col for col in df2.columns if df2[col].nunique() <10 and df2[col].dtypes in ["int,float"]]

#kardinatilisi yüksek degıskenler: kategorik tür olur ama içinde cok sınıf vardır: örn adlar

def cat_summary(dataframe_name,column_name, plot= False): #istediğim column degerinin yüzdesini ve degerlerini vericek
    print(pd.DataFrame({column_name: dataframe_name[column_name].value_counts(),
            "Ratio" : 100 * dataframe_name[column_name].value_counts() / len(dataframe_name)}))
    print("$$$$$$$$$$$$$$$$$$$$$$")

    if plot:
        sns.countplot(x= dataframe_name[column_name], data= dataframe_name)
        plt.show(block=True)


[cat_summary(df2,col) for col in categoric_ones]

cat_summary(df2,"sex",plot=True) #male ve female grafiği

[cat_summary(df2,col,plot=True) for col in categoric_ones] #katagorik degiskenlerin grafiği

df2["adult_name"].astype(int) #true-false ---> 0,1


