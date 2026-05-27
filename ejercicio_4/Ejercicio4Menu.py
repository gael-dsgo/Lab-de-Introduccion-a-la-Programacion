Usuario="admin"
Contraseña="Admin2026"
intento=0
VERDE='\033[92m'
ROJO='\033[91m'
RESET='\033[0m'
programa=True
while programa and intento<3:
    print(f"\n--- INTENTO {intento+1} DE 3 ---")
    user=input("Usuario: ")
    if user=="":
        print("No ingresaste un usuario")
        intento+=1
        continue
    if chr(32) in user:
        print("El usuario no puede contener espacios")
        intento+=1
        continue
    passw=input("Contraseña: ")
    letra=any(c.isalpha() for c in passw)
    numero=any(c.isdigit() for c in passw)
    if len(passw)<8:
        print("La contraseña debe tener al menos 8 caracteres")
        intento+=1
        continue
    if not letra:
        print("La contraseña debe contener letras")
        intento+=1
        continue
    if not numero:
        print("La contraseña debe contener números")
        intento+=1
        continue
    if user==Usuario and passw==Contraseña:
        print(f"\n{VERDE}ACCESO CONCEDIDO{RESET}")
        print("Bienvenido al sistema")
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Clasificar número")
            print("2. Categoría de edad y permisos")
            print("3. Calcular tarifa")
            print("4. Cerrar sesión")
            print("5. Salir")
            menu=input("\nSeleccione una opción: ")
            if menu=="1":
                print("\nOpción 1 deshabilitada temporalmente")
            elif menu=="2":
                print("\nOpción 2 deshabilitada temporalmente")
            elif menu=="3":
                print("\nOpción 3 deshabilitada temporalmente")
            elif menu=="4":
                print("\nCerrando sesión...")
                break
            elif menu=="5":
                print("\nHasta luego")
                programa=False
                break
            else:
                print("\nOpción no válida")
        intento=0
        continue
    else:
        print(f"{ROJO}Usuario o contraseña incorrectos{RESET}")
        intento+=1
if intento>=3:
    print(f"{ROJO}Demasiados intentos fallidos. Acceso bloqueado{RESET}")