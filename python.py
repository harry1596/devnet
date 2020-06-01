import json as j
import yaml as y
from dicttoxml import dicttoxml as d

with open("sample.json","r") as  f:
 
 dic = j.load(f)
 xml = d(dic)
 yaml = y.dump(dic)
 
print(type(xml))
print(type(yaml)) 
 
with open('sample.yaml','w+') as t:
    t.write(yaml)
with open('sample.xml','wb+') as t:
    t.write(xml)    