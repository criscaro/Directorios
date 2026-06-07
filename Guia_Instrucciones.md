# Guía de Práctica: Comodines (`*`, `?`, `[]`), `file` y `head`

¡Bienvenido a esta guía práctica de comandos de terminal! 

Esta práctica está diseñada para que domines el uso de comodines de búsqueda (globbing) y comandos fundamentales de visualización y análisis de archivos en Linux/UNIX.

Para comenzar, abre una terminal, dirígete al directorio donde se encuentra este proyecto y entra en la carpeta de práctica ejecutando:
```bash
cd practica_comodines
```

---

## Parte 1: Comodines (Globbing)
Los comodines son caracteres especiales que la terminal interpreta para realizar búsquedas o filtrados masivos de nombres de archivos. Los tres principales son:

*   **`*` (Asterisco):** Coincide con cualquier cadena de caracteres (incluyendo ninguna letra o número, es decir, cero o más caracteres).
*   **`?` (Signo de interrogación):** Coincide con exactamente **un** solo carácter.
*   **`[ ]` (Corchetes):** Coinciden con cualquier carácter individual que se encuentre dentro de los corchetes. Se pueden especificar listas (ej. `[abc]`) o rangos (ej. `[a-z]` o `[0-9]`).

### Ejercicios a Resolver:

1.  **Ejercicios con el comodín `*`**
    *   **Ejercicio 1.1:** Escribe el comando para listar todos los archivos dentro de la carpeta que tengan extensión `.txt`.
    *   **Ejercicio 1.2:** Escribe el comando para listar todos los archivos cuyo nombre comience con la palabra `datos`.
    *   **Ejercicio 1.3:** Escribe el comando para listar todos los archivos que contengan la palabra `script` en cualquier parte de su nombre.

2.  **Ejercicios con el comodín `?`**
    *   **Ejercicio 2.1:** Escribe el comando para listar todos los archivos que comiencen con la palabra `archivo`, seguidos de exactamente **un** carácter (cualquiera) y que tengan la extensión `.txt`.
    *   **Ejercicio 2.2:** Escribe el comando para listar todos los archivos cuyos nombres tengan exactamente **5 caracteres** antes de su extensión (pista: usa la combinación de `?` y el punto `.`).

3.  **Ejercicios con el comodín `[ ]`**
    *   **Ejercicio 3.1:** Escribe el comando para listar únicamente los archivos que comiencen con `archivo` seguido de un **número** (del 0 al 9) y tengan extensión `.txt`.
    *   **Ejercicio 3.2:** Escribe el comando para listar los archivos que comiencen con `archivo` seguido de una **letra mayúscula** (de la A a la Z) y tengan extensión `.txt`.
    *   **Ejercicio 3.3:** Escribe el comando para listar todos los archivos que comiencen con la letra `c` o con la letra `n` (de cualquier extensión).

---

## Parte 2: El Comando `file`
El comando `file` analiza el contenido interno de un archivo (mediante cabeceras y firmas de datos o "magic numbers") para decirnos qué tipo de archivo es en realidad, independientemente de la extensión que tenga en su nombre.

### Ejercicios a Resolver:

4.  **Ejercicios con `file`**
    *   **Ejercicio 4.1:** Escribe el comando para averiguar qué tipo de archivo es `vacio.log`. ¿Qué resultado te arroja la terminal y por qué?
    *   **Ejercicio 4.2:** Escribe el comando para comprobar el tipo de archivo de `script_limpieza.sh` y `codigo_calculo.py`. Observa las diferencias entre ambos.
    *   **Ejercicio 4.3:** Escribe el comando para comprobar el tipo de `web_index.html`.
    *   **Ejercicio 4.4:** Escribe un comando combinando `file` con comodines para analizar el tipo de **todos** los archivos de la carpeta a la vez.

---

## Parte 3: El Comando `head`
El comando `head` se utiliza para mostrar por pantalla las primeras líneas de un archivo de texto. Por defecto muestra las primeras **10 líneas**, pero puedes modificar este comportamiento con el parámetro `-n` seguido del número de líneas que deseas ver.

### Ejercicios a Resolver:

5.  **Ejercicios con `head`**
    *   **Ejercicio 5.1:** Escribe el comando para mostrar las primeras 10 líneas de `archivo1.txt`.
    *   **Ejercicio 5.2:** Escribe el comando para mostrar únicamente las primeras **3 líneas** de `archivo1.txt`.
    *   **Ejercicio 5.3:** Escribe el comando para mostrar las primeras **5 líneas** de `datos_2026.csv`. ¿Cuáles son los nombres de las columnas que define este archivo en su primera línea?
