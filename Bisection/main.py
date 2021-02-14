import biseccion

if __name__ == '__main__':
    equation: str = input("Introduzca la formula en términos de X: ")
    xi: float = float(input("Introduzca el xi: "))
    xu: float = float(input("Introduzca el xu: "))
    iterations: int = int(input("Introduzca el número de iteraciones: "))
    print(biseccion.bisection(xi, xu, equation, iterations))




