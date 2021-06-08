from src.endpointController import EndpointController
from src import app


@app.route("/")
def home():
    return "Hello, You!"


endpointController = EndpointController()
