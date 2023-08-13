from pathlib import Path
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


def is_db_file(f):
    return f.name.endswith("csv")


def get_files(p):
    f = []
    for x in p.iterdir():
        if is_db_file(x):
            f.append(x)
    return f


def get_date_str_from_file_name(f):
    return f.name.split('.')[0]


def get_date_from_file_name(f):
    date_str = get_date_str_from_file_name(f)
    return get_date_from_str(date_str)


def get_date_from_str(date_string):
    return dt.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')


def get_price_for_ticker_from_file(f, my_stock):
    xx = pd.read_csv(f)
    for xo in xx.iterrows():
        series = xo[1]
        ticker = series[0]
        if ticker == my_stock:
            current_price = series[4]
            return current_price


class StockPoint:
    def __init__(self, date, price):
        self.date = date
        self.price = price

    def to_string(self):
        return '{0} @ {1}'.format(self.date, self.price)


def get_prices_for_ticker(files, my_stock):
    pp = []
    for f in files:
        date = get_date_from_file_name(f)
        price = get_price_for_ticker_from_file(f, my_stock)
        pp.append(StockPoint(date, price))
    pp.sort(key=lambda x: x.date, reverse=False)
    return pp


def plot_prices(price_list):
    global p
    pp = []
    for p in price_list:
        pp.append(p.price)
    plt.plot(pp)
    plt.ylabel('some numbers')
    plt.show()


prices = get_prices_for_ticker(get_files(Path('./records')), "EEEE")

for p in prices:
    print(p.to_string())

plot_prices(prices)
