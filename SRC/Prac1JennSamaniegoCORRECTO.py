
# coding: utf-8

# In[274]:


import requests
import csv
import unicodedata


# In[292]:


from bs4 import BeautifulSoup as BS


# In[293]:


page = requests.get("https://es.wikipedia.org/wiki/Provincias_de_Ecuador")


# In[294]:


page.status_code


# In[295]:


soup = BS(page.content,"html.parser")


# In[296]:


table_wiki = soup.find('table', {"class":"sortable"})


# In[297]:


len(table_wiki)


# In[298]:


provincias=[]

headerList=[u"Provincia", u"Habitantes",u"Extension",u"Densidad"]

provincias.append(headerList)


# In[299]:


print(provincias)


# In[306]:


import codecs
f = codecs.open('provincias_test.csv','wb',encoding='windows-1254')
f.write('"Provincia","Habitantes","Extension","Densidada","link"\n')
for row in table_wiki.findAll("tr")[1:]: #descartamos indice 0
    cells = row.findAll('td')
           
    provincia=cells[3].findAll('a')[1]
    ##print provincia.getText()
    habitantes=cells[4].find(text=True)
    #print (habitantes)

    extension=cells[5].find(text=True)
    #print (extension)

    densidad=cells[6].find(text=True)
    #print (densidad)
    link=cells[3].findAll('a')[1]
    ##print link.get("href")

  

    f.write(u'"{provincia}","{habitantes}","{extension}","{densidad}","{link}"\n'.format(provincia=provincia.getText(),habitantes=habitantes.replace('&nbsp;',''),extension=extension.replace('&nbsp;',''),densidad=densidad.replace('&nbsp;',''), link= u"https://es.wikipedia.org%s" % link.get("href")))
   
f.close()

