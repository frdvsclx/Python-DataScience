#yeni personaların sirkete ortalamama kazancları projesi

import pandas as pd


pd.set_option("display.max_rows",None)

df= pd.read_csv("datasets/persona.csv")
df.head()
df.info()

df["PRICE"].nunique()
df["PRICE"].value_counts()
'''
PRICE
29    1305
39    1260
49    1031
19     992
59     212
9      200
'''

df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()
'''
COUNTRY
bra    1496
can     230
deu     455
fra     303
tur     451
usa    2065
Name: PRICE, dtype: int64
'''

df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})

df.groupby("COUNTRY").agg({"PRICE": "mean"})
df.groupby("SOURCE").agg({"PRICE": "mean"})

df.groupby(by=["COUNTRY",'SOURCE']).agg({"PRICE": "mean"})
'''
                    PRICE
COUNTRY SOURCE            
bra     android  34.387029
        ios      34.222222
can     android  33.330709
        ios      33.951456
deu     android  33.869888
        ios      34.268817
fra     android  34.312500
        ios      32.776224
tur     android  36.229437
        ios      33.272727
usa     android  33.760357
        ios      34.371703
'''

df.groupby(by=["COUNTRY",'SOURCE',"SEX","AGE"]).agg({"PRICE": "mean"}).head()

agg_df= df.groupby(by=["COUNTRY",'SOURCE',"SEX","AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE",ascending=False)

agg_df= agg_df.reset_index()
agg_df.head()

'''
  COUNTRY   SOURCE     SEX  AGE  PRICE
0     bra  android    male   46   59.0
1     usa  android    male   36   59.0
2     fra  android  female   24   59.0
3     usa      ios    male   32   54.0
4     deu  android  female   36   49.0
'''

agg_df["AGE"].describe()

bins= [0,20,25,30,40,agg_df["AGE"].max()]
mylabels= ['0-20','21-25','26-30','31-40', '41-'+ str(agg_df["AGE"].max())]

agg_df["age_cat"] = pd.cut(agg_df["AGE"],bins,labels=mylabels)
agg_df.head()

'''
  COUNTRY   SOURCE     SEX  AGE  PRICE age_cat
0     bra  android    male   46   59.0   41-66
1     usa  android    male   36   59.0   31-40
2     fra  android  female   24   59.0   21-25
3     usa      ios    male   32   54.0   31-40
4     deu  android  female   36   49.0   31-40
'''

agg_df["customers_level_based"] = agg_df[["COUNTRY","SOURCE","SEX","age_cat"]].agg(lambda x: "_".join(x).upper(),axis=1)
agg_df=agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df.reset_index(inplace=True)
agg_df.head(5)

'''
      customers_level_based      PRICE
0   BRA_ANDROID_FEMALE_0-20  34.798018
1  BRA_ANDROID_FEMALE_21-25  35.269294
2  BRA_ANDROID_FEMALE_26-30  32.976190
3  BRA_ANDROID_FEMALE_31-40  34.898326
4  BRA_ANDROID_FEMALE_41-66  36.737179
'''

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))


agg_df["customers_level_based"].value_counts()
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE":"mean"})

agg_df= agg_df.reset_index()

agg_df.head()

'''
                              PRICE
customers_level_based              
BRA_ANDROID_FEMALE_0-20   34.798018
BRA_ANDROID_FEMALE_21-25  35.269294
BRA_ANDROID_FEMALE_26-30  32.976190
BRA_ANDROID_FEMALE_31-40  34.898326
BRA_ANDROID_FEMALE_41-66  36.737179

'''

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"],4,labels=["D","C","B","A"])
agg_df.head(10)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

'''
             PRICE
SEGMENT           
D        29.078788
C        33.142196
B        34.857879
A        38.263525
'''

#########################################################
#PREDICTIONS:

new_user= "TUR_IOS_FEMALE_21-25"
agg_df[agg_df["customers_level_based"]== new_user]

#here is the prediction:
'''
   customers_level_based      PRICE SEGMENT
78  TUR_IOS_FEMALE_21-25  35.325758       B
'''




