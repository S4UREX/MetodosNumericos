from static.NumericalMethods.Bisection.Bisection import Bisection
from static.NumericalMethods.FalsePosition.FalsePosition import FalsePosition
from static.NumericalMethods.Newton_Raphson.NewtonRaphson import NewtonRaphson
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

@app.route('/bisection', methods=['POST'])
def bisection():
    json = request.get_json();
    xi = float(request.get_json()['xi'])
    xu = float(request.get_json()['xu'])
    error_range = float(request.get_json()['errorRange'])
    equation = request.get_json()['equation']
    result = Bisection().execute(xi, xu, equation, error_range)
    return jsonify(result)


@app.route('/falseposition', methods=['POST'])
def falseposition():
    xa = float(request.get_json()['xa'])
    xb = float(request.get_json()['xb'])
    error_range = float(request.get_json()['errorRange'])
    equation = request.get_json()['equation']
    result = FalsePosition().execute(xa, xb, equation, error_range)
    return jsonify(result)


@app.route('/newtonraphson', methods=['GET'])
def newtonraphson():
    xn = float(request.get_json()['xn'])
    error_range = float(request.get_json()['errorRange'])
    equation = request.get_json()['equation']
    result = NewtonRaphson().execute(xn, equation, error_range)
    return jsonify(result)


if __name__ == '__main__':
    app.run()