
class Prenda:
    def __init__(self, tipo, color, talla):
        self.tipo = tipo
        self.color = color
        self.talla = talla

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}, Color: {self.color}, Talla: {self.talla}")

def backtraking(array, sol, n, level):
    global outfit
    global cnt
    if (n < level):
        for i in array:
            sol[n] = i
            if (sol[n].tipo == "frio"):
                outfit[n] = sol[n].tipo;
            else:
                backtraking(array, sol, n+1, level)
    else:
        print(sol)

def main():
    # n = int(input("Ingrese el numero de niveles: "))
    # binaryDigits = [0, 1]
    # solution = [0 for i in range(n)]
    # numLevels = len(solution)
    #backtraking(binaryDigits, solution, 0, numLevels)

    playera = Prenda("calor", "rojo", "36")
    blusa = Prenda("calor", "rojo", "36")
    bufanda = Prenda("frio", "rojo", "36")
    abrigo = Prenda("frio", "rojo", "36")
    gorro = Prenda("frio", "rojo", "36")
    botas = Prenda("frio", "rojo", "36")
    short = Prenda("calor", "rojo", "36")


    prendas = [playera, blusa, bufanda, abrigo, gorro, botas, short]
    solucion = [0 for i in range(7)]

    backtraking(prendas, solucion, 0, 6)

    print(outfit)
if __name__ == "__main__":
    main()
