"""1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”"""
print("Hola Mundo!")

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
"""
nombre = input("ingrese su nombre: ")
print(f"hola {nombre}")

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
residencia = input("ingrese su lugar de residencia: ")
print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""

radio = float(input("ingrese el radio del circulo: "))
pi = 3.14
perimetro = (pi*2)*radio
area = pi*(radio**2)

print(f"el perimetro es: {perimetro}, y el area es: {area}")

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""

segundos = int(input("ingrese una cantidad de segundos: "))
horas = segundos/3600
print(f"sus segundos convertidos a hs son equivalentes a {horas} hs")

"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""

numero = int(input("ingresa un numero del 1 al 9: "))
print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")

"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""

numero1 = int(input("ingrese el primer numero distinto de 0: "))
numero2 = int(input("ingrese el segundo numero distinto de 0: "))

print(f"la suma de los numeros es {numero1+numero2}")
print(f"la resta de los numeros es {numero1-numero2}")
print(f"la multiplicacion de los numeros es {numero1*numero2}")
print(f"la division de los numeros es {numero1/numero2}")


"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
"""

altura = float(input("ingrese su altura: "))
peso = float(input("ingrese su peso: "))

imc = peso/(altura**2)

print(f"su imc es: {imc}")

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
"""

temp = float(input("ingrese la temperatura en grados celcius: "))
print(f"el equivalente en fahrenheit es: {((9/5)*temp)+32}")

"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el terser numero: "))

print(f"el promedio de los numeros es: {(numero1+numero2+numero3)/3}")
