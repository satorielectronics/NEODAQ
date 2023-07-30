import time, random
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import os
import colorama
from datetime import datetime
from colorama import Fore, Back, Style

#export NEO_NAME="USER here"
#export NEO_PASS="PASS here"

#stock_data = pd.DataFrame(columns=['Symbol', 'Company', 'Volume', 'Open Price', 'Current', 'Change'])


#Initialize colorama
colorama.init(autoreset=True)

user_name  = str(os.environ.get("NEO_NAME"))
password = str(os.environ.get("NEO_PASS"))

stocks = []

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

    print(f"Earth Time:  {format_time}")
    print(f"Neopia Time: {hour}:{minute}:{second} {am_pm_caps}")

#clear terminal
def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')


#remove empty gif element from each row
def remove_empty_stock(some_2d_list):
    for sublist in some_2d_list:
        del sublist[0]

#fish for all and return available pets
def fishing():
    driver.get("https://www.grundos.cafe/water/fishing/")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup.find_all('a')
    available_pets = []

    for a in a_tags:
        href = a['href']
        if "/setactivepet/" in href:
            available_pets.append(href)
    #print(a_tags)
    print(available_pets)

    driver.find_element("xpath","/html/body/div/div[5]/main/div[3]/form/input[3]").click()
    print(driver.current_url)

#scrape stocks
def stock_scrape():
    driver.get("https://www.grundos.cafe/games/stockmarket/stocks/?view_all=True")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    #pretty_table = soup.prettify()
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
    #del stocks[0]
    clear_term()
    get_time(soup)
    vol(stocks)
    records = []

    for row in stocks:
        ticker, company, volume, open_price, curr, change = row
        record = StockData(ticker, company, volume, open_price, curr, change)
        records.append(record)
    #records = remove_duplicate_arrays(records)
    #data = np.array(records)
    del stocks[0]
    df = pd.DataFrame(stocks, columns=['Ticker', 'Company', 'Volume', 'Open Price', 'Current', 'Change'])
    df.to_csv('stocks.csv', index=False)
#    global stock_data
#    stock_data = stock_data.append({'Ticker':stocks[0],'Company':stocks[1],'Volume':stock[2],'Open Price':stocks[3],'Current':stocks[4],'Change':stocks[5]}, ignore_index=True)
#    print(stock_data)

    b = Back.LIGHTBLACK_EX
    r = Fore.LIGHTRED_EX
    g = Fore.LIGHTGREEN_EX
    y = Fore.LIGHTYELLOW_EX

    #print(records[1].ticker)

    for record in records:
        if "+" in record.change:
            print(g+record.ticker, g+record.company, g+record.volume, g+record.open_price, g+record.curr, g+record.change)
        elif "-" in record.change:
            print(r+record.ticker, r+record.company, r+record.volume, r+record.open_price, r+record.curr, r+record.change)
        else:
            print(y+record.ticker, y+record.company, y+record.volume, y+record.open_price, y+record.curr, y+record.change)


def vol(some_list):
    #remove first index
    #del some_list[0]
    #removes first index of each remaining list
    remove_empty_stock(some_list)
    # Initialize a variable to store the sum of the volumes
    sum_volume = 0

    # Iterate over each sublist in the array starting from the second sublist (skipping the header)
    for sublist in some_list[1:]:
        # Access the "Volume" element (at index 2) of the sublist
        volume = sublist[2]
        # Remove the commas from the volume string and convert it to an integer
        volume = int(volume.replace(',', ''))
        # Add the volume to the sum
        sum_volume += volume

    # Print the sum of the volumes
    print("Sum of volumes:", sum_volume)
    #print(some_list)


#setup
driver = webdriver.Firefox()
driver.set_window_size(550, 550)
print(driver)

#login
driver.get("https://www.grundos.cafe/login/")
driver.find_element("name","username").send_keys(user_name)
driver.find_element("name","password").send_keys(password)
driver.find_element("name","button").click()
print(driver.current_url)


while True:
    try:
        #print(f"Fishing!")
        #fishing()
        print(f"Polling Stocks!")
        stock_scrape()
    except Exception as e:
        print(f"Error: {str(e)}")
    jitter = random.uniform(30,  1200)
    time.sleep(jitter)

#quit
driver.quit()


