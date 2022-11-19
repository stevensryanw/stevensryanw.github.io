import requests
from bs4 import BeautifulSoup
import time
import csv

def csv_write_headline(filename, data_to_write):
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(data_to_write)
        
csv_write_headline('data/nhl/salary_data/salaries.csv', ['Name', 'Year', 'Salary'])

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

    url = f'https://www.hockeyzoneplus.com/search-results/filter?q={name}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        salary_url = 'https://www.hockeyzoneplus.com/' + soup.select_one('[itemprop="name"]>a').get('href')
    except Exception as e:
        #print(e)
        salary_url = False
    
    return salary_url


def grab_salary_info(salary_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    response = requests.get(salary_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        name = soup.select_one('[itemprop="name"]').text.strip().split('*')[0]
        table_eles = soup.select('[class="table-container"]>table:not([bordercolor])>tbody>tr[style]')[:-1]
    except Exception as e:
        #print(e)
        table_eles = 0
        name = 'N/A'

    for table_ele in table_eles:
        box = table_ele.select('td>strong')
        try:
            year = box[0].text.split('-')[0]
            sal = box[1].text.split('$')[1].replace(',', '')
            data_write = [name, year, sal]
            csv_write('data/nhl/salary_data/salaries.csv', data_write)
            print(name, year, sal)
        except Exception as e:
            #print(e)
            pass


names = csv_read('webscrapers/nhlName.csv')
for name in names:
    print(f"____________{name}____________")
    salary_url = grab_salary_url(name)
    if salary_url:
        grab_salary_info(salary_url)
        time.sleep(1)
