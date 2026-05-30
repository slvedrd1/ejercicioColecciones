
def sumarDosNumeros():
    """esta funcion permite sumar dos numeros,
       ingresados dentro de la funcion
    """


    num1 = int(input("ingrese numero 1: ")) 
    num2 = int(input("ingrese numero 2: "))

    suma = num1 + num2

    print(f"la suma de {num1} + {num2} es : {suma}")

def sumar(a,b):
    """esta funcion permite sumar dos numeros
        ingresados por parametros
        """
    suma = a + b
    return suma