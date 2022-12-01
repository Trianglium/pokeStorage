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
            print('\t', t)
        
        elif isinstance(t, dict):
            print('\t', t.keys())

        else: 
            print(type(t), t)





f.close()