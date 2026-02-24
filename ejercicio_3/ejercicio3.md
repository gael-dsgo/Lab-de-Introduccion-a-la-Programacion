# Sistema de Validación de Usuario y Contraseña

## Descripción General

Este programa en Python permite validar un usuario y contraseña con las
siguientes reglas:

-   Máximo **3 intentos**
-   El usuario no puede estar vacío ni contener espacios
-   La contraseña debe:
    -   Tener entre 1 y 8 caracteres
    -   Contener al menos una letra
    -   Contener al menos un dígito
-   Usuario válido: `admin`
-   Contraseña válida: `Admin2026`

------------------------------------------------------------------------

## 1. Inicialización de intentos

Se inicializa la variable `intentos` en 0 para llevar el control de los
intentos fallidos.

## 2. Bucle principal

Se utiliza un ciclo `while intentos < 3` para permitir hasta tres
intentos de acceso.

## 3. Validación del usuario

Se solicita el usuario con `input()` y se valida que:

-   No esté vacío (`usuario.strip() == ""`)
-   No contenga espacios (`" " in usuario`)

Si no cumple estas condiciones, el programa muestra un mensaje y
reinicia el ciclo con `continue`.

## 4. Validación de longitud de contraseña

Se solicita la contraseña y se verifica que tenga entre 1 y 8 caracteres
usando:

`len(contraseña)`

Si no cumple, se muestra un mensaje y se reinicia el ciclo.

## 5. Validación de contenido (letra y número)

Se usan las funciones:

-   `isalpha()` para detectar letras
-   `isdigit()` para detectar números
-   `any()` para verificar que exista al menos una coincidencia

Si la contraseña no contiene al menos una letra y un dígito, se reinicia
el ciclo.

## 6. Verificación de credenciales

Se comparan directamente:

`usuario == "admin"`\
`contraseña == "Admin2026"`

Si ambas coinciden, se muestra "Acceso concedido" y se usa `break` para
salir del ciclo.

## 7. Manejo de intentos fallidos

Si los datos no coinciden:

-   Se incrementa `intentos += 1`
-   Se muestran los intentos restantes
-   Si se llega a 3 intentos, se muestra "Acceso denegado"

