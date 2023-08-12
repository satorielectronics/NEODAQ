import datetime
import fileinput
from pathlib import Path
import pandas as pd
import datetime as dt


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


def get_prices_for_ticker(files, my_stock):
    pp = []
    for f in files:
        tt = []
        date = get_date_from_file_name(f)
        price = get_price_for_ticker_from_file(f, my_stock)
        tt.append(date)
        tt.append(price)
        pp.append(tt)
    return pp


prices = get_prices_for_ticker(get_files(Path('./records')), "YIPP")

for p in prices:
    print(p)

# print(date)