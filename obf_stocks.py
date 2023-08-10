import time, random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import os
from datetime import datetime
from colorama import Fore, Back, Style
import base64 as a
from fake_useragent import UserAgent

class StockData:
    def __init__(self, ticker, company, volume, open_price, curr, change):
        self.ticker = ticker
        self.company = company
        self.volume = volume
        self.open_price = open_price
        self.curr = curr
        self.change = change

def get_params():
    state = str(input("Headless? (y/n): ")).lower()
    fishing = str(input("Want to fish? (y/n): ")).lower()

    return (state, fishing)

#HEADLESS SETUP
ua = UserAgent()
fake_user_agent = ua.firefox
options = Options()
#PASTE YOUR ACTUAL USER AGENT INTO THE SECOND ARG
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0"
state, fishing = get_params()

def setup(state):
    if state == 'y':
        options.add_argument('-headless') # Set headless mode
        options.set_preference("general.useragent.override",fake_user_agent)

    # HEADLESS
    if state == 'y':
        d = webdriver.Firefox(options=options)
    # GUI
    else:
        d = webdriver.Firefox()
        d.set_window_size(550, 850)
    return d

d = setup(state)

resulting_user_agent = d.execute_script("return navigator.userAgent;")

user_name  = str(os.environ.get("NEO_NAME"))
password = str(os.environ.get("NEO_PASS"))

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

#remove empty gif element from each row
def remove_empty_stock(some_2d_list):
    for sublist in some_2d_list:
        del sublist[0]

#clear terminal
def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    if r:
        print(f"Mystery!?!")
        d.find_element("xpath",a.b64decode(c).decode()).click()
    else:
        print("No fish available.")

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

def fish():
    p()
    print(f"Polling Stocks!")
    stocks = get_stocks()
    records = stocks_to_records(stocks)
    write_csv(stocks)
    print_stocks(stocks)
    print(resulting_user_agent)

def no_fish():
    print(f"Polling Stocks!")
    stocks = get_stocks()
    records = stocks_to_records(stocks)
    write_csv(stocks)
    print_stocks(stocks)
    print(resulting_user_agent)

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

#login
d.get("https://www.grundos.cafe/login/")
d.find_element("name","username").send_keys(user_name)
d.find_element("name","password").send_keys(password)
d.find_element("name","button").click()
#print(d.current_url)

while True:
    try:
        if fishing == 'y':
            #  #[print(stock.ticker) for stock in records]
            fish()

        else:
            no_fish()

    except Exception as e:
        print(f"Errorm: {str(e)}")
        d.quit()
    jitter = random.uniform(1800,  10800)
    time.sleep(jitter)

#quit
d.quit()
