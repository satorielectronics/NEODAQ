import time, random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import os
import colorama
from datetime import datetime
from colorama import Fore, Back, Style
import base64 as a
from fake_useragent import UserAgent
import threading



#HEADLESS SETUP
ua = UserAgent()
fake_user_agent = ua.firefox
options = Options()
options.add_argument('-headless') # Set headless mode
#PASTE YOUR ACTUAL USER AGENT INTO THE SECOND ARG
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0"
options.set_preference("general.useragent.override",user_agent)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 4)
#export NEO_NAME="USER here"
#export NEO_PASS="PASS here"

#Initialize colorama
colorama.init(autoreset=True)

user_name  = str(os.environ.get("NEO_NAME"))
password = str(os.environ.get("NEO_PASS"))



class StockData:
    def __init__(self, ticker, company, volume, open_price, curr, change):
        self.ticker = ticker
        self.company = company
        self.volume = volume
        self.open_price = open_price
        self.curr = curr
        self.change = change

def get_time(soup):
    clock_div = soup.find("div", id="sb_clock")

    hour = clock_div.find("span", id="NST_clock_hours").text
    minute = clock_div.find("span", id="NST_clock_minutes").text
    second = clock_div.find("span", id="NST_clock_seconds").text
    am_pm = clock_div.find(class_="nst").text.split()[-2]
    am_pm_caps = am_pm.upper()
    current_time = datetime.now().strftime("%I:%M:%S %p")

    format_time = current_time[1:]
    global today_time
    today_time = str(datetime.today())

    print(f"Earth Time  : {format_time}")
    print(f"Neopia Time : {hour}:{minute}:{second} {am_pm_caps}")
    #return format_time

#clear terminal
def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')

#remove empty gif element from each row
def remove_empty_stock(some_2d_list):
    for sublist in some_2d_list:
        del sublist[0]

#fish for all and return available pets
def fishing():
    d.get("https://www.grundos.cafe/water/fishing/")
    html = d.page_source
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup.find_all('a')
    available_pets = []

    for a in a_tags:
        href = a['href']
        if "/setactivepet/" in href:
            available_pets.append(href)
    #print(a_tags)
    print(available_pets)

    if available_pets:
        d.find_element("xpath","/html/body/div/div[5]/main/div[3]/form/input[3]").click()
    else:
        print(d.current_url)

    #  div = soup.find('div', class_='flex-column med-gap')
    #  p_tags = soup.find_all('p')
    #
    #  strong_texts = []
    #  for p_tag in p_tags:
    #      strong_tag = p_tag.find('strong')
    #      if strong_tag:
    #          strong_texts.append(strong_tag.text)
    #
    #  for text in strong_texts:
    #      print(text)
#secret fishing function

