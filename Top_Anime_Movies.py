
# coding: utf-8

# In[1]:


import requests
import csv
from bs4 import BeautifulSoup


# In[40]:


mname,mlink=list(),list()


# In[47]:


mrating=list()


# In[4]:


response=requests.get("https://www.imdb.com/list/ls050006886/?sort=list_order,asc&st_dt=&mode=detail&page=1")


# In[5]:


soup=BeautifulSoup(response.text,'lxml')


# In[18]:


name=soup.select('h3.lister-item-header a')


# In[25]:


rating = soup.find_all(class_="ipl-rating-star__rating")


# In[41]:


for a,b in zip(name,name):
    mname.append(a.get_text())
    mlink.append("https://www.imdb.com/"+b.get('href'))


# In[54]:


for i in range(0,2300,23):
    mrating.append(rating[i].get_text())


# In[56]:


with open("Imdb_top115_animemovies.csv","w",encoding='utf-8',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Rating","Link"])
    for a,b,c in zip(mname,mrating,mlink):
        writer.writerow([a,b,c])

