import sympy as sp
from beautifultable import *
import warnings
from static.NumericalMethods.Methods_formulas import MethodsFormulas

warnings.simplefilter(action='ignore', category=FutureWarning)
table = BeautifulTable()


class NewtonRaphson(MethodsFormulas):

    def __init__(self):
        super().__init__()

    def execute(self, xn: float, equation: str, error: float):
        if self.validate_formula(equation):
            x = sp.Symbol('x')
            y = equation
            derivative: str = str(sp.diff(y, x))
            table.column_headers = ["it", "xn", "F(xn)", "F'(xn)", "Xn+1"]
            return self.__process(xn, equation, derivative, error)
        else:
            return "La formula no es correcta"

    def __process(self, xn: float, equation: str, derivative: str, error: float, xn_1old: float = 0, it: int = 0):

        Fxn = self.evaluate_formula(equation, xn)
        Fdxn = self.evaluate_formula(derivative, xn)
        Xn_1 = xn - (Fxn / Fdxn)
        table.append_row([it + 1, xn, Fxn, Fdxn, Xn_1])

        if ( abs(Xn_1 - xn_1old) <= error) & it != 0:
            print(table)
            return Xn_1
        else:
            return self.__process(Xn_1, equation, derivative, error, Xn_1, it + 1)
