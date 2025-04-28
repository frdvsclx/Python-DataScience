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

cor_matrix = df[num_cols].corr().abs()#positive

#for repetitive data
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool_))

#if cor is higher that .90 delete it
drop_list =[col for col in upper_triangle_matrix if any(upper_triangle_matrix[col] > .90)]

cor_matrix[drop_list]
df.drop(drop_list, axis=1)

def high_correlated_cols(dataframe,plot=False,corr_th=0.90):
    numerical_col=[col for col in dataframe.columns if dataframe[col].dtype in [int,float]  ]
    corr=dataframe[numerical_col].corr()
    corr_matrix=corr.abs()
    upper_triangle_matrix=cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list=[col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90) ]

    if plot:
        sns.set(rc={'figure.figsize': (15,15)})
        sns.heatmap(corr,cmap="RdBu")
        plt.show()
    return drop_list


high_correlated_cols(df)
drop_list=high_correlated_cols(df)
df.drop(drop_list,axis=1)
high_correlated_cols(df.drop(drop_list,axis=1), plot=True)

