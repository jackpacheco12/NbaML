# import needed libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
# create a function to scrape team performance for multiple years

import requests
from bs4 import BeautifulSoup

def games_month(year, month):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html"
    
# Send an HTTP request to the URL and get the content
    response = requests.get(url)
    html_content = response.content

    print(html_content)
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    print("aljlskdjf")
    # Find all rows within tbody
    rows = soup.select('tbody tr')
    print(rows)
    # Iterate through rows and extract csk attribute
    csk_values = [row.th.get('csk', '') for row in rows]
    return csk_values

games = games_month(2024, "october")





def make_url(game):
    url = f"https://www.basketball-reference.com/boxscores/{game}.html"
    return url 

url = make_url(games[0])
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
target_row = soup.find_all('tfoot')

lst_values = []
for i in range(len(games)): 
    url = make_url(games[i])
    response = requests.get(url)
    html_content = response.content
    # Find the h1 element within the specified context
    soup = BeautifulSoup(html_content,'html.parser')
    h1_text = soup.select_one('#content h1').get_text(strip=True)
    Away = h1_text.split("at")[0]
    Home = h1_text.split("at")[1].split("Box Score")[0]



    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <tfoot> element
    target_row = soup.find('tfoot')

    target_row = soup.find_all('tfoot')
    #print(target_row[0])
    

    tfoot_elements = soup.find_all('tfoot')

    # Iterate through each tfoot element
    for tfoot_element in tfoot_elements:
        # Find the tr element with data-row="13" within the current tfoot
        target_row2 = tfoot_element.find('tr', {'data-row': '13'})
    #print(target_row[0])
    

    if target_row:
        # Extract values from the <tr> element
        values = {
            'Away Team' : Away,
            'fg': target_row[0].find('td', {'data-stat': 'fg'}).text.strip(),
            'fga': target_row[0].find('td', {'data-stat': 'fga'}).text.strip(),
            'fg_pct': target_row[0].find('td', {'data-stat': 'fg_pct'}).text.strip(),
            'fg3': target_row[0].find('td', {'data-stat': 'fg3'}).text.strip(),
            'fg3a': target_row[0].find('td', {'data-stat': 'fg3a'}).text.strip(),
            'fg3_pct': target_row[0].find('td', {'data-stat': 'fg3_pct'}).text.strip(),
            'ft': target_row[0].find('td', {'data-stat': 'ft'}).text.strip(),
            'fta': target_row[0].find('td', {'data-stat': 'fta'}).text.strip(),
            'ft_pct': target_row[0].find('td', {'data-stat': 'ft_pct'}).text.strip(),
            'orb': target_row[0].find('td', {'data-stat': 'orb'}).text.strip(),
            'drb': target_row[0].find('td', {'data-stat': 'drb'}).text.strip(),
            'trb': target_row[0].find('td', {'data-stat': 'trb'}).text.strip(),
            'ast': target_row[0].find('td', {'data-stat': 'ast'}).text.strip(),
            'stl': target_row[0].find('td', {'data-stat': 'stl'}).text.strip(),
            'blk': target_row[0].find('td', {'data-stat': 'blk'}).text.strip(),
            'tov': target_row[0].find('td', {'data-stat': 'tov'}).text.strip(),
            'pf': target_row[0].find('td', {'data-stat': 'pf'}).text.strip(),
            'Home Team' : Home,
            'fg1': target_row[-8].find('td', {'data-stat': 'fg'}).text.strip(),
            'fga1': target_row[-8].find('td', {'data-stat': 'fga'}).text.strip(),
            'fg_pct1': target_row[-8].find('td', {'data-stat': 'fg_pct'}).text.strip(),
            'fg31': target_row[-8].find('td', {'data-stat': 'fg3'}).text.strip(),
            'fg3a1': target_row[-8].find('td', {'data-stat': 'fg3a'}).text.strip(),
            'fg3_pct1': target_row[-8].find('td', {'data-stat': 'fg3_pct'}).text.strip(),
            'ft1': target_row[-8].find('td', {'data-stat': 'ft'}).text.strip(),
            'fta1': target_row[-8].find('td', {'data-stat': 'fta'}).text.strip(),
            'ft_pct1': target_row[-8].find('td', {'data-stat': 'ft_pct'}).text.strip(),
            'orb1': target_row[-8].find('td', {'data-stat': 'orb'}).text.strip(),
            'drb1': target_row[-8].find('td', {'data-stat': 'drb'}).text.strip(),
            'trb1': target_row[-8].find('td', {'data-stat': 'trb'}).text.strip(),
            'ast1': target_row[-8].find('td', {'data-stat': 'ast'}).text.strip(),
            'stl1': target_row[-8].find('td', {'data-stat': 'stl'}).text.strip(),
            'blk1': target_row[-8].find('td', {'data-stat': 'blk'}).text.strip(),
            'tov1': target_row[-8].find('td', {'data-stat': 'tov'}).text.strip(),
            'pf1': target_row[-8].find('td', {'data-stat': 'pf'}).text.strip()}
    lst_values.append(values)
    

        
