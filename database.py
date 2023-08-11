from pathlib import Path

p = Path('./records')
var = [x for x in p.iterdir() if x.is_dir()]
print(var)