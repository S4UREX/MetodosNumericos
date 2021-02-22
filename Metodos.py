from beautifultable import *
import warnings
import decimal

warnings.simplefilter(action='ignore', category=FutureWarning)
table = BeautifulTable()


class Metodos:

    def __init__(self):
        pass

    def execute_bisection(self):
        equation: str = input("Introduzca la formula en términos de X: ")
        xi: float = float(input("Introduzca el xi: "))
        xu: float = float(input("Introduzca el xu: "))
        if self.__check_sqrt(xi, xu, equation):
            error: float = float(input("Introduzca el margen de error: "))
            if self.__validate_formula(equation):
                table.column_headers = ["it", "xi", "xu", "xr", "F(xi)", "F(xr)", "F(xi)*F(xr)"]
                self.__bisection(xi, xu, equation, error)
            else:
                return "La formula no es correcta"
        else:
            print("No hay una raíz en el rango especificado")
            return False

    # Funcion que busca una raiz por el metodo de biseccion
    def __bisection(self, xi: float, xu: float, equation: str, error_range: float, xrold: float = 0, it: int = 0):

        xr: float = (xi + xu) / 2
        row = [it + 1, xi, xu, xr]
        Fxi: float = self.__evaluate_formula(equation, xi)
        Fxr: float = self.__evaluate_formula(equation, xr)

        FxixFxr = (Fxi * Fxr)
        row.extend([Fxi, Fxr, FxixFxr])
        table.append_row(row)

        # Caso base
        if (abs((xr - xrold)/xr) < error_range)*100 & it != 0:
            print(table)
            print("it", it)
            print("xi: ", xi)
            print("xu: ", xu)
            print("xr: ", xr)
            return xr

        if FxixFxr < 0:
            return self.__bisection(xi, xr, equation, error_range, xu, it + 1)
        else:
            return self.__bisection(xr, xu, equation, error_range, xi, it + 1)

    def allDecimals(self, x: float):
        return decimal.Decimal.from_float(x)

    # Funcion para dar un resultado a partir de la formula
    def __evaluate_formula(self, equation: str, value: float):
        x = value
        return eval(equation)

    # Funcion para verificar si la formula es valida
    def __validate_formula(self, equation: str):
        try:
            x = 0
            eval(equation)
            return True
        except:
            return False

    # Funcion para verificar si hay una raiz en el rango especificado
    def __check_sqrt(self, xi: float, xu: float, equation: str):
        Fxi = self.__evaluate_formula(equation, xi)
        Fxu = self.__evaluate_formula(equation, xu)
        return Fxi * Fxu >= 0 if False else True

