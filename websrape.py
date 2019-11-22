

import requests
import urllib.request
import time
import pandas as pd
from bs4 import BeautifulSoup

quote_page = 'http://www.nationmaster.com/country-info/stats/Media/Internet-users'

#page = urllib.urlopen(quote-page)
response = requests.get(quote_page)
print (response.status_code)

soup = BeautifulSoup(response.text, "html.parser")#response.text or .content?

########################
########################actual project
########################
quote_page2 = 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=shrp1&output=tabular&time_zone=edt'

#page = urllib.urlopen(quote-page)
response2 = requests.get(quote_page2)
#print (response.status_code)
#response2.replace('kcfs','')


soup2 = BeautifulSoup(response2.text.replace("kcfs","",-1).replace("ft","",-1), "html.parser")#response.text or .content?
#df2 = pd.read_html(soup2)#the ".read_html" only takes html TABLES...not straight up text
table = soup2.find_all('table')[1]


df2 = pd.read_html(str(table))[0]
print(df2.to_json(orient="records"))

#print(df2.to_json(orient='values'))
#print(df2.to_json)
#print (soup2)
#tables = soup2.find_all('td') 
#print (len(tables))
#table = tables[0]
df = pd.read_html(quote_page2)

#print (df[0].to_json(orient = 'records'))
#print (soup2.find_all('td')[0])
# df = pd.read_html(str(table))
#name_box = soup.find('td',attrs = {'class':'amount'})
#name = name_box
#print (name['class'])
#one_a_tag = soup.findAll('a') #soup.findAll('a')
#link = one_a_tag['href']


