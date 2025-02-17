###büyük data setlere genel bakıs###

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('displays.max_columns',None)
pd.set_option('display.width', 500)

df=sns.load_dataset("titanic")
df.head()

"""
df2.head() #ilk 5elemanı verir
df2.tail() #son 5 elemanı verir
df2.shape #boyutu (891, 15)
df2.info() #değişkenlerin tipler gibi detaylı bilgi için
####object yani katagorik değişken demektir category de vardır
df2.columns #değişken isimlerini listeler
df2.index #aralıgını verir RangeIndex(start=0, stop=891, step=1)
df2.describe().T #.T trasnpozunu al demektir #sayısal edgıskenlerı betımleme
#describe methodu df i özetler

df2.isnull().values.any() #isnull boş olup olmadıgına bakar, values true/falselardan olusan bi numpy array yapar
#any ifadesi de var mı yok mu diye sorar
df2.isnull().sum() #true ve false toplamını ayrı ayrı yazar -dataframedeki nerede eksik var görülür-
"""

def check_df(dataframe, head=5):
        print("###size###")
        print(dataframe.shape)
        print("###missing###")
        print(dataframe.isnull().sum())
        print("###info###")
        print(dataframe.info())
        print("###head###")
        print(dataframe.head(head))

df2= sns.load_dataset("tips")
check_df(df2,5)
