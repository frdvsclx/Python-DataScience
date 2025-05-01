###VERİ GÖRSELLEŞTİRME#####
#kategorik değişken: sütun grafiği[seaborn->countplot // matlib-> bar ile gercekleştirilir]
###sayısal değişkenler için: histogram, boxplot  grafikleri kullanılabilir
#####veri görselleştirmek için-> power bı//tableau//qlikview buna daha uygundur


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wheel.metadata import pkginfo_to_metadata

pd.set_option('display.width',500)
pd.set_option('display.max_columns',None)

df= sns.load_dataset("titanic")
df.head(10)

df["sex"].value_counts().plot(kind="bar") ##cinsiyet verisini sütun grafiğine gösterir
plt.show() ##cıktı alınır

plt.hist(df["age"]) #yaslara göre histogram dagılımı
plt.show()

plt.bar()

#fare: yolculuk ücreti
plt.boxplot(df["fare"]) #aykırı değerleri bulmakta iyi
plt.show()

#y=x^2 grafigi:
x= np.array([1,2,3,4,5,6,7,8,9,10])
y= np.array([2,4,8,16,32,64,128,256,512,1024])
plt.plot(x,y) #aynı indexleri birlestirir
plt.plot(x,y,"o") #dot koyar
plt.show()


'''
import matplotlib.pyplot as plt

notlar = [68, 74, 82, 90, 78, 85, 92, 88, 76, 61, 79, 73, 89, 81, 72, 95, 70, 83, 77, 75]

plt.hist(notlar, bins=10, edgecolor='r', alpha=0.7)
plt.xlabel('Notlar')
plt.ylabel('Frekans')
plt.title('Sınav Notları Dağılımı')
plt.show()
'''