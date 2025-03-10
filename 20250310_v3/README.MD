# Programa de Conversión de Texto a Código Morse

Este programa es un traductor de texto a código Morse y también tiene la funcionalidad de escuchar esa traducción. Presenta un menú con las siguientes opciones:
1. Traducir texto a código Morse
2. Reproducir el código Morse
3. Salir

El programa convierte un texto ingresado por el usuario a su equivalente en código Morse. El código Morse es un sistema de codificación de texto que utiliza secuencias de puntos (.) y guiones (-) para representar letras, números y signos de puntuación.

## Descripción del Programa

El programa solicita al usuario ingresar un texto y luego lo convierte a código Morse utilizando un diccionario predefinido que contiene las correspondencias entre caracteres y su representación en Morse. El resultado es una cadena de caracteres Morse donde cada carácter está separado por un espacio para poder distinguirlos. Además, cuenta con una función adicional que permite escuchar la traducción en código Morse.

## Requisitos previos

Antes de ejecutar el programa, asegúrate de tener los siguientes requisitos instalados:

- **Python 3.x**: Este programa fue desarrollado utilizando Python 3. Si aún no lo tienes, puedes descargarlo desde la página oficial de Python:  
    [Descargar Python](https://www.python.org/downloads/)

- **playsound3**: Necesitarás instalar la librería `playsound3` para poder reproducir el sonido del código Morse. Puedes instalarla usando pip:

    pip install playsound3
    

    Más detalles en [PyPI - playsound3](https://pypi.org/project/playsound3/).

## Instrucciones para ejecutar el programa en Windows

1. **Abrir una terminal o línea de comandos**  
   Para abrir una terminal en Windows, sigue estos pasos:

   - Presiona `Win + R`, escribe `cmd` y presiona Enter.
   - Alternativamente, puedes usar PowerShell o Windows Terminal.

2. **Navegar a la carpeta del proyecto**  
   Usa el comando `cd` para cambiar el directorio hasta la carpeta donde descargaste el proyecto y entrar en la carpeta llamada windows. Ejemplo:

    cd ruta\donde\se\encuentra\el\proyecto\windows

3. **Ejecutar el programa**
  Una vez en la carpeta del proyecto, puedes ejecutar el archivo main.py con el siguiente comando:
    python .\main.py

## Instrucciones para ejecutar el programa en Linux

1. **Abrir una terminal**  
   Puedes abrir la terminal en tu sistema Linux presionando Ctrl + Alt + T o buscando "Terminal" en el menú de aplicaciones.

   - Presiona `Win + R`, escribe `cmd` y presiona Enter.
   - Alternativamente, puedes usar PowerShell o Windows Terminal.

2. **Navegar a la carpeta del proyecto**  
   Usa el comando `cd` para cambiar el directorio hasta la carpeta donde descargaste el proyecto y entrar en la carpeta llamada linux. Ejemplo:

    ```cd ruta\donde\se\encuentra\el\proyecto\linux```

3. **Ejecutar el programa**
  Una vez en la carpeta del proyecto, puedes ejecutar el archivo main.py con el siguiente comando:
  Para saber que version de Python, ejecutar
    python3 --version
  
  Si tienes Python instalado correctamente, verás una versión como Python 3.x.x
    ```python3 .\main.py```

  Si solo tienes Python 2.x, utiliza python
    ```python .\main.py```

## Funcionamiento
  **Menú: El programa despliega un menú con las siguientes opciones:**

  1. Traducir texto a código Morse
  2. Reproducir el código Morse del texto codificado
  3. Salir del programa

  **Conversión**
  Opción 1 - Cada carácter del texto se traduce a su equivalente en código Morse utilizando un diccionario predefinido.

  **Reproducción**
  Opción 2 (opcional) - El programa toma el texto ingresado y llama a la función morse_sonido para reproducirlo en código Morse.

  **Salida**
  Opción 3 - Salida del programa.