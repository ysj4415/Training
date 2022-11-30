import json

data = {'x':10, 'y':20, 'size':1.5}
with open('data.json', 'w') as f:
    json.dump(data, f)

