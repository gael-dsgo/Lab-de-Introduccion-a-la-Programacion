
print("1. Imprimir una palabra 10 veces.")
print("2. edad por año")
print("3. Numeros impares.")
print("4. Cuenta atras.")
print("5. Inversion, interes y obtencion")
print("6. Triangulo rectangulo de asteriscos.")
print("7. Tablas del 1 al 10")
print("8. Triangulo rectangulo de numeros")
print("9. Contraseñas")
print("10. Numero primo o no")
print("11. Letras una a una")
print("12. Letras en una frase")
print("13. Eco hasta salir")
opcion= input("Selecciona el ejercicio: ")

match opcion:
    case "1":
        palabra = input("Ingresa la palabra: ")
        for i in range(10):
            print(palabra)
    case "2":
        edad=input("Ingresa tu edad: ")
        for i in range(1, int(edad)+1):
            print(i)
    case "3":
        resultado=""
        positivo = int(input("Ingresa un número positivo: "))
        if positivo < 0:
            print("Error: el número debe ser positivo.")
        else:
            for i in range(1, positivo + 1):
                if i % 2 != 0:
                    resultado += str(i) + ", "
            print(resultado[-2])
    case "4": 
        reversa = int(input("Ingresa un número positivo: "))
        for i in range(reversa, 0, -1):
            print(i, end=", ")
    case "5":
        capital = float(input("Ingresa el capital a invertir: "))
        tasa_interes = float(input("Ingresa la tasa de interés anual (en porcentaje): "))
        años = int(input("Ingresa el número de años: "))
        monto_final = capital * (1 + tasa_interes / 100) ** años
        print(f"El monto final después de {años} años es: {monto_final:.2f}")
    case "6": #triangulo rectangulo de asteriscos
        filas = int(input("Ingresa el número de filas para el triángulo: "))
        for i in range(1, filas + 1):
            print("*" * i)
    case "7": 
        for numero in range(1, 11):
            print(f"Tabla de multiplicar del {numero}:")
            for i in range(1, 11):
                resultado = numero * i
                print(f"{numero} x {i} = {resultado}")
            print()
    case "8": #triangulo rectangulo de numeros principiante
        filas = int(input("Ingresa el número de filas para el triángulo: "))
        for i in range(1, filas + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
    case "9":
        while True:
            contraseña = input("Ingresa una contraseña: ")
            if contraseña == "gaelito":
                print("Contraseña correcta. Bienvenido.")
                break
            else:
                print("Contraseña incorrecta. Inténtalo de nuevo.")
    case "10":
        numero = int(input("Ingresa un número: "))
        primo=True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
            if primo and numero > 1:
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
    case "11":
        palabra = input("Ingresa una palabra: ")
        for letra in palabra:
            print(letra)
    case "12": #escribir una frase y muestre el numero de veces que aparece una letra
        frase = input("Ingresa una frase: ")
        letra = input("Ingresa la letra a contar: ")
        contador = frase.count(letra)
        print(f"La letra '{letra}' aparece {contador} veces en la frase.")
    case "13": #eco de todo lo que introduzca el usuario, hasta eccribir salir
        while True:
            entrada = input("Escribe algo (o 'salir' para terminar): ")
            if entrada.lower() == "salir":
                print("Saliendo del programa...")
                break
            else:
                print(f"Eco: {entrada}")
                
 