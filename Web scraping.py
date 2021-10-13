#!/usr/bin/env python
# coding: utf-8

# # Import BeautifulSoup, requests , pandas and scrap data from Wikipedia

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue'
response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')
table=soup.find('table',{'class':'wikitable sortable plainrowheads'}).tbody
rows=table.find_all('tr')
columns=[v.text.replace('\n', '')for v in rows[0].find_all('th')]
df=pd.DataFrame(columns=columns)
for i in range(1, len(rows)):
    tds=rows[i].find_all('td')
    if len(tds)==4:
        values=[tds[0].text, tds[1].text, '', tds[2].text, tds[3].text.replace('\n',''.replace('\xa0',''))]
    else:
        values=[td.text.replace('\n','').replace('\xa0','') for td in tds]
    df=df.append(pd.Series(values,index=columns), ignore_index=True)
    df.to_csv(r 'C:\Users\1\Documents\Web scraping project' +
              '\\ManufactureToplist.csv', index=False)


# In[6]:





# In[ ]:




