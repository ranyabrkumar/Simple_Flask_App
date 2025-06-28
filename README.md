# Simple_Flask_App


# Build the Docker image
docker build -t flask-docker-app .

# Run the container
docker run -p 5000:5000 flask-docker-app
