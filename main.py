from static.NumericalMethods.Bisection.Bisection import Bisection
from static.NumericalMethods.FalsePosition.FalsePosition import FalsePosition
from static.NumericalMethods.Newton_Raphson.NewtonRaphson import NewtonRaphson

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/bisection/<xi>/<xu>/<equation>/<error_range>', methods=['GET'])
def bisection(xi, xu, equation, error_range):
    xi = float(xi)
    xu = float(xu)
    error_range = float(error_range)
    result: float = Bisection().execute(xi, xu, equation, error_range)
    print(result)
    return jsonify(msg=result)


@app.route('/falseposition/<xa>/<xb>/<equation>/<error_range>', methods=['GET'])
def falseposition(xa, xb, equation, error_range):
    xa = float(xa)
    xb = float(xb)
    error_range = float(error_range)
    result: float = FalsePosition().execute(xa, xb, equation, error_range)
    return jsonify(msg=result)


@app.route('/newtonraphson/<xn>/<equation>/<error_range>', methods=['GET'])
def newtonraphson(xn, equation, error_range):
    xn = float(xn)
    error_range = float(error_range)
    result = NewtonRaphson().execute(xn, equation, error_range)
    return jsonify(msg=result)


if __name__ == '__main__':
    # app.run()
    print(eval("2*log10(5)"))