def fish_test():
    url = 'https://www.grundos.cafe/water/fishing/'  # Replace with the actual URL
    csrf_token = 'r3Kyed74ZFr75GGVo87Y3YzqRXS68NkwHsPXublHs8yoXlr7QUVGCG84Y30uVvWj'  # Replace with the actual CSRF token

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',  # Set the content type accordingly
    }

    data = {
        'csrfmiddlewaretoken': csrf_token,
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print("POST request successful!")
    else:
        print("POST request failed.")

def p():
    c = "L2h0bWwvYm9keS9kaXYvZGl2WzVdL21haW4vZGl2WzNdL2Zvcm0vaW5wdXRbM10="
    e = "L3NldGFjdGl2ZXBldC8="
    f = "aHR0cHM6Ly93d3cuZ3J1bmRvcy5jYWZlL3dhdGVyL2Zpc2hpbmcv="

    d.get(a.b64decode(f).decode())
    h = d.page_source
    s = BeautifulSoup(h, 'html.parser')
    t = s.findAll('a')
    r = []
    for i in t:
        w = i['href']
        if a.b64decode(e).decode() in w:
            r.append(w)
    print(r)
    if r:
        d.find_element("xpath",a.b64decode(c).decode()).click()
    else:
        print(d.current_url)

#p()




#create sub_folder and write CSV named after the current time
def write_csv(stocks):
    parent_folder = 'records'
    os.makedirs(parent_folder, exist_ok=True)

    df = pd.DataFrame(stocks, columns=['Ticker', 'Company', 'Volume',
                                       'Open Price', 'Current', 'Change'])
    file_path = os.path.join(parent_folder, today_time+'.csv')

    df.to_csv(file_path, index=False)

def print_stocks(stocks):
    df = pd.DataFrame(stocks, columns=['Ticker', 'Company', 'Volume',
                                       'Open Price', 'Current', 'Change'])
    print(df.to_string(justify=True))
    #print(user_agent)




#scrape stocks
def stock_term(records):

    b = Back.LIGHTBLACK_EX
    r = Fore.LIGHTRED_EX
    g = Fore.LIGHTGREEN_EX
    y = Fore.LIGHTYELLOW_EX



    for record in records:
        if "+" in record.change:
            print(g+record.ticker, g+record.company, g+record.volume,
                  g+record.open_price, g+record.curr, g+record.change)
        elif "-" in record.change:
            print(r+record.ticker, r+record.company, r+record.volume,
                  r+record.open_price, r+record.curr, r+record.change)
        elif "Ticker" in record.ticker:
            print(b+record.ticker, b+record.company, b+record.volume,
                  b+record.open_price, b+record.curr, b+record.change)
        else:
            print(y+record.ticker, y+record.company, y+record.volume,
                  y+record.open_price, y+record.curr, y+record.change)



def stocks_to_records(stocks):
    records = []
    for row in stocks:
        ticker, company, volume, open_price, curr, change = row
        record = StockData(ticker, company, volume, open_price, curr, change)
        records.append(record)
    # records = remove_duplicate_arrays(records)
    # data = np.array(records)
    del stocks[0]
    return records


def get_stocks():
    d.get("https://www.grundos.cafe/games/stockmarket/stocks/?view_all=True")
    html = d.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # pretty_table = soup.prettify()
    stocks = []
    table = soup.find('table')
    # Iterate over the table rows
    for row in table.find_all('tr'):
        # Create a temporary list to store the row data
        temp_row = []
        # Iterate over the cells of each row
        for cell in row.find_all('td'):
            # Extract the data from the cell
            cell_data = cell.text.strip()
            # Append the data to the temporary row list
            temp_row.append(cell_data)
        # Append the temporary row list to the 'stocks' list
        stocks.append(temp_row)
    # del stocks[0]
    clear_term()
    get_time(soup)
    vol(stocks)

    return stocks


def vol(some_list):
    remove_empty_stock(some_list)
    # Initialize a variable to store the sum of the volumes
    sum_volume = 0

    # Iterate over each sublist in the array starting from the second sublist
    # (skipping the header)
    for sublist in some_list[1:]:
        # Access the "Volume" element (at index 2) of the sublist
        volume = sublist[2]
        # Remove the commas from the volume string and convert it to an integer
        volume = int(volume.replace(',', ''))
        # Add the volume to the sum
        sum_volume += volume

    # Print the sum of the volumes
    print("Total Volume:", sum_volume)
    #print(some_list)



#HEADLESS
d = webdriver.Firefox(options=options)

#NORMAL
#d = webdriver.Firefox()

# Retrieve the modified user agent string
resulting_user_agent = d.execute_script("return navigator.userAgent;")
d.set_window_size(550, 850)
print(resulting_user_agent)
#login
d.get("https://www.grundos.cafe/login/")
d.find_element("name","username").send_keys(user_name)
d.find_element("name","password").send_keys(password)
d.find_element("name","button").click()
print(d.current_url)
print(f"Mystery?!")
background_thread = threading.Thread(target=p)
background_thread.start()

while True:
    try:
        #print(f"Mystery?!")
        #fishing()
        #p()
        print(f"Polling Stocks!")
        stocks = get_stocks()
        records = stocks_to_records(stocks)
        write_csv(stocks)
        print_stocks(stocks)
        #stock_term(records)
    except Exception as e:
        print(f"Errorm: {str(e)}")
        d.quit()
    jitter = random.uniform(1800,  10800)
    time.sleep(jitter)

#quit
d.quit()


