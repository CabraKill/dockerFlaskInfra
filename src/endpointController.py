from flask.app import Flask

class EndpointController():
    def __init__(self, app: Flask) -> None:
        self.app = app
        self.setEndpoinst()

    def test(self):
        print("test")
        return f"Testing... OK!"

    # Necessary to intermediate the self
    # when needed
    def setEndpoinst(self):
        @self.app.route("/test")
        def _test():
            return self.test()