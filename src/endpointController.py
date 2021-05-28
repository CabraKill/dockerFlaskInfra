from src.context import app

class EndpointController():
    def __init__(self) -> None:
        self.setEndpoinst()

    def test(self):
        print("test")
        return "Testing... OK!"

    # Necessary to intermediate the self
    # when needed
    def setEndpoinst(self):
        @app.route("/test")
        def _test():
            return self.test()
        
if __name__ == '__main__':
    print(str(app))