import datetime
import fileinput
from pathlib import Path
import pandas as pd
import datetime as dt

p = Path('./records')


def is_db_file(f):
    return f.name.endswith("csv")


def get_files():
    f = []
    for x in p.iterdir():
        if is_db_file(x):
            f.append(x)
    return f


files = get_files()

i = files[0]

xx = pd.read_csv(i)


# print(xx)

def get_date_str_from_file_name(f):
    return f.name.split('.')[0]


def get_date_from_file_name(f):
    date_str = get_date_str_from_file_name(f)
    return get_date_from_str(date_str)


def get_date_from_str(date_string):
    return dt.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')


date = get_date_from_file_name(i)

print(date)
