
# coding: utf-8

# In[1]:


import requests
import csv
from bs4 import BeautifulSoup


# In[147]:


mname,mrating,myear=list(),list(),list()


# In[72]:


response=requests.get("http://www.imdb.com/chart/top")


# In[74]:


soup=BeautifulSoup(response.text,'lxml')


# In[112]:


name=soup.select('td.titleColumn')
rating=soup.find_all('strong')
year=soup.find_all(class_="secondaryInfo")


# In[148]:


for a,b,c in zip(name,rating,year):
    mname.append(a.get_text()[16:])
    mrating.append(b.get('title')[0:3])
    myear.append(c.get_text()[1:5])


# In[150]:


with open("imdb_top250_movies.csv","w",encoding='utf-8',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Rating","Year"])
    for a,b,c in zip(mname,mrating,myear):
        writer.writerow([a,b,c])

