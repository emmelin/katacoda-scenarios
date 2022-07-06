#!/usr/bin/python3

import  json
import sys
import  os


with open(str(sys.argv[1]), "r") as f:
    df = json.load(f)
 
new={}

for n in ("title","description","difficulty","time","environment","backend"):
    if n in df:
        new[n]=df[n]

details={}
for n in ("intro","steps","finish","assets"):
    if n in df["details"]:
        details[n]=df["details"][n]

new["details"]=details


for step in details["steps"]:
    print(step["text"]) 
    filename=step["text"].split("/")[-1].split(".")[0]
    if not os.path.exists(filename):
           os.makedirs(filename)

print(new)

with open('result.json', 'w', encoding='utf8') as fp:
    json.dump(new, fp, indent=4, ensure_ascii=False)
