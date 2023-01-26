import json
############################################################
# Need to install requests package with < pip install requests >
############################################################
import requests
# Get Key from https://openweathermap.org
weatherKey = '96919ca4c6da418a0e083b07f84744b3'

url='https://api.openweathermap.org/data/2.5/weather?appid=96919ca4c6da418a0e083b07f84744b3&q='

cityName = input("Enter City Name : ")

# Append City Name to q=
cityWeatherURL = url + cityName

### JSON ###
jsonData = requests.get(cityWeatherURL).json()

# Readable Format 
dataFormat = json.dumps(jsonData,indent=4)

print(dataFormat)
