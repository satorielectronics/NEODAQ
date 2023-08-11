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


my_stock = "YIPP"

files = get_files(Path('./records'))

i = files[0]

xx = pd.read_csv(i)
for xo in xx.iterrows():
    series = xo[1]
    ticker = series[0]
    if ticker == my_stock:
        current_price = series[4]
        print(current_price)

# print(xx)

date = get_date_from_file_name(i)

# print(date)
