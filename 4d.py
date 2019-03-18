import base64
import json
import requests
from bs4 import BeautifulSoup

FOURD_BASE_URL = 'http://www.singaporepools.com.sg/en/product/Pages/4d_results.aspx'
draw_no = int(input('draw no: '))

params = {
  'sppl': base64.b64encode(b'DrawNumber=%d' % draw_no)
}

get_4d = requests.get(FOURD_BASE_URL, params=params)
soup = BeautifulSoup(get_4d.content, 'html.parser')

# get date of draw
date = soup.find('th', class_='drawDate').get_text()

# get first prize
first_prize = soup.find('td', class_='tdFirstPrize').get_text()

# get second prize
second_prize = soup.find('td', class_='tdSecondPrize').get_text()

# get third prize
third_prize = soup.find('td', class_='tdThirdPrize').get_text()

# get starter prizes
starter_prizes = []
starter_prizes_tbody = soup.find('tbody', class_='tbodyStarterPrizes').findAll('td')
for td in starter_prizes_tbody:
  starter_prizes.append(td.get_text())

# get consolation prizes
consolation_prizes = []
consolation_prizes_tbody = soup.find('tbody', class_='tbodyConsolationPrizes').findAll('td')
for td in consolation_prizes_tbody:
  consolation_prizes.append(td.get_text())

result = {
  'drawNo': draw_no,
  'date': date,
  'results': {
    'firstPrize': first_prize,
    'secondPrize': second_prize,
    'thirdPrize': third_prize,
    'starterPrizes': starter_prizes,
    'consolationPrizes': consolation_prizes
  }
}

print(json.dumps(result))