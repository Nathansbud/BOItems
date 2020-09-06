import json
import os
import re

from collections import Counter

data_path = os.path.join(os.path.dirname(__file__), "data")
files = [open(os.path.join(data_path, f"{game}{'_items' if i < 3 else '_trinkets'}.json")) for i, game in enumerate(["rebirth", "afterbirth", "afterbirthplus"]*2)]

item_data = {}
doubles = ["Cancer", "Tonsil"]
for f in files:
    lines = json.load(f)
    for item, data in lines.items():
        if item not in doubles or len(data['meta']) == 0:
            item_data[item.lower()] = data
        else:
            item_data[f"{item.lower()}_i"] = data

    f.close()


if __name__ == "__main__":
    if item_match := re.findall(r"!!(.*?)!!", "!!Cancer_I!! So do you$[Brother Bobby]"):
        for n in item_match:
            print(n, n.lower() in item_data)
            
            
        


