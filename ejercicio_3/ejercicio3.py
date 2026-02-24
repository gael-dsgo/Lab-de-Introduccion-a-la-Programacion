intentos = 0
while intentos < 3:
    usuario = input("Ingresa el Usuario: ")
    if usuario.strip() == "" or " " in usuario:
        print("El usuario no debe estar vacío ni contener espacios.")
        continue
    contraseña = input("Ingresa la Contraseña: ")
    if len(contraseña) < 1 or len(contraseña) > 8:
        print("La contraseña debe tener entre 1 y 8 caracteres.")
        continue
    tiene_letra = any(letra.isalpha() for letra in contraseña)
    tiene_digito = any(numero.isdigit() for numero in contraseña)
    if not tiene_letra or not tiene_digito:
        print("La contraseña debe contener al menos una letra y un dígito.")
        continue
    if usuario == "admin" and contraseña == "Admin2026":
        print("Acceso concedido")
        break
    else:
        intentos += 1
        print(f"Datos incorrectos o contraseña inválida. Intentos restantes: {3 - intentos}")
        if intentos == 3:
            print("Has agotado tus intentos. Acceso denegado.")
            
