from beautifultable import *
import warnings
from static.NumericalMethods.Methods_formulas import MethodsFormulas

warnings.simplefilter(action='ignore', category=FutureWarning)
table = BeautifulTable()


class Bisection(MethodsFormulas):

    def __init__(self):
        super().__init__()

    def execute(self, xi: float, xu: float, equation: str, error: float):
        if self.check_sqrt(xi, xu, equation):
            if self.validate_formula(equation):
                table.column_headers = ["it", "xi", "xu", "xr", "F(xi)", "F(xr)", "F(xi)*F(xr)"]
                return self.__process(xi, xu, equation, error)
            else:
                return "La formula no es correcta"
        else:
            return "No hay una raíz en el rango especificado"

    # Funcion que busca una raiz por el metodo de biseccion
    def __process(self, xi: float, xu: float, equation: str, error_range: float, xrold: float = 0,
                  it: int = 0) -> float:

        xr: float = (xi + xu) / 2
        row = [it + 1, xi, xu, xr]
        Fxi: float = self.evaluate_formula(equation, xi)
        Fxr: float = self.evaluate_formula(equation, xr)

        FxixFxr = (Fxi * Fxr)
        row.extend([Fxi, Fxr, FxixFxr])
        table.append_row(row)

        # Caso base
        if (abs(xr - xrold) <= error_range) & it != 0:
            print(table)
            return xr
        elif FxixFxr < 0:
            return self.__process(xi, xr, equation, error_range, xu, it + 1)
        else:
            return self.__process(xr, xu, equation, error_range, xi, it + 1)
