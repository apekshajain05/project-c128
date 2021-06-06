import requests
from bs4 import BeautifulSoup
import pandas as pd

starturl='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'


star_data=[]

page=requests.get(starturl)

soup=BeautifulSoup(page.text,'html.parser')
table=soup.find_all('table')

table_rows=table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    star_data.append(row)

# print(star_data)

star_names = []
distance =[]
mass = []
radius =[]

for i in range(1,len(star_data)):
    star_names.append(star_data[i][0])
    distance.append(star_data[i][5])
    mass.append(star_data[i][7])
    radius.append(star_data[i][8])
    
    
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])
# print(df)

df.to_csv('project-c128.csv')
