# building the image
docker build -t flask-simple:latest .

# running the container - will listen on port 80
docker run -d -p 80:5000 --name flask-api-core flask-simple

# Available API calls:

# Get the weather conditions on the server's location
curl -i -H "Content-Type: application/json" -X GET http://SERVER/v1/api/checkCurrentWeather
  
# Get the weather conditions for a city
curl -i -H "Content-Type: application/json" -X GET http://SERVER/v1/api/checkCityWeather?city=CITY
  
# Upload drives status (input.json) to the app
curl -i -H "Content-Type: application/json" -X POST -d @input.json http://SERVER/v1/api/driveStatus
  
# Get the details of offline drives
curl -i -H "Content-Type: application/json" -X GET http://SERVER/v1/api/driveStatus?status=Offline

