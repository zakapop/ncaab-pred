import requests
import pandas as pd
from bs4 import BeautifulSoup

URL_END_SEASON_STATS = 'https://www.teamrankings.com/ncb/team-stats/'
URL_END_SEASON_BASE = 'https://www.teamrankings.com'

# Retrieve end of season stats for each team
end_season_site_req = requests.get(URL_END_SEASON_STATS).content
end_season_html_sp = BeautifulSoup(end_season_site_req.decode('utf-8', 'ignore'), 'lxml')

# Define replacements for long strings
str_repl = {
    'opponent': 'opp',
    'offensive': 'off',
    'defensive': 'def',
    'field-goals': 'fg',
    'possessions': 'poss',
    'overtime': 'ot',
    'personal': 'pers',
    'first-half': 'h1',
    'second-half': 'h2',
    'free-throw': 'ft',
    'three-point': '3p',
    'two-point': '2p',
    'rebounds': 'reb',
    'blocks': 'blk',
    'turnover': 'trno',
    'shooting': 'sht',
    'efficiency': 'eff',
    'points-per-game': 'ppg',
    'total': 'total',
    'average': 'avg',
    '-of': '',
    'margin': 'marg',
    'attempted': 'att',
    '--': '-',
    'possession': 'poss',
    'rebounding': 'reb',
    'percent': 'pct',
    'per-game': 'pg',
    'ratio': 'rat',
    'field-goal': 'fg',
    'points': 'pts',
    '2-pointers': '2p',
    '3-pointers': '3p',
    'effective': 'eff'

}

def replaceString(str, repl):
    for key, replacement in repl.iteritems():
        if key in str:
            str = str.replace(key, replacement)
    return str

# Scrape all links from page
all_links = end_season_html_sp.find_all('a', href=True)
stat_links = []
for link in all_links:
    if '/ncaa-basketball/stat/' in link['href']:
        stat_link = URL_END_SEASON_BASE + link['href']
        #print link['href']
        stat_base = replaceString(link['href'].rsplit('/')[-1], str_repl)
        stat_links.append({'link': stat_link, 'stat_base': stat_base})

test_link = stat_links[0]['link']
test_req = requests.get(test_link).content
test_sp = BeautifulSoup(test_req.decode('utf-8', 'ignore'), 'lxml')

#print test_sp.prettify('latin-1')

stat_table = test_sp.find_all('table')
print stat_table

