I have created a webscraper using beautiful soup, but am having issues dealing with the output.

Idealy for scrape 1 id like it to ouput:  
  
Peyton Manning, 1998, 11744000  
Peyton Manning, 1999, 1430000  
Peyton Manning, 2000, 11066000  
Peyton Manning, 2001, 4452000  
Peyton Manning, 2002, 6298000  
Peyton Manning, 2003, 11324000  
Peyton Manning, 2004, 35035000  
Peyton Manning, 2005, 665000  
Peyton Manning, 2006, 10000000  
Peyton Manning, 2007, 11000000  
Peyton Manning, 2008, 11500000  
Peyton Manning, 2009, 14000000  
Peyton Manning, 2010, 15800000  
Peyton Manning, 2011, 26400000  
Peyton Manning, 2012, 18000000  
Peyton Manning, 2013, 25000000  
Peyton Manning, 2014, 15000000  
Peyton Manning, 2015, 19000000  

This is my current code:  

```
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

def parser():
    name = soup.find('h3').text
    tables = soup.find_all('table', {'class': 'contract salary-cap-history player-new'})
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            #cols = [ele.text.strip() for ele in cols]
            year = cols[:1]
            sal = cols[-1:]
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
```

And this is the output im getting: 
   
Peyton Manning,[],[]  
Peyton Manning,[<td>1998</td>],"[<td>$11,744,000</td>]"  
Peyton Manning,[<td>1999</td>],"[<td>$1,430,000</td>]"  
Peyton Manning,[<td>2000</td>],"[<td>$11,066,000</td>]"  
Peyton Manning,[<td>2001</td>],"[<td>$4,452,000</td>]"  
Peyton Manning,[<td>2002</td>],"[<td>$6,298,000</td>]"  
Peyton Manning,[<td>2003</td>],"[<td>$11,324,000</td>]"  
Peyton Manning,[<td>2004</td>],"[<td>$35,035,000</td>]"  
Peyton Manning,[<td>2005</td>],"[<td>$665,000</td>]"  
Peyton Manning,[<td>2006</td>],"[<td>$10,000,000</td>]"  
Peyton Manning,[<td>2007</td>],"[<td>$11,000,000</td>]"  
Peyton Manning,[<td>2008</td>],"[<td>$11,500,000</td>]"  
Peyton Manning,[<td>2009</td>],"[<td>$14,000,000</td>]"  
Peyton Manning,[<td>2010</td>],"[<td>$15,800,000</td>]"  
Peyton Manning,[<td>2011</td>],"[<td>$26,400,000</td>]"  
Peyton Manning,[<td>2012</td>],"[<td>$18,000,000</td>]"  
Peyton Manning,[<td>2013</td>],"[<td>$25,000,000</td>]"  
Peyton Manning,[<td>2014</td>],"[<td>$15,000,000</td>]"  
Peyton Manning,[<td>2015</td>],"[<td>$19,000,000</td>]"  
Peyton Manning,"[<td colspan=""2"">Total</td>]","[<td>$247,714,000</td>]"  



Ive tried creating a function and changing parser to individualy change to strings:

```
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
            #cols = [ele.text.strip() for ele in cols]
            year = cols[:1]
            sal = cols[-1:]
            year = listToString(year)
            sal = listToString(sal)
            data_write = [name, year, sal]
            if (year != []) | (year != 'Total'):
                csv_write('/Users/ryanstevens/Documents/GitHub/CMPS-3160-Final-Project/data/nfl/player_salaries/salaries.csv', data_write)
                print(name, year, sal)
```
And here is its error output:
```
Starting...
____________1____________
Peyton Manning  
Traceback (most recent call last):
  File "/Users/ryanstevens/Documents/GitHub/CMPS-3160-Final-Project/webscrapers/nflSalary.py", line 52, in <module>
    parser()
  File "/Users/ryanstevens/Documents/GitHub/CMPS-3160-Final-Project/webscrapers/nflSalary.py", line 39, in parser
    year = listToString(year)
  File "/Users/ryanstevens/Documents/GitHub/CMPS-3160-Final-Project/webscrapers/nflSalary.py", line 26, in listToString
    string += ele
TypeError: can only concatenate str (not "Tag") to str
```

When uncommenting the text.strip loop in the first code I provided:

```
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
```
This outputs better but still not quite what im looking for and I cant seem to do anything with the one element lists it created:  
  
Peyton Manning,[],[]  
Peyton Manning,['1998'],"['$11,744,000']"  
Peyton Manning,['1999'],"['$1,430,000']"  
Peyton Manning,['2000'],"['$11,066,000']"  
Peyton Manning,['2001'],"['$4,452,000']"  
Peyton Manning,['2002'],"['$6,298,000']"  
Peyton Manning,['2003'],"['$11,324,000']"  
Peyton Manning,['2004'],"['$35,035,000']"  
Peyton Manning,['2005'],"['$665,000']"  
Peyton Manning,['2006'],"['$10,000,000']"  
Peyton Manning,['2007'],"['$11,000,000']"  
Peyton Manning,['2008'],"['$11,500,000']"  
Peyton Manning,['2009'],"['$14,000,000']"  
Peyton Manning,['2010'],"['$15,800,000']"  
Peyton Manning,['2011'],"['$26,400,000']"  
Peyton Manning,['2012'],"['$18,000,000']"  
Peyton Manning,['2013'],"['$25,000,000']"  
Peyton Manning,['2014'],"['$15,000,000']"  
Peyton Manning,['2015'],"['$19,000,000']"  
Peyton Manning,['Total'],"['$247,714,000']"  

Anything anyone can see that would prevent this from working or how to fix my scraper to get the output im looking for? Thanks!