#!/usr/bin/python3

import  json
import sys
import  os
import shutil




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

print("treate"+indexfile)

with open(str(indexfile), "r") as f:
    df = json.load(f)

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
    with open(filename+"/"+namestep+".md") as f:
        file=f.read()
        if "[ ]" in file  or "( )" in file :
            step["verify"]=namestep+"/verify.sh"
       
    step["text"]=namestep+"/"+namestep+".md"
    step["background"]="assets/cleanrep.sh"


for file in ("aide","cleanrep.sh","rep"):
    src="./resourcesKillercoda/"+file
    des=os.path.dirname(indexfile)+"/assets/"+file
    #print(src+" to "+des)
    shutil.copy(src, des)


details["finish"]["background"]="assets/cleanrep.sh"

for file in ("intro.md","finish.md"):
    src=os.path.dirname(indexfile)+"/markdown/"+file
    des=os.path.dirname(indexfile)+"/"+file
    #print(src+" to "+des)
    shutil.copy(src, des)




with open(os.path.dirname(indexfile)+"/finish.md") as f:
    file=f.read()
    if "[ ]" in file  or "( )" in file :
        step["verify"]=os.path.dirname(indexfile)+"/verify.sh"

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
new["details"]["intro"]["text"]=new["details"]["intro"]["text"].replace("/markdown/","")
new["details"]["finish"]["text"]=new["details"]["finish"]["text"].replace("/markdown/","")



with open('result.json', 'w', encoding='utf8') as fp:
    json.dump(new, fp, indent=4, ensure_ascii=False)




