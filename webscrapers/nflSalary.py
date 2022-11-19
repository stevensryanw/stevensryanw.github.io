import requests
from bs4 import BeautifulSoup
import time
import csv
import random

def csv_write_headline(filename, data_to_write):
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(data_to_write)
        
csv_write_headline('nfl_salaries.csv', ['Name', 'Year', 'Salary'])

def csv_write(filename, data_to_write):
    with open(filename, 'a', encoding='utf-8', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(data_to_write)

def csv_read(filename):
    with open(filename, encoding='utf-8') as file:
        rows = [line.strip('\n') for line in file.readlines()]
    return rows


def grab_salary_url(name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    url = f'https://overthecap.com/player/filler/{name}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        salary_url = url
    except Exception as e:
        print(e)
        salary_url = False
    print(salary_url)
    return salary_url


def grab_salary_info(salary_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    response = requests.get(salary_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.prettify()

    soup.find_all('title')
    for title in soup.find_all('title'):
        if title.text == 'WordPress › Error':
            return False
    try:
        name = soup.find('h3').text
        table_sal = soup.find('table', {'class': 'contract salary-cap-history player-new'})
        table_body = table_sal.find('tbody')
    except Exception as e:
        print(e)
        table_sal = 0
        name = 'N/A'
    #print(name)
    if name != 'N/A':
        for table_ele in table_body:
            box = table_ele.select('td')
            try:
                year = box[0].text
                sal = box[-1:][0].text.split('$')[1].replace(',', '')
                data_write = [name, year, sal]
                csv_write('nfl_salaries.csv', data_write)
                print(name, year, sal)
            except Exception as e:
                print(e)
                pass
    else:
        print("null page")
        pass

names = csv_read('nflName.csv')
start = time.time()
for i in range(200):
    if i != 0:
        print(f"____________{i}____________")
        salary_url = grab_salary_url(i)
        if salary_url:
            grab_salary_info(salary_url)
            end1 = time.time()
            print(f"Time: {end1 - start}")
            rand1 = random.randint(0, 10) + random.randint(1,15)
            print(f"Sleeping for {rand1} seconds")
            time.sleep(rand1)
    else:
        print ('Starting...')
end = time.time()
print(f"Total Time: {end - start}")

#grab_salary_info('https://overthecap.com/player/filler/258')