## Parse dictionary response as custom object to simplify weather app code

While dictionaries are very useful data structures, their main drawback is that you need to know the exact
spelling of their keys to access their values. Automatic editor code completion features and direct overview of
their keys becomes somehow tricky, and you need to write more code in order to get the values you are actually 
looking for.


## Challenge

For this challenge, you will have to cast the api response of the OpenWeatherMap service into a custom object
so that you can simplify the code used to access the response data. You need to do it in the following fashion.
Assuming you have a response who looks like this:

`data = {
    'coord': {'lon': 5.25, 'lat': 52},
    'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
    'base': 'stations',
    'main': {'temp': 279.8, 'feels_like': 277.87, 'temp_min': 277.63, 'temp_max': 281.49, 'pressure': 1021, 'humidity': 73},
    'visibility': 10000,
    'wind': {'speed': 2.68, 'deg': 309, 'gust': 7.6},
    'clouds': {'all': 62},
    'dt': 1679914909,
    'sys': {'type': 2, 'id': 2009768, 'country': 'NL', 'sunrise': 1679894779, 'sunset': 1679940148},
    'timezone': 7200,
    'id': 2745909,
    'name': 'Provincie Utrecht',
    'cod': 200
}`

The object should be able to access every value as an attribute. For example, if you want to access the temperature 
value you should use `object_name.main.temp`etc. 

HINT: Dataclasses can be quite useful in this process.










