#!/usr/bin/env python
import json
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd


data=[]

url="https://howrare.is/drops"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}

r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

rows=soup.findAll('tbody')

data=[]
for row in rows:
    #a=row.find('td').text
    #a = getattr(row.find('td'),'text',None)
    #print(a)
#    print(row)
    for r in row.findAll('tr'):
        d=dict()
        d['nom']=(r.select('td:nth-child(1)'))
        data.append(d)
        print(d['nom'])

"""  
   for row in rows:
    d=dict()
    d['nom']=row.select_one('td:nth-child(1)').text.strip()
    
    data.append(d)

with open('data.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

rows = soup.findAll('table')
#print(rows)

for row in rows:
    
    row.findAll('td[scope="row"]')
    
    print(row)
    for r in row:
    
        d=dict()
        
        d['nom']=row.select_one('td:nth-child(1)').text.strip()
    
    data.append(d)
    
with open('data.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

#   for r in row:
        #print(r.select_one('td:nth-child(1)'))
    #print(row.select_one('td:nth-child(1)').text)
    #for r in rows:
    #    print(r.select("td:nth-child(1)"))
"""