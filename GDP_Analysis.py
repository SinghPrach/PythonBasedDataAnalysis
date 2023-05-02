# Importing Libraries

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


gdp_df = pd.read_csv(r"C:\Users\prach\Desktop\New folder\gdp_data.csv",decimal=',')
print(gdp_df.isnull().sum())
print(gdp_df.describe(include='all'))

# Data Preparation- Missing Values
# Here, we will fill the missing data using the median of the region that a country belongs,
# as countries that are close geologically are often similar in many ways.
gdp_df.groupby('Region')[['GDP ($ per capita)','Literacy (%)','Agriculture']].median()
for col in gdp_df.columns.values:
    if gdp_df[col].isnull().sum() == 0:
        continue
    if col == 'Climate':
        guess_values = gdp_df.groupby('Region')['Climate'].apply(lambda x: x.mode().max())
    else:
        guess_values = gdp_df.groupby('Region')[col].median()
    for region in gdp_df['Region'].unique():
        gdp_df[col].loc[(gdp_df[col].isnull())&(gdp_df['Region']==region)] = guess_values[region]

# Visualizing the data
fig, ax = plt.subplots(figsize=(16,6))
top_gdp_countries = gdp_df.sort_values('GDP ($ per capita)',ascending=False).head(20)
mean = pd.DataFrame({'Country':['World mean'], 'GDP ($ per capita)':[gdp_df['GDP ($ per capita)'].mean()]})
gdps = pd.concat([top_gdp_countries[['Country','GDP ($ per capita)']],mean],ignore_index=True)

sns.barplot(x='Country',y='GDP ($ per capita)',data=gdps, palette='Set3')
ax.set_xlabel(ax.get_xlabel(),labelpad=15)
ax.set_ylabel(ax.get_ylabel(),labelpad=30)
ax.xaxis.label.set_fontsize(16)
ax.yaxis.label.set_fontsize(16)
plt.xticks(rotation=90)
plt.show()

# Looking at the correlation between variables
plt.figure(figsize=(16,12))
sns.heatmap(data=gdp_df.iloc[:,2:].corr(),annot=True,fmt='.2f',cmap='coolwarm')
plt.show()

# Top factors affecting GDP
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20,12))
plt.subplots_adjust(hspace=0.4)

corr_to_gdp = pd.Series()
for col in gdp_df.columns.values[2:]:
    if ((col!='GDP ($ per capita)')&(col!='Climate')):
        corr_to_gdp[col] = gdp_df['GDP ($ per capita)'].corr(gdp_df[col])
abs_corr_to_gdp = corr_to_gdp.abs().sort_values(ascending=False)
corr_to_gdp = corr_to_gdp.loc[abs_corr_to_gdp.index]

for i in range(2):
    for j in range(3):
        sns.regplot(x=corr_to_gdp.index.values[i*3+j], y='GDP ($ per capita)', data=gdp_df,
                   ax=axes[i,j], fit_reg=False, marker='.')
        title = 'correlation='+str(corr_to_gdp[i*3+j])
        axes[i,j].set_title(title)
axes[1,2].set_xlim(0,102)
plt.show()


# Dataset Link: https://thecleverprogrammer.com/wp-content/uploads/2020/05/world.csv
