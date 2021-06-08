from src import app


class EndpointController():
    def __init__(self) -> None:
        self.setEndpoints()

    def test(self):
        print("test")
        return f"Testing... OK!"

    def setEndpoints(self):
        app.add_url_rule('/test', view_func=self.test, methods=['GET'])
