import requests
from bs4 import BeautifulSoup
import csv
rootURL="https://www.ptt.cc/"
def write_csv(entry):
    title = entry.select('.title')[0].text
    tmp = entry.select('.title')[0].find('a')
    tmp = tmp['href']
    with open('output.csv', 'a', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title,rootURL+tmp])


for index in range(20):
    print("第",index,"頁")
    payload = {
    'from': '/bbs/Gossiping/index'+str(index)+'.html',
    'yes': 'yes'
    }
    res = requests.post('https://www.ptt.cc/ask/over18',data = payload)
    soup = BeautifulSoup(res.text)
    for entry in soup.select('.r-ent'):
        trigger = entry.select('.nrec')[0].text
        if trigger=="爆":
            write_csv(entry)
        elif trigger.isdigit() :
            trigger = int(trigger)
            if trigger>10:
                write_csv(entry)