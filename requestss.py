import requests

req = requests.get('https://api.openweathermap.org/data/2.5/weather',
                   params={'appid': 'dc4782cd45700c18c29efd99522de225',
                           'units': 'metric',
                           'q': 'Dnipro',
                           'weather.id': 'Dnipro',
                           'feels_like.value': 'Dnipro',
                           'wind.speed.value': 'Dnipro',
                           'wind.direction.code': 'Dnipro',
                           'clouds.value': 'Dnipro',
                           'clouds.name': 'Dnipro',
                           'visibility.value': 'Dnipro',
                           })

if req.status_code in [200, 202]:
    print(req.status_code, 'code')
    req.json = req.json()

else:
    print('Bad requests.')
    print(req.status_code, 'code')