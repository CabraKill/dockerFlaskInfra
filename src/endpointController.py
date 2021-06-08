from src import app


class EndpointController():
    def __init__(self) -> None:
        self.setEndpoints()

    def test(self):
        return "Testing subroute... OK!"

    def setEndpoints(self) -> None:
        app.add_url_rule('/test', view_func=self.test, methods=['GET'])
