from flask import Flask, request
from drives import DrivesArray
import json
import requests
app = Flask(__name__)

@app.route("/v1/api/driveStatus",  methods=['GET', 'POST'])
def driveStatus():
  if request.method == 'GET':
    if 'status' in request.args and request.args['status'] == 'Offline':
      try:
        drives = DrivesArray()   
        outdata = drives.show_drives(status='Offline')
        output = {}
        output['message'] = 'Found {} offline drive'.format(len(outdata))
        output['data'] = outdata
        s = json.dumps(output, indent = 4)
        return(s)
      except:
        return('No drive defined yet, please send data file first')
    else:
      return('Invalid request')

  if request.method == 'POST':
    content = request.json
    drives = DrivesArray(content)
    return('drives')
  else:
    return('Invalid request method')

@app.route("/v1/api/checkCityWeather", methods=['GET'])
def getCityWeather():

  if 'city' in request.args:
      city_name = request.args['city']
  else:
    return('Missing city name')

  weather_api_key = '7483724b93bde963f7789b0e25b7ab00'
  api_url_we = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, weather_api_key)

  try:
    response = requests.post(api_url_we, verify=False)
    if (response.status_code == 200):
      data = json.loads(response.text)
      weather = {'city': data['name'], 'country': data['sys']['country'], 'degrees': int(data['main']['temp']-273)}
      return(json.dumps(weather))
    elif (response.status_code == 404):
      return('Wrong city name: {}'.format(city_name))
  except:
    return('Problem to fetch weather, please try again later')
  '''  
  except Exception, e:
    return('Problem to fetch weather - {}, please try again later'.format(str(e))
  '''

@app.route("/v1/api/checkCurrentWeather", methods=['GET'])
def getCurrentWeather():
  ip_access_token = '0a0c931f2254c5'
  weather_api_key = '7483724b93bde963f7789b0e25b7ab00'
  api_url_ip = 'http://ipinfo.io?token={}'.format(ip_access_token)
  response = requests.post(api_url_ip, verify=False)
  data = json.loads(response.text)
  city_name = data['city']
  api_url_we = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, weather_api_key)
  response = requests.post(api_url_we, verify=False)
  data = json.loads(response.text)
  weather = {'city': data['name'], 'country': data['sys']['country'], 'degrees': int(data['main']['temp']-273)}
  return(json.dumps(weather))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
