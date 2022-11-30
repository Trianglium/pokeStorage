import json

fields = {''}

f = open('abra.json')
data = json.load(f)
for i in data:
    print(i)
    t = data[i]
    if isinstance(t, bool) or isinstance(t, str):
        fields[i] = t
    else:
        if isinstance(t, list):
        
        elif isinstance(t, list):





f.close()