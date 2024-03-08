from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

def holamundo():
    return("Hola mundo!")
def suma(x,y):
    return(x+y)
def calcular_edad(fecha_nacimiento):
    ahora = datetime.now()
    edad = relativedelta(ahora, fecha_nacimiento)
    return f"Su edad es de {edad.years} años, {edad.months} meses y {edad.days} días"

def imc(peso, altura):
    imc = peso/(altura**2)
    return imc
def par(x):
    if x % 2 == 0:
        print(f"El número {x} es par")
    else:
        print(f"El {x} es impar")

def area_cuadrado(lado):
    return lado * lado

def area_triangulo(x,y):
    return (x*y)/2

def mostrar_menu():
    print("Seleccione una operación")
    print("1. Hola Mundo!")
    print("2. Suma")
    print("3. Calculdar Edad")
    print("4. IMC")
    print("5. Par o impar")
    print("6. Area del cuadrado")
    print("7. Area del triangulo")
    print("8. Salir")

# Solicitar datos al usuario
while True:
    mostrar_menu()
    opcion = (input("Ingrese el número correspondiente a la operación que desea utilizar: "))

    if opcion == '1':
        print("Hola Mundo!")
    elif opcion == '2':
        a = float(input("Ingrese el primer número:"))
        b = float(input("Ingrese el segundo número"))
        resultado = suma(a,b)
        print(f"El resultado es {resultado}")
    elif opcion == '3':
        # Solicitar la fecha de nacimiento al usuario
        dia = int(input("Ingrese el día de nacimiento: "))
        mes = int(input("Ingrese el mes de nacimiento: "))
        año = int(input("Ingrese el año de nacimiento: "))
        fecha = date(año, mes, dia)
        edad = calcular_edad(fecha)
        print(f"Su edad es de {edad} años")
    elif opcion == '4':
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en m"))
        resultado = imc(peso, altura)
        print(f"Su IMC es {resultado}")
    elif opcion == '5':
        n = int(input("Ingrese un número:"))
        resultado = par(n)
        print(resultado)
    elif opcion == '6':
        lado = float(input("Ingrese el valor del lado del cuadrado"))
        resultado = area_cuadrado(lado)
        print(f"El área del cuadrado es {resultado}")
    elif opcion == '7':
        base = float(input("Ingrese la base del triangulo"))
        altura = float(input("Ingrese la altura del triangulo"))
        resultado = area_triangulo(base, altura)
        print(f"El área del triangulo es {resultado}")
    elif opcion == '8':
        print("Saliendo...")
        break
    else:
        print("Opcion no válida. Ingrese un número de 1 a 8")