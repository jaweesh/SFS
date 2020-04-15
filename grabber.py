import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os
import csv

URL = "https://standforsudan.ebs-sd.com/StandForSudan/" # Old URL "https://ebs-sd.com:444/StandForSudan/"


def get_Count(URL):
    # get html tree from page
    headers = {'user-agent':'python scraper v1'}
    try:
        r = requests.get(url = URL , headers=headers) #, verify = False)
    except:
        pass
        return -127
    if r.status_code == 200:
        html = r.text
        parsed_html = BeautifulSoup(html,features="lxml")
    return parsed_html

def get_usd(spans):
    # get USD count
    usd_count = spans[7].text
    usd_amount = spans[8].text
    data = []
    
    data.append(usd_count)
    data.append(usd_amount)
    return data


def jsonify(spans):
    # save data in json file or append to it
    dateTimeObj = datetime.now()
    PEOPLE = spans[5].text
    CASH = spans[6].text
    data = get_usd(spans)
    usd_count = data[0].replace(',','')
    usd_amount = data[1].replace(',','')
    
    J_OBJECT = {}
    J_FILE = "~/StandForSudan_DATA.json"
    try:
        f = open(J_FILE, "r+",encoding='utf8')
    except:
        f = open(J_FILE, "w+",encoding='utf8')

    if os.stat(J_FILE).st_size == 0:
        J_OBJECT['StandForSudan'] = []
    else:
        J_OBJECT = json.loads(f.read())

    f.close()
    J_OBJECT['StandForSudan'].append({
        'TIME': str(dateTimeObj),
        'PEOPLE': str(PEOPLE) ,
        'CASH': str(CASH),
        'USD_Doners':str(usd_count),
        'USD_CASH': str(usd_amount)
    }
    )
    with open(J_FILE, 'w+') as json_file:
	    json.dump(J_OBJECT , json_file)

def csvefy(spans):
    # write data to csv file
    DONATIONS_COUNT = str( spans[5].text).replace(',','')
    DONATIONS = str(spans[6].text).replace(',','')
    dateTimeObj = str(datetime.now())
    # incorporate usd into new objects
    data = get_usd(spans)
    usd_count = data[0].replace(',','')
    usd_amount = data[1].replace(',','')

    DATA = [dateTimeObj, DONATIONS_COUNT, DONATIONS,usd_count,usd_amount]
    CSV_FILE = "~DataFiles/StandForSudan_DATA.csv"
    afile = open(CSV_FILE, 'a', encoding='utf8')
    afile.write(','.join(DATA)+'\n')
    afile.close()

def main():
    # get total doners, total cash, time
    dateTimeObj = datetime.now()
    data = get_Count(URL)
    if data:
        spans = data.find_all('span')
        # DONATIONS_COUNT = spans[5].text
        # DONATIONS = spans[6].text
        # print(dateTimeObj)
        # print("People donated: " + DONATIONS_COUNT)
        # print("Cache collected: " + DONATIONS)
        # print("Donations per Sudanese: "+ str( int(DONATIONS.replace(',',''))/int(DONATIONS_COUNT.replace(',','')) ) )
        jsonify(spans)
        csvefy(spans)
        



if __name__ == "__main__":
    main()

