import selenium
import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv('indexes/nasdaq100.csv')

cap = []
high = []
low = []
sectors = []

for i in df['SYMBOL']:
    print(i)
    url = 'https://finance.yahoo.com/quote/' + i
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    try:
        capitalization = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[8].text
    except:
        capitalization = ''
    try:
        high_52 = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[5].text.split()[0]
    except:
        high_52 = ''
    try:
        low_52 = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[5].text.split()[2]
    except:
        low_52 = ''
    try:
        sector = soup.find('p', class_ = 'D(ib) Va(t)').find('span', class_ = 'Fw(600)').text
    except:
        sector = ''

    try:
        cap.append(capitalization)
        high.append(high_52)
        low.append(low_52)
        sectors.append(sector)
    except:
        cap.append('')
        high.append('')
        low.append('')
        sectors.append('')
    

df['Capitalization'] = cap
df['High 52 Weeks'] = high
df['Low 52 Weeks'] = low
df['Sector'] = sectors
df['Index'] = 'Nasdaq 100'
    
df.to_csv('indexes/nasdaq 100.csv', index=False)