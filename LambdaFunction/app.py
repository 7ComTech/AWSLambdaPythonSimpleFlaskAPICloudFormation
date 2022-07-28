from custom_flask_lambda import FlaskLambda
from flask import request, Response
import json


lambda_handler = FlaskLambda(__name__)


@lambda_handler.route('/teste', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def main_route():
    if request.method == 'GET':
        response = 'GET does not have body!'
        print("GET Route Call", flush=True)
        return Response(json.dumps(response), status=200, content_type='application/json')

    elif request.method == 'POST':
        response = 'POST ' + str(request.json)
        print("POST Route Call", flush=True)
        return Response(json.dumps(response), status=200, content_type='application/json')

    elif request.method == 'PATCH':
        response = 'PATCH ' + str(request.json)
        print("PATCH Route Call", flush=True)
        return Response(json.dumps(response), status=200, content_type='application/json')

    elif request.method == 'PUT':
        response = 'PUT ' + str(request.json)
        print("PUT Route Call", flush=True)
        return Response(json.dumps(response), status=200, content_type='application/json')

    elif request.method == 'DELETE':
        response = 'DELETE ' + str(request.json)
        print("DELETE Route Call", flush=True)
        return Response(json.dumps(response), status=200, content_type='application/json')


if __name__ == '__main__':
    lambda_handler.run(debug=True)
