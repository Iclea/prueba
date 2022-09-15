from operaciones.potencias import basicas as pot
from operaciones.matematicas import basicas as mat

if __name__ == "__main__":
    print(mat.suma(10, 10))
    print(mat.resta(10, 10))
    print(mat.multiplicacion(10, 10))
    print(mat.division(10, 10))

    print(pot.cuadrado(3))
    print(pot.cubo(3))