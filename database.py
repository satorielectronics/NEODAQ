from pathlib import Path

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
print(i)
