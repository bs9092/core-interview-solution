# building the image
docker build -t flask-simple:latest .

# running the container - will listen on port 80
docker run -d -p 80:5000 --name flask-api-core flask-simple
