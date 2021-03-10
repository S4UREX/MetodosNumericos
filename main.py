from helpers.NumericalMethods.Bisection.Bisection import Bisection
from helpers.NumericalMethods.FalsePosition.FalsePosition import FalsePosition
from helpers.NumericalMethods.Newton_Raphson.NewtonRaphson import NewtonRaphson
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/bisection', methods=['POST'])
def bisection():
    json = request.get_json()
    try:
        xi = float(request.get_json()['xi'])
        xu = float(request.get_json()['xu'])
        error_range = float(request.get_json()['errorRange'])
        equation = request.get_json()['equation']
        result = Bisection().execute(xi, xu, equation, error_range)
        return jsonify(
            ok=True,
            msg=result
        )
    except KeyError:
        return jsonify(
            ok=False,
            msg='Faltan argumentos'
        )


@app.route('/falseposition', methods=['POST'])
def falseposition(xa, xb, equation, error_range):
    json = request.get_json()
    try:
        xa = float(xa)
        xb = float(xb)
        error_range = float(error_range)
        result = FalsePosition().execute(xa, xb, equation, error_range)
        return jsonify(
            ok=True,
            msg=result
        )
    except KeyError:
        return jsonify(
            ok=False,
            msg='Faltan argumentos'
        )


@app.route('/newtonraphson', methods=['POST'])
def newtonraphson(xn, equation, error_range):
    json = request.get_json()
    try:
        xn = float(xn)
        error_range = float(error_range)
        result = NewtonRaphson().execute(xn, equation, error_range)
        return jsonify(
            ok=True,
            msg=result
        )
    except KeyError:
        return jsonify(
            ok=False,
            msg='Faltan argumentos'
        )


if __name__ == '__main__':
    app.run(debug=True)
