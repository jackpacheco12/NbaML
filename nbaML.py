# import needed libraries
import pandas as pd
# create a function to scrape team performance for multiple years

import requests
from bs4 import BeautifulSoup
import re 
import time
def games_month(year, month):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html"
    
# Send an HTTP request to the URL and get the content
    response = requests.get(url)
    html_content = response.content
    #print(html_content)
   
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    csk_values = [re.search(r'csk="([^"]+)"', str(tag)) and re.search(r'csk="([^"]+)"', str(tag)).group(1) for tag in soup.find_all('th', {'data-stat': 'date_game'})]
    time.sleep(5)
    return csk_values 

Home= []
#games_month(2024, "october")[1:]




def make_url(Home):
    url = f"https://www.basketball-reference.com/boxscores/{Home}.html"
    return url 



import time 


months = ["january", "february"]
#, "march", "april", "october", "november", "december"]



years = [2023,2024]
for y in years: 
    for m in months: 
        Home.append(games_month(y, m)[1:])
        
def flatten(xss):
    return [x for xs in xss for x in xs]

Home = flatten(Home)


game_list = []
for i in range(len(Home)):
   game_list.append(make_url(Home[i]))

print(game_list[0:10])

lst_values = []
for i in range(len(game_list)): 
    print(game_list[i])


    response = requests.get(game_list[i])
    html_content = response.content
    # Find the h1 element within the specified context
    soup = BeautifulSoup(html_content,'html.parser')
    h1_text = soup.select_one('#content h1').get_text(strip=True)

    Away = h1_text.split(" at")[0]
    Home = h1_text.split(" at")[1].split("Box Score")[0].strip()
    

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <tfoot> element


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
    time.sleep(10)


print(lst_values)  
df = pd.DataFrame(lst_values)  
print(df.head())



