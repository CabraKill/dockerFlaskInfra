from flask import request
from src import app


class EndpointController():
    def __init__(self) -> None:
        self.setEndpoints()

    def test(self):
        return "Testing subroute... OK!"

    def test_body(self):
        return f"Testing body received: {request.data}"
    
    def test_body_json(self):
        """
        Expects a Content-Type json header 
        """
        return f"Testing body received: {request.json}"

    @app.route('/testWithAnnotation')
    def testWithAnnotation():
        return "Testing annotation... OK!"

    def testWithArgs(name):
        name = request.args.get('name')
        return f'Name: {name}'

    def testWithData(self, title):
        return f'Data: {title}'

    def setEndpoints(self) -> None:
        app.add_url_rule('/test', view_func=self.test, methods=['GET'])
        app.add_url_rule('/test', view_func=self.test_body, methods=['POST'])
        app.add_url_rule('/test-json', view_func=self.test_body_json, methods=['POST'])
        app.add_url_rule(
            '/test-args', view_func=self.testWithArgs, methods=['GET'])
        app.add_url_rule('/test/<string:title>',
                         view_func=self.testWithData, methods=['GET'])
