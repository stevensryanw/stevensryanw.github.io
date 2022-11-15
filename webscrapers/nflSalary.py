import requests
from bs4 import BeautifulSoup
import time
import csv

def csv_write_headline(filename, data_to_write):
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(data_to_write)
        
csv_write_headline('/Users/ryanstevens/Documents/GitHub/CMPS-3160-Final-Project/data/nfl/player_salaries/salaries.csv', ['Name', 'Year', 'Salary'])

def csv_write(filename, data_to_write):
    with open(filename, 'a', encoding='utf-8', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(data_to_write)

def csv_read(filename):
    with open(filename, encoding='utf-8') as file:
        rows = [line.strip('\n') for line in file.readlines()]
    return rows

def listToString(s):
    string = ''
    for ele in s:
        string += ele
    return string

def parser():
    name = soup.find('h3').text
    tables = soup.find_all('table', {'class': 'contract salary-cap-history player-new'})
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            year = cols[:1]
            sal = cols[-1:]
            # year = listToString(year)
            # sal = listToString(sal)
            data_write = [name, year, sal]
            if (year != []) | (year != 'Total'):
                csv_write('/Users/ryanstevens/Documents/GitHub/CMPS-3160-Final-Project/data/nfl/player_salaries/salaries.csv', data_write)
                print(name, year, sal)

for i in range(10800):
    page = requests.get('https://overthecap.com/player/filler/' + str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    if i != 0:
        print(f"____________{i}____________")
        if soup:
            parser()
            time.sleep(2)
    else:
        print ('Starting...')