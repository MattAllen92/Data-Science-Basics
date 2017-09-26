import csv
#import requests as rq
from bs4 import BeautifulSoup as bs

# extract HTML (request code commented out because firewall blocks it)
#url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
#response = rq.get(url)
#html = response.content
rawHTML = r"C:\Users\AllenM\Desktop\TGI-Ops\MA Programs\Python Scripts\Practice and Notes\WebScraper\Boone County Jail HTML.html"

with open(rawHTML) as raw:
    soup = bs(raw)

# extract table
table = soup.find('tbody', attrs={'class':'stripe'}) # find tbody record with 'stripe' class

# create list for CSV
csv_rows = []
                 
# iterate through rows then cols
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        cell_text = cell.text.replace('&nbsp;','') # extract cell text (clearing HTML fluff)
        if "Details" not in cell_text:
            row_data.append(cell_text) # build respondent row data
    csv_rows.append(row_data) # add respondent to final csv data                                                        

with open("./inmates.csv", "wb") as outfile: # wb = write and binary (opens file in binary mode, preventing Python from
    writer = csv.writer(outfile)                                    # altering eof chars etc. and corrupting CSV files)
    writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
    writer.writerows(csv_rows)