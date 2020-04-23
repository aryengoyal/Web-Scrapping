
# coding: utf-8

# In[2]:


#Scrapy is an application framework for crawling web sites and extracting 
#structured data(originally built for web scraping but now used for web crawling)


# In[23]:


from bs4 import BeautifulSoup
import requests
import csv
import pprint


# In[60]:


response = requests.get('https://www.flipkart.com/search?q=nokia+smartphones&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=nokia+smartphones&requestId=675612e2-512b-4d0e-8b75-6bdf91921d7c&as-backfill=on')


# In[61]:


response


# In[62]:


soup = BeautifulSoup(response.text,'lxml')


# In[76]:


mname,mprice,mrating,mdes=list(),list(),list(),list()


# In[67]:


mobname= soup.find_all(class_="_3wU53n")


# In[68]:


mobprice = soup.find_all(class_="_1vC4OE _2rQ-NK")


# In[69]:


mobrating = soup.find_all(class_="hGSR34")


# In[70]:


mobdes = soup.find_all(class_="vFw0gD")


# In[77]:


for a,b,c,d in zip(mobname,mobprice,mobrating,mobdes):
    mname.append(a.get_text())
    mprice.append(b.get_text())
    mrating.append(c.get_text())
    mdes.append(d.get_text())


# In[82]:


with open('nokiaphone.csv','w',encoding="utf-8",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name',"Price","Rating","Description"])
    for a,b,c,d in zip(mname,mprice,mrating,mdes):
        writer.writerow([a.strip(),b.strip(),c.strip(),d.strip()])

