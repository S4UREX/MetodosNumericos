from beautifultable import *
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

table = BeautifulTable()

iterations: int

def bisection(xi, xu, equation: str, it: int):
    global iterations
    iterations = it
    table.column_headers = ["it", "xi", "xu", "xr", "F(xi)", "F(xr)", "F(xi)*F(xr)"]
    if validate_formula(equation):
        process(xi, xu, equation)
    else:
        return "La formula no es correcta"


def process(xi: float, xu: float, equation: str, it: int = 0):
    xr: float = (xi + xu) / 2
    row = [it+1, xi, xu, xr]
    Fxi: float = evaluate_formula(equation, xi)
    Fxu: float = evaluate_formula(equation, xu)
    Fxr: float = evaluate_formula(equation, xr)

    if it == iterations:
        return table

    FxixFxr = (Fxi * Fxr)
    row.extend([Fxi, Fxr, FxixFxr])
    table.append_row(row)

    if FxixFxr < 0:
        return process(xi, xr, equation, it + 1)
    else:
        return process(xr, xu, equation, it + 1)


def evaluate_formula(equation: str, value: float):
    x = value
    return eval(equation)


def validate_formula(equation: str):
    try:
        x = 0
        eval(equation)
        return True
    except:
        return False
