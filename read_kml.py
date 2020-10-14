
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


with open ('your file here') as f:
    doc=f.read()
soup = BeautifulSoup(doc, 'xml')
locs=soup.find_all("Placemark")
# names=locs.find_all("name")
names=[]
lat=[]
long=[]
for eachtakeaway in locs:
    nametag = eachtakeaway.find('name')
    nametag = remove_html_tags (str(nametag))
    loctag = eachtakeaway.find('coordinates')
    loctag = remove_html_tags (str(loctag))
    loctag = loctag[:-2]
    loc=loctag.split(',')
    names.append(nametag)
    lat.append(loc[0])
    long.append(loc[1])

data = {
    'Names': names, 
    'Latitude': lat,
    'Longitude': long,
}
df=pd.DataFrame(data)
df=df.drop_duplicates()
df.to_excel("location.xlsx",index=False)  
