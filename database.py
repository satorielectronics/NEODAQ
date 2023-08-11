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

def get_date_from_file_name(f):
    return f.name.split('.')[0]


date_str = get_date_from_file_name(i)

print(date_str)

date = dt.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

print(date)
