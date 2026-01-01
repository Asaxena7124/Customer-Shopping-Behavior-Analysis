import pandas as pd 

df = pd.read_csv('customer_shopping_behavior.csv')
# import os
# print(os.getcwd())

# print(df.head())
# print(df.info())
# print(df.describe(include='all'))
# print(df.isnull().sum())
# Now Finding the median of review rating in each category and replace it with null values 
# With this technique that the footwear category null rating will filled by its median value not the median of other category and its meaningful 


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))

# NOw check if there is any nullvalues still left 

# print(df.isnull().sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)


# Create a column age_group

labels = ['Young Adult','Adult','Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']].head(10))

# create column purchase_frequency_days

frequency_mapping = {
'Fortnightly': 14,
'Weekly': 7,
'Monthly': 30,
'Quarterly': 90,
'Bi-Weekly': 14,
'Annually': 365,
'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
# print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))


print(df[['discount_applied','promo_code_used']].head(10))

# check if one of the column is redundant
print((df['discount_applied'] == df['promo_code_used']).all())

# drop one of them
df = df.drop(columns=['promo_code_used'],axis=1)
print((df.columns)=='promo_code_used')

