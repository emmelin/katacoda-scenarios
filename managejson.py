#!/usr/bin/python3

import  json
import sys
import  os


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

def change(json_input, lookup_key,text):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                 json_input[k]=text
            else:
                change(v, lookup_key,text)
    elif isinstance(json_input, list):
        for item in json_input:
            change(item, lookup_key,text)

def changeKey(json_input, lookup_key,text):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                 json_input[text]=json_input[k]
                 del json_input[k]
            else:
                changeKey(v, lookup_key,text)
    elif isinstance(json_input, list):
        for item in json_input:
            changeKey(item, lookup_key,text)




indexfile=sys.argv[1]

with open(str(indexfile), "r") as f:
    df = json.load(f)
print(df)
new={}

for n in ("title","description","difficulty","time","environment","backend"):
    if n in df:
        new[n]=df[n]

details={}
for n in ("intro","steps","finish"):
    if n in df["details"]:
        details[n]=df["details"][n]




for step in details["steps"]:
    textinit=step["text"]
    namestep=textinit.split("/")[-1].split(".")[0]
    filename=os.path.dirname(indexfile)+"/"+namestep
    if not os.path.exists(filename):
           os.makedirs(filename)
           print(textinit[1:])
           os.rename(os.path.dirname(indexfile)+"/"+textinit[1:],filename+"/"+namestep+".md")
    step["text"]=namestep+"/"+namestep+".md"
    step["background"]="assets/cleanrep.sh"




details["finish"]["background"]="assets/cleanrep.sh"

#print(new)


# for step in details:
#     for key, value in step:
#         if 
# if isinstance(x, dict):

new["details"]=details


# for champ in item_generator(new,"text"):
#         print (champ)

changeKey(new,"courseData","background")

changeKey(new,"code","foreground")


new["details"]["assets"]={'host01': [{'file': 'aide', 'target': '/usr/local/bin', 'chmod': '+rx'}, {'file': 'rep', 'target': '/usr/local/bin', 'chmod': '+rx'}, {'file': 'tpunixauto.sh', 'target': '/etc/profile.d', 'chmod': '+r'}, {'file': 'alternatif.tar.bz2', 'target': '/tmp', 'chmod': '+r'}]}


with open('result.json', 'w', encoding='utf8') as fp:
    json.dump(new, fp, indent=4, ensure_ascii=False)




