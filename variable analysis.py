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
df2.head(10)
df2.info()

categoric_ones = [col for col in df2.columns if str(df2[col].dtypes) in "category,object,bool"]
"""
['sex',
 'embarked',
 'class',
 'who',
 'adult_male',
 'deck',
 'embark_town',
 'alive',
 'alone']
 """


numeric_but_categoric = [col for col in df2.columns if df2[col].nunique() < 5 and df2[col].dtypes in ["int64","float64"]]

#['survived', 'pclass']


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

#NUMERIC VARIABLES

numeric_ones = [col for col in df2.columns if df2[col].dtypes in ["int64" , "float64"] ]
#['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']

numeric_not_cat = [col for col in numeric_ones if col not in categoric_ones] #['age', 'fare']

#['age', 'sibsp', 'parch', 'fare']

#def num_summary(dataframe_name, numerical_col)

#DEGISKEN YAKALAMAA

#docstring: explaining the fonc
def a(dataframe,cat_th=10,car_th=20):
    """
   the function ...


    Parameters //or arguman
    ----------
    dataframe: dataframe

    cat_th: int,float

    car_th: int,float


    Returns
    -------

    Notes
    -------


    """

def grab_col_names(dataframe, cat_th = 10, car_th=20):

    #categoric tespiti

    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["object","category","bool"]]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes in ["int64","float"]]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and str(dataframe[col].dtypes) in ["object","category","bool"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in  cat_cols if col not in cat_but_car]

    # numeric tespiti

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int64","float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print("categoric",len(cat_cols))
    print("numeric",len(num_cols))
    print("cat but car",len(cat_but_car))
    print("num but cat",len(num_but_cat))

    return num_cols,cat_cols, cat_but_car

num_cols,cat_cols, cat_but_car= grab_col_names(df2)
"""
categoric 13
numeric 2
cat but car 0
num but cat 4
"""

for col in df2.columns:
    if df[col].dtypes== "bool":
        df2[col] =df2[col].astype(int)

#hedef degısken analizi:

df2.groupby("sex")["survived"].mean() #the survival percentage of sex
"""Out[14]: 
sex
female    0.742038 %74..
male      0.188908 %18..
Name: survived, dtype: float64
"""

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}),end="\n\n\n")

target_summary_with_cat(df2, "survived", "sex")

#5666666666666666666666666666666666666666666666666666 the cat say:

for col in df2.columns:
    target_summary_with_cat(df2,"survived",col)

"""
       TARGET_MEAN
alive             
no             0.0
yes            1.0
       TARGET_MEAN
alone             
False     0.505650
True      0.303538
"""

df2.groupby("survived")["age"].mean() #age of survivors
"""
Out[23]: 
survived
0    30.626179 
1    28.343690 
Name: age, dtype: float64
"""

df2.groupby("survived").agg({"age":"mean"})




