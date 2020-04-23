
# coding: utf-8

# In[1]:


import requests
import csv
from bs4 import BeautifulSoup


# In[60]:


sname,ssinger,slink=list(),list(),list()


# In[3]:


response = requests.get('https://www.youtube.com/watch?v=eH4F1Tdb040&list=RDeH4F1Tdb040&start_radio=1&t=0')


# In[4]:


response


# In[6]:


soup=BeautifulSoup(response.text,'lxml')


# In[40]:


name= soup.find_all(class_="yt-ui-ellipsis yt-ui-ellipsis-2")


# In[51]:


singer=soup.find_all(class_="video-uploader-byline")


# In[63]:


link= soup.find_all(class_=" spf-link playlist-video clearfix yt-uix-sessionlink spf-link ")


# In[65]:


link[0].get('href')


# In[71]:


for a,b,c in zip(name,singer,link):
    sname.append(a.get_text().strip())
    ssinger.append(b.get_text().strip())
    slink.append('https://www.youtube.com'+c.get('href'))


# In[73]:


with open("Crossfire_Playlist.csv",'w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name','Composer','Link'])
    for a,b,c in zip(sname,ssinger,slink):
        writer.writerow([a,b,sc])

