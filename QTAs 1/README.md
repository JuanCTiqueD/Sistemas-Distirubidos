# Laboratorio 1: Entrada de Datos por Medio de Argumentos en Python

## Universidad Jorge Tadeo Lozano - Facultad de Ingeniería

### Asignatura: Sistemas Distribuidos

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Archivos Incluidos](#archivos-incluidos)
3. [Requisitos Previos](#requisitos-previos)
4. [Instrucciones de Ejecución](#instrucciones-de-ejecución)
   - [Navegación a la Carpeta de Trabajo](#navegación-a-la-carpeta-de-trabajo)
   - [Ejecución de los Scripts](#ejecución-de-los-scripts)
     - [Ejercicio 1: Imprimir Argumentos en Líneas Separadas](#ejercicio-1-imprimir-argumentos-en-líneas-separadas)
     - [Ejercicio 2: Convertir Argumentos a Enteros](#ejercicio-2-convertir-argumentos-a-enteros)
     - [Ejercicio 3: Obtener Mínimo y Máximo](#ejercicio-3-obtener-mínimo-y-máximo)
     - [Ejercicio 4: Ordenar Números](#ejercicio-4-ordenar-números)
     - [Ejercicio 5: Buscar Elemento en una Lista Enlazada](#ejercicio-5-buscar-elemento-en-una-lista-enlazada)
5. [Créditos](#créditos)

### Descripción General

Este laboratorio está diseñado para que los estudiantes se familiaricen con la entrada de argumentos en scripts de Python a través de la terminal de comandos, una habilidad clave en el desarrollo de aplicaciones distribuidas. Los ejercicios abordarán cómo recibir, procesar y manipular datos enviados a los scripts, lo cual es fundamental para la creación de programas que se comuniquen de manera efectiva en sistemas distribuidos.

## Archivos Incluidos

- **`p1.py`**: Imprime cada argumento proporcionado en una línea diferente.
- **`p2.py`**: Convierte los argumentos a enteros, maneja errores y muestra el tipo de dato.
- **`p3.py`**: Convierte argumentos numéricos a enteros, filtra valores no válidos, y encuentra el valor mínimo y máximo.
- **`p4.py`**: Ordena los números proporcionados de mayor a menor después de convertirlos a enteros.
- **`p5.py`**: Crea una lista enlazada a partir de los argumentos proporcionados y busca un elemento específico en ella.

## Requisitos Previos

- **Python**: Debes tener Python instalado en tu computadora. Verifica la instalación ejecutando el siguiente comando en la terminal CMD:

  ```bash
  python --version
  ```

## Instrucciones de Ejecución

### Navegación a la Carpeta de Trabajo

1. Abre la terminal CMD
2. Navega al directorio donde se encuentran los archivos de la carpeta de trabajo.
   En mi caso se encuentran en la siguiente ruta:

```bash
  cd C:\Users\juanc\OneDrive\Desktop\Systems Engeneering\Talleres\Sistemas Distirubidos\QTAs 1
```

#### Ejecución de los Scripts

##### Ejercicio 1: Imprimir Argumentos en Líneas Separadas

Archivo: `p1.py`

Descripción: Este script imprime cada argumento proporcionado en una línea diferente.

**Uso:**

```bash
  python p1.py arg1 arg2 arg3 ...
```

**Salida Esperada:**

```yaml
Argumento 1 = uno
Argumento 2 = 4
Argumento 3 = hola
Argumento 4 = tres
Argumento 5 = 1245
```

##### Ejercicio 2: Convertir Argumentos a Enteros

Archivo: `p2.py`

Descripción: Convierte los argumentos a enteros, maneja errores de conversión, y muestra el tipo de dato.

**Uso:**

```bash
  python p2.py num1 num2 num3 ...
```

**Salida Esperada:**

```yaml
10 es de tipo <class 'int'>
30 es de tipo <class 'int'>
```

##### Ejercicio 3: Obtener Mínimo y Máximo

Archivo: `p3.py`

Descripción: Encuentra el valor mínimo y máximo de una lista de números enteros proporcionados como argumentos. Ademas tambie filtra entradas no válidas.

**Uso:**

```bash
  python p3.py num1 num2 num3 ...
```

**Salida Esperada:**

```yaml
Valor mínimo: 1
Valor máximo: 7
```

##### Ejercicio 4: Ordenar Números

Archivo: `p4.py`

Descripción: Ordena los números de mayor a menor después de convertirlos a enteros.

**Uso:**

```bash
  python p4.py num1 num2 num3 ...
```

**Salida Esperada:**

```yaml
Lista ordenada de mayor a menor: [9, 7, 3]
```

##### Ejercicio 5: Buscar Elemento en una Lista Enlazada

Archivo: `p5.py`

Descripción: Crea una lista enlazada con los números proporcionados y busca un elemento específico.

> NOTA: El primer argumento siempre será el elemento a buscar, desde el segundo argumento en adelante serán elementos que deberá contener la lista enlazada.

**Uso:**

```bash
  python p5.py elemento_a_buscar num1 num2 num3 ...
```

**Salida Esperada:**

```yaml
Elemento 5 encontrado en la posición 4.
```

## Créditos

### Desarrollado por

- **Juan Camilo Tique Ducuara** - Estudiante de Ingeniería de Sistemas, Universidad Jorge Tadeo Lozano

### Herramientas Utilizadas

- **Python** - Lenguaje de programación utilizado para el desarrollo de los scripts.
- **CMD de Windows** - Terminal de comandos utilizada para la ejecución de los scripts.
