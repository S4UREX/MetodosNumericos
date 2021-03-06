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


@app.route('/falseposition/<xa>/<xb>/<equation>/<error_range>', methods=['GET'])
def falseposition(xa, xb, equation, error_range):
    xa = float(xa)
    xb = float(xb)
    error_range = float(error_range)
    result = FalsePosition().execute(xa, xb, equation, error_range)
    return jsonify(msg=result)


@app.route('/newtonraphson/<xn>/<equation>/<error_range>', methods=['GET'])
def newtonraphson(xn, equation, error_range):
    xn = float(xn)
    error_range = float(error_range)
    result = NewtonRaphson().execute(xn, equation, error_range)
    return jsonify(msg=result)


if __name__ == '__main__':
    app.run()