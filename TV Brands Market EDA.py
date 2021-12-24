#%%
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import warnings
warnings.filterwarnings('ignore') 
# %%
#Load Data
df = pd.read_csv('TV_Final.csv')
# %%
#Exploratory Data Analysis
df.sample(10)
# %%
list(df.columns)
# %%
df.isnull().sum()
# %%
df.shape
# %%
df.dtypes
#%%
df.nunique()
#%%
df['Brand']=df['Brand'].replace('Samsung','SAMSUNG')
# %%
def bar_plot(variable):
    var = df[variable]
    varValue = var.value_counts()
    plt.figure(figsize = (9,3))
    plt.bar(varValue.index, varValue)
    plt.xticks(varValue.index, varValue.index.values)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()
    print("{}:\n{}".format(variable,varValue))
# %%
df.head()
# %%
sns.set_style('darkgrid')
categorical_variables = ['Brand', 'Resolution', 'Operating System', 'Rating']
for v in categorical_variables:
    bar_plot(v)
# %%
def plot_hist(variable):
    plt.figure(figsize = (9,3))
    plt.hist(df[variable], bins = 50)
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{} distribution with histogram".format(variable))
    plt.show()
# %%
numerical_variables = ['Selling Price', 'Original Price', 'Size ']
for m in numerical_variables:
    plot_hist(m)
# %%
#Average Selling Price By Resolution
df_Price = df[['Resolution', 'Selling Price']]
df_grp1 = df_Price.groupby(['Resolution']).mean()
# %%
df_grp1.sort_values('Selling Price', ascending = False)
# %%
df_grp1.plot(kind = 'bar')
# %%
labels = df['Resolution'].value_counts().index
sizes = df['Resolution'].value_counts().values

plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of TVs by Resolution',color = 'black',fontsize = 15)
# %%
df['Operating System'].unique()
# %%
labels = df['Operating System'].value_counts().index
sizes = df['Operating System'].value_counts().values

plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of TVs by Operating System',color = 'black',fontsize = 15)
# %%
sns.scatterplot(x = df['Size '], y = df['Selling Price'])
# %%
sns.barplot(x=df['Resolution'], y=df['Selling Price'])
plt.xticks(rotation="vertical")
plt.show()
# %%
#Average Selling Price By Brand
df_Price = df[['Brand', 'Selling Price']]
df_grp2 = df_Price.groupby(['Brand']).mean()
# %%
df_grp2.sort_values('Selling Price', ascending = False)
# %%
#Average Rating By Brand
df_Rate = df[['Brand', 'Rating']]
df_grp3 = round(df_Rate.groupby(['Brand']).mean().sort_values('Rating', ascending = False), 1)
# %%
df_grp3
# %%
sns.scatterplot(x = df['Rating'], y = df['Selling Price'], hue =  df['Brand'])
# %%
#Selling Price By Operating System
sns.barplot(x=df['Operating System'], y=df['Selling Price'])
plt.xticks(rotation="vertical")
plt.show()
# %%
#Percentage Discount
df['Discount'] = df['Original Price'] - df['Selling Price']
Percent_Disc = round((df['Discount'] / df['Original Price']) * 100, 2)
# %%
#Average Discount By Brand
df_Disc = df[['Brand', 'Discount']]
df_grp4 = round(df_Disc.groupby(['Brand']).mean().sort_values('Discount', ascending = False), 1)
# %%
df_grp4
# %%
