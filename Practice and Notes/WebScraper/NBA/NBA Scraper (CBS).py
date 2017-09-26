import csv
from bs4 import BeautifulSoup as bs

rawHTML = r"C:\Users\AllenM\Desktop\TGI-Ops\MA Programs\Python Scripts\Practice and Notes\WebScraper\NBA\Cavs - Celtics Box Score (CBS).html"

with open(rawHTML) as raw:
    soup = bs(raw)
    
table = soup.find('div', attrs={'id':'player-stats-away'})

csv_rows = []

for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        value = cell.text.replace('&nbsp','')
        row_data.append(value)
    csv_rows.append(row_data)
    
for row in csv_rows:
    print row
    
with open("./NBA/BOSCLE20170523.csv", "wb") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(csv_rows)