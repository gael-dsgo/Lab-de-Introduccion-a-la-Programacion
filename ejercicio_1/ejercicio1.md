# Uso de un entorno virtual en Python y verificación con NumPy

Este documento explica cómo crear y usar un **entorno virtual (venv)** en Python y cómo verificar que realmente se está trabajando dentro de él usando **NumPy (`np.`)** en Visual Studio Code.

---

## ¿Qué es un entorno virtual?

Un entorno virtual es un espacio aislado que permite instalar librerías solo para un proyecto específico, evitando conflictos con otros proyectos o con la instalación global de Python.

---

## Crear el entorno virtual

1. Abre tu proyecto en **Visual Studio Code**.
2. Abre la terminal integrada desde **Terminal → New Terminal**.
3. Asegúrate de estar en la carpeta del proyecto.
4. Ejecuta el comando:

```bash
python -m venv env
```

Esto creará una carpeta llamada `env` que contiene el entorno virtual.

---

## Activar el entorno virtual

En **Windows (CMD o PowerShell)** ejecuta:

```bash
env\Scripts\activate
```

Cuando el entorno esté activo, la terminal mostrará algo similar a:

```
(env) C:\ruta\del\proyecto>
```

Esto confirma que el entorno virtual está activo.

---

## Instalar NumPy en el entorno virtual

Con el entorno `(env)` activo, instala NumPy:

```bash
pip install numpy
```

La librería se instalará únicamente dentro del entorno virtual.

---

## Verificar el entorno virtual usando `np.`

> Importante: el indicador `(env)` se confirma en la **terminal**, no con `np.`.

El uso de `np.` sirve para comprobar que **NumPy está instalado y funcionando dentro del entorno virtual**.

1. Abre un archivo Python (por ejemplo `mate.py`).
2. Escribe el siguiente código:

```python
import numpy as np
np.
```

3. Presiona **Ctrl + Space**.

Si aparece una lista de funciones como `array`, `mean`, `zeros`, `sum`, etc., significa que:
- NumPy está instalado correctamente.
- VS Code reconoce el entorno virtual.
- Estás trabajando dentro del `(env)`.

---

## Si no aparece la lista al escribir `np.`

1. Presiona **Ctrl + Shift + P**.
2. Escribe **Python: Select Interpreter**.
3. Selecciona el intérprete que diga algo similar a:

```
Python 3.x (env)
```

4. Guarda el archivo y vuelve a escribir:

```python
import numpy as np
np.
```

---


Y listo, Con estos pasos, el entorno virtual queda correctamente configurado y puedes verificar su funcionamiento usando NumPy.
