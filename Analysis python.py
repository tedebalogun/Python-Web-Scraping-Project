#!/usr/bin/env python
# coding: utf-8


# Import libraries
import pandas as pd
from __future__ import print_function
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')
import warnings
import seaborn as sns
import pandas_profiling
pandas_profiling.ProfileReport(manufacturetoplist)


# Load data 
manufacturetoplist=pd.read_csv(r"C:\Users\1\Desktop\Python webscraping project\manufacturetoplist.csv")
pd.DataFrame(manufacturetoplist.Headquarters.value_counts(normalize=True))
manufacturetoplist.describe()
Industry_grp=pd.DataFrame(manufacturetoplist.Industry.value_counts(normalize=True))

# manufacturetoplist.describe()

# Revenue distribution

sns.distplot(manufacturetoplist['Revenue (by US$ billion)'], bins=5)

# Top 10 manufacturing companies

manufacturetoplist_top10=manufacturetoplist.head(10)



manufacturetoplist_top10



get_ipython().run_line_magic('matplotlib', 'inline')
manufacturetoplist_top10.plot.barh(x='Company', y='Revenue (by US$ billion)')


# # Group industry 


Industry_grp


get_ipython().run_line_magic('matplotlib', 'inline')
Industry_grp.plot.bar()

 # Count of companies by country


manufacturetoplist_new=manufacturetoplist.rename(columns={'No': 'No', 'Revenue':'Revenue', 'Company':'Company','Industry':'Industry',
                                             'Headquarters':'Headquarters', 'Revenue':'Revenue(by US$ billion)'}, inplace=False)


manufacturetoplist_new[ 'Revenue (by US$ billion)' ].count()


pd.DataFrame(manufacturetoplist.Headquarters.value_counts())

 # Group top companies in US by revenue


country_grp=manufacturetoplist.groupby(['Headquarters'])

Industry_us=country_grp.get_group('United States')


Industry_us.head(10)



get_ipython().run_line_magic('matplotlib', 'inline')
Industry_us.plot.bar(x='Company', y='Revenue (by US$ billion)')

# Group Revenue by country


country_grp[Revenue (by US$ billion)].median()


manufacturetoplist_country=pd.pivot_table(manufacturetoplist, index=[ 'Headquarters'], aggfunc={'Revenue (by US$ billion)':np.sum,})


manufacturetoplist_ind_country=pd.pivot_table(manufacturetoplist, index=[ 'Headquarters','Industry'], aggfunc={'Revenue (by US$ billion)':np.sum,}).head(10)



manufacturetoplist_ind_country



Country_rev=manufacturetoplist.groupby(['Headquarters'])[['Revenue (by US$ billion)']].sum()



Country_rev

get_ipython().run_line_magic('matplotlib', 'inline')
Country_rev.plot.barh()

 # Mean and median Revenue by country

country_grp['Revenue (by US$ billion)'].agg(['median','mean'])

country_grp['Revenue (by US$ billion)'].sum()

Group_rev=country_grp['Revenue (by US$ billion)'].sum()

Group_rev

Group_rev.sort_values

# Plot median revenue by country
plt.figure()
manufacturetoplist.groupby(['Headquarters'])['Revenue (by US$ billion)'].agg(['median']).plot(kind='barh', stacked=True)


company_group=manufacturetoplist.nlargest(5,['Revenue (by US$ billion)'])

company_group


get_ipython().run_line_magic('matplotlib', 'inline')
company_group.plot.barh(x='Company', y='Revenue (by US$ billion)')

sns.catplot(data=company_group, x='Company', y='Revenue (by US$ billion)', hue='Headquarters', kind='bar')

# plot group data bar chart by country

Groupdata=manufacturetoplist.groupby(by='Headquarters').size()

Groupdata

get_ipython().run_line_magic('matplotlib', 'inline')
Groupdata.plot.bar()


sns.stripplot(x='Headquarters', y='Revenue (by US$ billion)', data=manufacturetoplist)

df_manufacturetoplist = manufacturetoplist.groupby(by=['Headquarters'],as_index=False)[['Revenue (by US$ billion)','Industry']].mean().sort_values(by='Revenue (by US$ billion)', ascending=True)

# Plot bar chart by industry

df_manufacturetoplist

sns.barplot('Headquarters', 'Revenue (by US$ billion)', data=df_manufacturetoplist, palette='plasma')

df_manufacturetoplist1.sort_values(by='Revenue (by US$ billion)', ascending=False).head(3)

sns.barplot('Industry', 'Revenue (by US$ billion)', data=df_manufacturetoplist1, palette='plasma')

# Groupby industry and headquarters

manufacturetoplist.loc[filt_manufacturetoplist]['Industry'].value_counts()


manufacturetoplist_group1=manufacturetoplist.groupby(['Headquarters']).sum()


manufacturetoplist_group1

manufacturetoplist_group2=manufacturetoplist.groupby(['Industry']).sum('Revenue (by US$ billion)')

manufacturetoplist_group3=manufacturetoplist.groupby(['Company','Headquarters']).sum()

manufacturetoplist_group3.sort_values('Revenue (by US$ billion)', ascending=False)


# # Top 5 countries by company

manufacture_count = manufacturetoplist['Headquarters'].value_counts().head(5)



manufacture_count = manufacturetoplist['Headquarters'].value_counts().head(5)
sns.set(style="darkgrid")
sns.barplot(manufacture_count.index, manufacture_count.values, alpha=0.9)
plt.title('Frequency Distribution of headquarters companies')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Headquarters', fontsize=10)
plt.show()

