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
def falseposition():
    json = request.get_json()
    try:
        xa = float(request.get_json()['xa'])
        xb = float(request.get_json()['xb'])
        error_range = float(request.get_json()['error_range'])
        equation = request.get_json()['equation']
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
def newtonraphson():
    json = request.get_json()
    try:
        xn = float(request.get_json()['xn'])
        error_range = float(request.get_json()['error_range'])
        equation = request.get_json()['equation']
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
