# Laboratorio 4: implementación de sockets con Python

## Universidad Jorge Tadeo Lozano - Facultad de Ingeniería

### Asignatura: Sistemas Distribuidos

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
   - [Base de Datos](#base-de-datos)
3. [Ejecución](#ejecución)
4. [Créditos](#créditos)

### Descripción General

Este laboratorio tiene como objetivo desarrollar una aplicación de chat en línea utilizando Python, SQLite y manejo de sockets. El sistema permite a los usuarios registrarse, iniciar sesión, enviar mensajes a otros usuarios y recibir mensajes en tiempo real. El servidor maneja múltiples clientes de forma simultánea utilizando `threading`.

### Estructura del Proyecto

El proyecto está dividido en tres archivos principales:

- `db.py`: Encargado de la gestión de la base de datos SQLite, con funciones para registrar usuarios, autenticar usuarios, insertar mensajes y recuperar mensajes.
- `servidor_threading.py`: Implementa el servidor de chat que acepta múltiples conexiones de clientes y permite la transmisión de mensajes entre ellos.
- `usuarios.py`: Código del cliente que permite a los usuarios conectarse al servidor, iniciar sesión, registrarse y enviar mensajes.

#### Base de Datos

El archivo `db.py` maneja la creación de la base de datos `chat.db` y contiene las siguientes funciones principales:

- `create_db()`: Inicializa la base de datos y crea las tablas `users` (para los usuarios registrados) y `messages` (para almacenar los mensajes enviados).
- `register_user(name, username, password)`: Permite registrar un nuevo usuario en la base de datos.
- `authenticate_user(username, password)`: Autentica las credenciales de un usuario al iniciar sesión.
- `insert_message(user_id, message)`: Inserta un nuevo mensaje enviado por un usuario en la base de datos.
- `get_messages()`: Recupera todos los mensajes almacenados junto con el nombre del remitente.

#### Servidor

El servidor, implementado en el archivo `servidor_threading.py`, se encarga de manejar múltiples conexiones de clientes de manera concurrente mediante hilos. Los principales aspectos son:

- Maneja la autenticación de usuarios y permite a los nuevos usuarios registrarse.
- Difunde los mensajes de un cliente a todos los demás usuarios conectados.
- Utiliza `threading.Lock` para asegurar el acceso seguro a la lista de clientes.

#### Cliente

El archivo `usuarios.py` implementa el cliente del chat. Los usuarios pueden:

- Iniciar sesión o registrarse en el sistema.
- Enviar y recibir mensajes del servidor.
- Escuchar continuamente los mensajes de otros usuarios a través de un hilo independiente.

### Flujo de Trabajo

1. **Registro/Iniciar Sesión:** Los usuarios pueden registrarse en el sistema o iniciar sesión si ya tienen una cuenta.
2. **Envio de Mensajes:** Los usuarios pueden enviar mensajes que son almacenados en la base de datos y luego enviados a todos los demás usuarios conectados.
3. **Recepción de Mensajes:** Los clientes escuchan continuamente los mensajes provenientes del servidor y los muestran en la consola.

### Ejecución

#### 1. Iniciar el Servidor

Para iniciar el servidor de chat, ejecutar el archivo `servidor_threading.py`:

```bash
  python servidor_threading.py
```

#### 2. Ejecutar el Cliente

Para conectar un cliente al servidor, ejecutar el archivo `usuarios.py`:

```bash
  python usuarios.py
```

## Créditos

### Desarrollado por

- **Yarley Vanessa Castillo Melo** - Estudiante de Ingeniería de Sistemas, Universidad Jorge Tadeo Lozano
- **Juan Camilo Tique Ducuara** - Estudiante de Ingeniería de Sistemas, Universidad Jorge Tadeo Lozano

### Herramientas Utilizadas

- **Python** - Lenguaje de programación utilizado para el desarrollo de los scripts.
- **CMD de Windows** - Terminal de comandos utilizada para la ejecución de los scripts.
- **SQLite** - Sistema de base de datos utilizado para el almacenamiento de mensajes y usuarios.
