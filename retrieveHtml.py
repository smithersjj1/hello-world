

import requests
import urllib.request
import time
import pandas as pd
from bs4 import BeautifulSoup



htmlData = 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=shrp1&output=tabular&time_zone=edt'


responseHtml = requests.get(htmlData)
print(responseHtml.status_code)



soup2 = BeautifulSoup(responseHtml.text.replace("kcfs","",-1).replace("ft","",-1), "html.parser")#response.text or .content?

table = soup2.find_all('table')[1]

table.
df2 = pd.read_html(str(table))[0]
#print(df2.to_json(orient="records"))


df = pd.read_html(htmlData)




