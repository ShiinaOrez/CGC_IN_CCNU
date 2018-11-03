import json

data = json.dumps({"CGC": "CCNU"})
print (data)
print (type(data))

data = json.loads(data)
print (data)
print (type(data))

"""
API: Application Programming Interface

client get the information from API
server give the information to API

                 -----
                 |   |
                 | A |
client <<--data--| P | <<--data--server
                 | I |
                 |   |
                 -----
"""
