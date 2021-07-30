# dockerFlaskInfra
A showcase of a docker with flask infrastructure divided between the controllers.


# How to use it ?

## From waitress
```bash
waitress-serve --listen=*:8000 app:app
```

## From flask
```bash
flask run
```

## Docker
The docker image uses as image base the *python:3.8-slim-buster* with gunicorn execution.

### build
Run the command bellow or use the *build* script.
```bash
docker build -t dockerFlaskInfra:latest .
```

### run
Run the command bellow or use the *run* script.
```bash
docker run -p :5000 dockerflaskinfra:latest
```
# Why?
Organization of the controllers inside the API.

# Origin?
While I was studying I had difficulty to find ways of dividing the controllers.

This works for me as a historical backlog and a helping hand for others with the same problem.


# To do:
* Implement swagger documentation
