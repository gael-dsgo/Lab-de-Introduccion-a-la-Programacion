# Crear una carpeta en GitHub desde Visual Studio Code

## Requisitos
- Tener **Visual Studio Code** instalado
- Tener **Git** instalado
- Tener un **repositorio de GitHub** ya clonado en tu computadora

## Pasos

### 1. Abrir el proyecto en VS Code
Abre Visual Studio Code y carga la carpeta de tu repositorio.

### 2. Crear la carpeta
En el panel izquierdo (**Explorer**):
- Clic derecho → **New Folder**
- Escribe el nombre de la carpeta

> Nota: GitHub no permite carpetas vacías.

### 3. Crear un archivo dentro de la carpeta
- Clic derecho sobre la carpeta → **New File**
- Ejemplo: `README.md`

### 4. Guardar cambios en Git
- Abre **Source Control** (`Ctrl + Shift + G`)
- Escribe un mensaje de commit (ejemplo: *Agrega nueva carpeta*)
- Clic en **Commit**
- Luego selecciona **Sync Changes** o **Push**

## Método alternativo (terminal integrada)
```bash
mkdir nombre-carpeta
touch nombre-carpeta/README.md
git add .
git commit -m "Agrega carpeta"
git push
```

## Resultado
La carpeta aparecerá correctamente en tu repositorio de GitHub.
