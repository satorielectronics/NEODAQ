import fileinput
from pathlib import Path
import pandas as pd

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

print(xx)

