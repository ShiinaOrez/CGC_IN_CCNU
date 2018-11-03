"""
response<--server
   |        /|
   |/        |
client-->request
"""

"""
request methods:

like: GET, POST, PUT, DELETE
------------------------------
|GET:    |get the resource   |
------------------------------
|POST:   |post the resource  |
------------------------------
|PUT:    |change the resource|
------------------------------
|DELETE: |delete the resource|
------------------------------
"""

"""
response status code:

------------------
|200: OK         |
------------------
|400: BadRequest |
|401: Unauth     |
|404: NotFound   |
------------------
|502: BadGateway |
------------------
"""

import requests
response = requests.get('http://www.baidu.com')
print(response.text)
print(response.links)
