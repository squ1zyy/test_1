import requests
from json import dumps

req = requests.get('https://api.openweathermap.org/data/2.5/weather',
                   params={'appid': 'dc4782cd45700c18c29efd99522de225',
                           'units': 'metric',
                           'q': 'Dnipro',
                   })

if req.status_code in [200, 202]:
    print(req.status_code, 'code')
    req_json = req.json()
    print(dumps(req_json, indent=4))
    print(req_json.keys())
    temperature = req_json["main"]["temp"]
    print(temperature)

else:
    print('Bad requests.')
    print(req.status_code, 'code')