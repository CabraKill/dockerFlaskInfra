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
# Why?
Organization of the controllers inside the API

# Origin?
While I was studying I had difficulty to find ways of dividing the controllers.

This works for me as a historical backlog and a helping hand for others with the same problem.