from bs4 import BeautifulSoup
import sys
if sys.version_info[0] > 2:
    import urllib.request
else:
    import urllib2

class Leaderboard():
    def __init__(self, positions):
        self.positions = positions
    
class User():
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = clan
        self.honor = honor
    
def get_html(url):
    if sys.version_info[0] > 2:
        with urllib.request.urlopen(url) as response:
            return response.read()
    return urllib2.urlopen(url).read()

def get_table(html):
    return BeautifulSoup(html).find('table')

def solution():
    table = get_table(get_html('https://www.codewars.com/users/leaderboard'))
    positions = {}
    i = 0
    for row in table.find_all("tr")[1:]:
        clan, honor = row[-2:]
        name = row.attrs['data=username']
        positions[i] = User(str(name), clan.text, int(honor.text))
        i += 1
    return Leaderboard(positions)

print solution()