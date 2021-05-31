# save this as app.py
from src.endpointController import EndpointController
from src.context import app


@app.route("/")
def hello():
    print("algo aqui veio")
    return "Hello!\nFrom python in a container"


endpointController = EndpointController(app)
