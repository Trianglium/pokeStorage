import json

fields = {""}

f = open("abra.json")
data = json.load(f)
for i in data:
    print(i)


f.close()
