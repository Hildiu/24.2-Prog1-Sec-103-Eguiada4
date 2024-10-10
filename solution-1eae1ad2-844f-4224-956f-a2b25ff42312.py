from math import sqrt, pi

def numeroDeDivisores(numero):
    nd = 0
    for divisor in range(2,numero, 1):
        if numero % divisor ==0:
            nd= nd + 1
    return nd

def pregunta_1(numerico: int) -> str:
    """
    Genera un codigo de barras basado en la cantidad de 
    divisores de cada digito del numero ingresado.
    
    Parametros:
    	numerico (int): Numero entero para generar el codigo de barras.
    Retorna:
    	str: Una cadena que representa el codigo de barras '|'
            dependiendo de su cantidad de divisores.
    """
    codigo=""
    cadena = str(numerico)
    for numStr in cadena:
        nd = numeroDeDivisores(int(numStr))
        if nd>0:
            codigo = codigo + "|"*nd
        else:
            codigo = codigo + " "
    return codigo




def area(r,a):
    return 2*pi*r*a + 2*pi*r**2

def volumen(r,a):
    return pi*r**2*a

def pregunta_2(radio: float, altura: float) -> float:
    """
    Calcule la multiplicacion del area y volumen de un cilindro
    Parametros:
        radio (float): El radio del cilindro
        altura (float): La altura del cilindro
    Retorna:
        (float): El resultado es la multiplicacion del area y volumen de un cilindro
    """
    return( area(radio,altura) * volumen(radio,altura) )



def pregunta_3(cad:str)->float:
    """
    Determina la fortaleza de una contrasenya
    Parametros:
        cad (str) : una cadena de caracteres
    Retorna:
        float : Fortaleza de la contrasenya
    """
    caracteres=len(cad)
    digitos = 0
    mayusculas = 0
    minusculas = 0
    for item in cad:
        if item in "0123456789":
            digitos = digitos + 1
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            mayusculas = mayusculas + 1
        if item in "abcdefghijklmnopqrstuvwxyz":
            minusculas = minusculas + 1
    if caracteres<8 or digitos<2 or mayusculas<2 or minusculas<2:
        return 0
    else:
        return round(min(mayusculas,minusculas)*caracteres/digitos,2 )



def pregunta_4(vector: list) -> float:
    """
    Calcula el modulo de un vector.

    Parametros:
        vector (list): Lista de numeros reales que representan el vector.

    Retorna:
        float: Modulo del vector redondeado a 3 decimales.
    """
    modulo =0
    for item in vector:
        modulo  = modulo + item**2
    modulo = sqrt(modulo)
    return round(modulo, 3)
