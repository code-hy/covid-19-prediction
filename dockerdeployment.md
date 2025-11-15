# 🐳 Docker Deployment
You can also run the entire application in a Docker container.

Build the Docker image:
``` bash


docker build -t covid-prediction-api .

```

Run the Docker container:
``` bash

docker run -p 8000:8000 --name covid-api covid-prediction-api
```

The API will now be available at http://localhost:8000/docs.
