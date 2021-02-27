import decimal


class MethodsFormulas(object):

    def __init__(self):
        pass

    def allDecimals(self, x: float):
        return decimal.Decimal.from_float(x)

    # Funcion para dar un resultado a partir de la formula
    def evaluate_formula(self, equation: str, value: float):
        x = value
        return eval(equation)

    # Funcion para verificar si la formula es valida
    def validate_formula(self, equation: str):
        try:
            x = 0
            eval(equation)
            return True
        except:
            return False

    # Funcion para verificar si hay una raiz en el rango especificado
    def check_sqrt(self, xi: float, xu: float, equation: str):
        Fxi = self.evaluate_formula(equation, xi)
        Fxu = self.evaluate_formula(equation, xu)
        return Fxi * Fxu < 0
