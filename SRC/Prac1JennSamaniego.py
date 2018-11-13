
# coding: utf-8

# In[158]:


import requests
import csv
import unicodedata


# In[159]:


from bs4 import BeautifulSoup as BS


# In[160]:


page = requests.get("https://es.wikipedia.org/wiki/Provincias_de_Ecuador")


# In[161]:


page.status_code


# In[162]:


soup = BS(page.content,"html.parser")


# In[163]:


table_wiki = soup.find_all('table', {"class":"sortable"})


# In[164]:


len(table_wiki)


# In[165]:


table_wiki = table_wiki[0]


# In[166]:


provincias=[]

headerList=["Provincia", "Habitantes","Extension","Densidad"]

provincias.append(headerList)


# In[167]:


print(provincias)


# In[168]:


currentIndex=0
for row in table_wiki.findAll("tr"):
    cells = row.findAll('td')
    currentIndex=currentIndex+1
    
    if (currentIndex > 1): # Si tiene más de una provincia
        
        provincia=cells[3].find('a')['href']
        #print (provincia)
            
        habitantes=cells[4].find(text=True)
        #print (habitantes)
            
        extension=cells[5].find(text=True)
        #print (extension)
            
        densidad=cells[6].find(text=True)
        #print (densidad)
        
        #headerList=[provincia,habitantes.encode('utf-8'),extension.encode('ascii','ignore'),densidad.encode('utf-8')]
        headerList=[provincia,
                    unicodedata.normalize('NFKD', habitantes).encode('ascii','ignore'),
                    unicodedata.normalize('NFKD', extension).encode('ascii','ignore'),
                    unicodedata.normalize('NFKD', densidad).encode('ascii','ignore')]
        
        provincias.append(headerList)
        


# In[169]:


print(provincias)


# In[170]:


#csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

with open('provincias_Ecuador.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(provincias)

csvFile.close()

