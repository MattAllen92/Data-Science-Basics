import re
import csv
from bs4 import BeautifulSoup as bs

rawHTML = r'C:\Users\AllenM\Desktop\TGI-Ops\MA Programs\Python Scripts\Practice and Notes\WebScraper\NBA\Cavs - Celtics Box Score HTML.html'

with open(rawHTML) as raw:
    soup = bs(raw)
    
#tables = soup.find('div', attrs={'class':'col-12'})
#print tables

#csv_rows = []
#
#for row in table.find_all('tr'):
#    row_data = []
#    for cell in row.find_all('td'):
#        value = cell.text.replace('&nbsp','')
#        print value