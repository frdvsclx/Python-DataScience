#ekonometri ve finasn için dogdu ama sonradan veri analitiğind asık kullanılır, cok kullanılır

import pandas as pd
import seaborn as sns

pd.Series([56,34,23,21])
#cıktısı
#0    56
#1    34
#2    23
#3    21
#dtype: int64

a= pd.Series([23,45,65,34])
type(a) #pandas.core.series.Series
a.index #RangeIndex(start=0, stop=4, step=1) 0dan 4e 1er 1er giden index
a.dtype #dtype('int64')
a.size #eleman sayısı verir
a.ndim #boyutu veiri
a.values #array([23, 45, 65, 34] cıktı aynı zamnda numpy.arraydir
a.head(2) #ilk iki degeri getirir
a.tail(3) #son 3 elemanı getirir

########VERİ OKUMA######
#örn csv, text,excel dosyaları okuyabilir

df= pd.read_csv("datasets/username.csv") #read_ dan sonraki kısım değişebilir
df.head() #ile dataframe e bakarım
###EGER CRTL İLE PD ÜZERİNE GELİRSEM BASKA KULLANIMLARI DA GÖREBİLİRİM(aintnoway)



df2 = sns.load_dataset("titanic")
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

df2["sex"].value_counts() #cinsiyetlerin arasından kadın ve erkek sayısını ögrenirim

df2[0:10]
df2.drop(2,axis=0) #satırlardan 2. indexi sil demektir 0,1,3..
df2.drop([2,4,5,6,7,8,9,],axis=0) #gibi bir liste içinde de index verebilriiz

 #kalıcı olması için atama yapılabilir df2 = df2.drop([2,4,5,6,7,8,9,],axis=0)
# ya da inplace kullanılablir df2.drop([2,4,5,6,7,8,9,],axis=0,inplace= True    )


######DEGISKENLERI INDEX'E CEVIRMEK##########

df2["age"].head()
df2.sex.head() #şeklinde istenilen degıskenler secılebilir

df2.index = df2["age"] #bu şekilde index bilgisine age in degerlerini atabilirim
df2.drop("age",axis=1,inplace=True) #age sutünunu sil demektir, kalıcı sildik
df2.head()

#eklemek istersek:
df2["age"] = df2.index #eger yazıdıgım sey içidne yoksa dfin ona eklenir, age diye bir degısken sutunu var artık
df2.head()

#ya da resetleyrek silinenleri geri getirebliriz
df2.reset_index()
df2 = df2.reset_index() #atayarak kalıcı hale getırdım

"age" in df #age degıskenı içinde var mı diye sorar, true false döner

df3 = sns.load_dataset("titanic")
df3[["age"]].head()
type(df3["age"].head()) #pandas.core.series.Series cıktısı gelir SERIES OLARAK CIKTI
type(df3[["age"]].head()) #pandas.core.frame.DataFrame cıktısı gelir DATAFRAME

df3["pclass2"] = df3["pclass"]**2 #yeni pclass2 degerleri onun karelerini almıs hali olacak

df3["pclass3"] = df3["pclass"] / df3["pclass2"]
df3.drop("pclass3", axis=1).head() #pclass3ü sildim ve ilk5 yazdırdım

listeadi= ["sex","age"]
df3.drop(listeadi, axis=1).head() #silme işlemini birden fazla yere uygulayacaksam liste şeklinde yazbilirim

####SEÇİİİİİİİİİM YAPMA############

df3.loc[:,df3.columns.str.contains("pclass")].head() #içinde pclass kelimesini
#içeren strleri getir demek ####burada degıldır demek için dalgalı - sey kulanılır
#contains: bunu içeriyor mu kontrol eder

#iloc vs loc farkı
#iloc= integer based selection / loc = label based selection demektir
#loc direk ne yazarsam ona göre seçim yapar

df3.iloc[0:3] #0,1,2. satırları yazdırdı
df3.columns
df3.iloc[2,3] #2.idex satırında 3.idex sütunundanki değerş verir
#ilocda str bir şey gielmezsin

df3.loc[0:3] #burada 3.indexde dahil yazdırır
df3.loc[0:3,listeadi] #listedeki değişkenleri 0,1,2,3. satırlanırı yazdırdı

df3[df3["age"]>40 ].count() #40tan buyuk kac data var?
df3[df3["age"]>40 ]["age"].count()

df3.loc[df3["age"]>50, ["age","sex","pclass"]].head()

df3.loc[(df3["age"]>50) & (df3["sex"]=="male"), ["age","sex","pclass"]].head()

#aggregation and grouping: özet istatiksel bilgi veren fonksiyonlar

#bazı aggregation fnksiyonarı:

df3.groupby("sex")["age"].mean()  #cinsiyete göre yaş ortalamsı aldırır

df3.groupby("sex").agg({"age": ["sum","mean"],
                        "survived": ["mean"] }) #cinsiyete göre yaşların ortalamsını ve toplamını ver


df3.groupby(["sex", "embark_town", "class"]).agg({"age": ["sum","mean"],
                        "survived": ["mean"],
                        "sex": ["count"]})

pd.set_option('display.max_columns', None)
df4=sns.load_dataset("titanic")
df4.head()

###PIVOT TABLE $$$$$

df4.pivot_table("survived", "sex","embarked") #kesişim,satır,sutün
#kesişimde survived ın ortalası vardır cunku, pivot mean'i ön tanımlıdır

df4.pivot_table("survived", "sex","embarked", aggfunc="std") #dersem bu sefer
# kesişmde standart sapma hesaplar


df4.pivot_table("survived", "sex",["embarked", "class"])
#burada sutün kısmında hem yer hem sınıfı yazar

df4["new_age"] = pd.cut(df4["age"],[0,10,18,25,40,90]) ##aralıklara böler
df4["new_age"] = pd.qcut(df4["age"]) #secılen veriyi çeyrek halinde verir

df4.pivot_table("survived","sex", ["new_age","class"], aggfunc= ["mean","count"])
#burada hem kadın erkek yaşama ortalamasını alır, hem kaç kişi onu verir

pd.set_option('display.width',500)

# "~" BU->  ALT TUŞU+ NUMLOCK 0126 İLE YAPILIYO OMMGGGGGG


#####APPLY VE LAMBDA YAPILARI########
##apply toplu olarak fonksiyon uygulamaya yarar,
###lamda ise kullan-at fonksiyonlardır, bir kere kullanılıp atılıt


df4= df4.drop("new_age",axis=1)
df4["age1"] = df4["age"]**2
df4.head()

for col in df4.columns:
    if "age" in col:
        print((df4[col]/10).head())

for col in df4.columns:
    if "age" in col:
        df4[col] = df4[col]/10


df4.loc[:, df4.columns.str.contains("age")].apply(lambda x:x/10).head()

df4.loc[:, df4.columns.str.contains("age")].apply(lambda x: (x-x.mean()/x.std())).head()
#burada age içeren columnlar alınır, lambdadan sonra yazdıgın sey cıktısını almak ıstedıgın sey

def colums_std(col):
    return col-col.mean()/col.std()

df4.loc[:, df4.columns.str.contains("age")].apply(colums_std).head()

import numpy as np
import pandas as pd

a= np.random.randint(1,30,size=(3,3))
df5= pd.DataFrame(a,columns=["var1","var2","var3"])
df6= df5 + 31

pd.concat([df5,df6 ],ignore_index=True)

df['Yaş Kategorisi'] = df['Yaş'].apply(lambda x: 'Genç' if x < 30 else ('Orta yaşlı' if x <= 60 else 'Yaşlı'))
#########merge ile birleştirme işlemlerii#####