print(lst_values)  
df = pd.DataFrame(lst_values)  
df.head()
"""    
html_code2 = '''
<tfoot>
<tr data-row="13">
    <th scope="row" class="left " data-stat="player">Team Totals</th>
    <td class="right " data-stat="mp">240</td>
    <td class="right " data-stat="fg">48</td>
    <td class="right " data-stat="fga">91</td>
    <td class="right " data-stat="fg_pct">.527</td>
    <td class="right " data-stat="fg3">14</td>
    <td class="right " data-stat="fg3a">34</td>
    <td class="right " data-stat="fg3_pct">.412</td>
    <td class="right " data-stat="ft">9</td>
    <td class="right " data-stat="fta">12</td>
    <td class="right " data-stat="ft_pct">.750</td>
    <td class="right " data-stat="orb">9</td>
    <td class="right " data-stat="drb">33</td>
    <td class="right " data-stat="trb">42</td>
    <td class="right " data-stat="ast">29</td>
    <td class="right " data-stat="stl">9</td>
    <td class="right " data-stat="blk">6</td>
    <td class="right " data-stat="tov">11</td>
    <td class="right " data-stat="pf">15</td>
    <td class="right " data-stat="pts">119</td>
    <td class="right iz" data-stat="plus_minus"></td>
</tr>
</tfoot>
'''

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_code2, 'html.parser')

# Find the <tfoot> element
target_row2 = soup.find('tfoot')

if target_row2:
# Extract values from the <tr> element
values2 = {
    'Away Team' : Away,
    'fg': target_row2.find('td', {'data-stat': 'fg'}).text.strip(),
    'fga': target_row2.find('td', {'data-stat': 'fga'}).text.strip(),
    'fg_pct': target_row2.find('td', {'data-stat': 'fg_pct'}).text.strip(),
    'fg3': target_row2.find('td', {'data-stat': 'fg3'}).text.strip(),
    'fg3a': target_row2.find('td', {'data-stat': 'fg3a'}).text.strip(),
    'fg3_pct': target_row2.find('td', {'data-stat': 'fg3_pct'}).text.strip(),
    'ft': target_row2.find('td', {'data-stat': 'ft'}).text.strip(),
    'fta': target_row2.find('td', {'data-stat': 'fta'}).text.strip(),
    'ft_pct': target_row2.find('td', {'data-stat': 'ft_pct'}).text.strip(),
    'orb': target_row2.find('td', {'data-stat': 'orb'}).text.strip(),
    'drb': target_row2.find('td', {'data-stat': 'drb'}).text.strip(),
    'trb': target_row2.find('td', {'data-stat': 'trb'}).text.strip(),
    'ast': target_row2.find('td', {'data-stat': 'ast'}).text.strip(),
    'stl': target_row2.find('td', {'data-stat': 'stl'}).text.strip(),
    'blk': target_row2.find('td', {'data-stat': 'blk'}).text.strip(),
    'tov': target_row2.find('td', {'data-stat': 'tov'}).text.strip(),
    'pf': target_row2.find('td', {'data-stat': 'pf'}).text.strip()
}
"""







