from os import system

valor1 = int(input("Ingrese su primer numero: "))
valor2 = int(input("Ingrese su primer numero: "))

system("cls")

print("Operacion a seguir\n \n 1 = + \n 2 = - \n 3 = * \n 4 = / \n")
operacion = int(input("Ingrese su operacion: "))

system("cls")

if operacion == 1 :
    resultado = valor1 + valor2
    print ("Resultado final:", resultado)

elif operacion == 2 :
    resultado = valor1 + valor2
    print ("Resultado final:", resultado)

elif operacion == 3 : 
    resultado = valor1 * valor2
    print ("Resultado final:", resultado)
elif operacion == 4 :
    resultado = valor1 / valor2
    print ("Resultado final:", resultado)

else: 
    print("Sin Operacion")