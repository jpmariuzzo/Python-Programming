import json

#Presenting a list (also called array) of 2 items called 'input'
input = '''[
    {   "id" : "001", 
        "x" : "2", 
        "name" : "Chuck"
    },

    {   "id": "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

#Loads method in this case creates a list 'info'
info = json.loads(input)
print('User count:', len(info), '\n')

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'], '\n')